"""Tests for core agent functionality."""

import pytest

from smolagent.agent import Agent
from smolagent.llm import LLMProvider
from smolagent.tools import Tool


class MockLLMProvider(LLMProvider):
    """Mock LLM provider for testing."""

    def __init__(self, responses):
        """Initialize with a list of responses to return."""
        self.responses = responses
        self.call_count = 0

    def generate(self, messages, **kwargs):
        """Return the next response in the list."""
        if self.call_count >= len(self.responses):
            raise RuntimeError("No more mock responses")
        response = self.responses[self.call_count]
        self.call_count += 1
        return response


class MockTool(Tool):
    """Mock tool for testing."""

    def __init__(self, name="mock_tool", description="A mock tool", result="success"):
        self._name = name
        self._description = description
        self.result = result
        self.call_count = 0
        self.last_args = None

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def execute(self, **kwargs):
        self.call_count += 1
        self.last_args = kwargs
        return self.result


class TestAgent:
    """Test the Agent class."""

    def test_agent_initialization(self):
        """Test agent can be initialized."""
        llm = MockLLMProvider([])
        tools = [MockTool()]
        agent = Agent(llm, tools)
        assert agent is not None
        assert len(agent.tools) == 1

    def test_agent_simple_task(self):
        """Test agent can complete a simple task."""
        responses = ['{"final_answer": "The answer is 42"}']
        llm = MockLLMProvider(responses)
        tools = [MockTool()]
        agent = Agent(llm, tools)

        result = agent.run("What is the meaning of life?")
        assert result == "The answer is 42"

    def test_agent_uses_tool(self):
        """Test agent can use a tool."""
        tool = MockTool(result="tool output")
        responses = [
            '{"tool": "mock_tool", "arguments": {"param": "value"}}',
            '{"final_answer": "Task complete"}',
        ]
        llm = MockLLMProvider(responses)
        agent = Agent(llm, [tool])

        result = agent.run("Do something")
        assert result == "Task complete"
        assert tool.call_count == 1
        assert tool.last_args == {"param": "value"}

    def test_agent_max_iterations(self):
        """Test agent raises error when max iterations exceeded."""
        responses = ['{"tool": "mock_tool", "arguments": {}}'] * 20
        llm = MockLLMProvider(responses)
        tools = [MockTool()]
        agent = Agent(llm, tools, max_iterations=5)

        with pytest.raises(RuntimeError) as exc_info:
            agent.run("Do something")
        assert "Max iterations" in str(exc_info.value)

    def test_agent_unknown_tool(self):
        """Test agent handles unknown tool gracefully."""
        responses = [
            '{"tool": "unknown_tool", "arguments": {}}',
            '{"final_answer": "I cannot complete this task"}',
        ]
        llm = MockLLMProvider(responses)
        tools = [MockTool()]
        agent = Agent(llm, tools)

        result = agent.run("Use unknown tool")
        assert result == "I cannot complete this task"

    def test_agent_tool_error(self):
        """Test agent handles tool errors gracefully."""
        tool = MockTool()

        def error_execute(**kwargs):
            raise ValueError("Tool error")

        tool.execute = error_execute

        responses = [
            '{"tool": "mock_tool", "arguments": {}}',
            '{"final_answer": "Error handled"}',
        ]
        llm = MockLLMProvider(responses)
        agent = Agent(llm, [tool])

        result = agent.run("Do something")
        assert result == "Error handled"

    def test_agent_invalid_json(self):
        """Test agent handles invalid JSON responses."""
        responses = [
            "This is not JSON",
            '{"final_answer": "Recovered"}',
        ]
        llm = MockLLMProvider(responses)
        tools = [MockTool()]
        agent = Agent(llm, tools)

        result = agent.run("Do something")
        assert result == "Recovered"
