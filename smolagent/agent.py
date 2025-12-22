"""
Core Agent implementation.

The Agent is the main class that orchestrates tool use and LLM interaction
to accomplish tasks.
"""

import json
import re
from typing import Any

from smolagent.llm import LLMProvider
from smolagent.tools import Tool


class Agent:
    """
    An AI agent that can use tools to accomplish tasks.

    The agent uses an LLM to decide which tools to use and how to use them
    to accomplish a given task. It follows a simple loop:
    1. Receive a task
    2. Think about what to do
    3. Use a tool (if needed)
    4. Observe the result
    5. Repeat until task is complete
    """

    def __init__(
        self,
        llm_provider: LLMProvider,
        tools: list[Tool],
        max_iterations: int = 10,
    ):
        """
        Initialize the agent.

        Args:
            llm_provider: The LLM provider to use for reasoning
            tools: List of tools available to the agent
            max_iterations: Maximum number of reasoning iterations
        """
        self.llm_provider = llm_provider
        self.tools = {tool.name: tool for tool in tools}
        self.max_iterations = max_iterations

    def _format_tools_description(self) -> str:
        """Format tool descriptions for the LLM prompt."""
        descriptions = []
        for tool in self.tools.values():
            descriptions.append(f"- {tool.name}: {tool.description}")
        return "\n".join(descriptions)

    def _create_system_prompt(self) -> str:
        """Create the system prompt that defines the agent's behavior."""
        tools_desc = self._format_tools_description()
        return f"""You are a helpful AI assistant that can use tools to \
accomplish tasks.

Available tools:
{tools_desc}

To use a tool, respond with a JSON object in this format:
{{"tool": "tool_name", "arguments": {{"arg1": "value1", "arg2": "value2"}}}}

When you have completed the task, respond with:
{{"final_answer": "your answer here"}}

Always think step by step and use tools to verify your work when possible.
"""

    def run(self, task: str, verbose: bool = False) -> str:
        """
        Run the agent on a task.

        Args:
            task: The task description
            verbose: Whether to print intermediate steps

        Returns:
            The final answer

        Raises:
            RuntimeError: If max iterations exceeded or task fails
        """
        messages = [
            {"role": "system", "content": self._create_system_prompt()},
            {"role": "user", "content": task},
        ]

        for iteration in range(self.max_iterations):
            if verbose:
                print(f"\n=== Iteration {iteration + 1} ===")

            # Get LLM response
            response = self.llm_provider.generate(messages)

            if verbose:
                print(f"Agent: {response}")

            # Add assistant response to messages
            messages.append({"role": "assistant", "content": response})

            # Try to parse as JSON
            try:
                action = self._parse_action(response)
            except json.JSONDecodeError:
                # If not JSON, ask for clarification
                messages.append(
                    {
                        "role": "user",
                        "content": "Please respond with a valid JSON object.",
                    }
                )
                continue

            # Check for final answer
            if "final_answer" in action:
                return action["final_answer"]

            # Execute tool
            if "tool" in action:
                tool_name = action["tool"]
                tool_args = action.get("arguments", {})

                if tool_name not in self.tools:
                    error_msg = f"Unknown tool: {tool_name}"
                    if verbose:
                        print(f"Error: {error_msg}")
                    messages.append({"role": "user", "content": error_msg})
                    continue

                try:
                    result = self.tools[tool_name].execute(**tool_args)
                    result_msg = f"Tool result: {result}"
                    if verbose:
                        print(result_msg)
                    messages.append({"role": "user", "content": result_msg})
                except Exception as e:
                    error_msg = f"Tool error: {str(e)}"
                    if verbose:
                        print(error_msg)
                    messages.append({"role": "user", "content": error_msg})
            else:
                messages.append(
                    {
                        "role": "user",
                        "content": (
                            "Please specify a tool to use or provide a final_answer."
                        ),
                    }
                )

        raise RuntimeError(f"Max iterations ({self.max_iterations}) exceeded")

    def _parse_action(self, response: str) -> dict[str, Any]:
        """
        Parse the agent's response to extract the action.

        Args:
            response: The LLM response text

        Returns:
            Parsed action dictionary

        Raises:
            json.JSONDecodeError: If response is not valid JSON
        """
        # Try to find JSON in the response
        json_match = re.search(r"\{.*\}", response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        # If no JSON found, try to parse the whole response
        return json.loads(response)
