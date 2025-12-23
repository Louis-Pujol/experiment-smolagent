"""
Custom Tools Example
====================

This example shows how to create custom tools for your agent.

Creating custom tools is straightforward: inherit from the Tool class
and implement the required methods.
"""

# %%
# Creating a Custom Tool
# ----------------------
#
# Let's create a simple tool that reverses a string.

from agentexp import Tool


class ReverseStringTool(Tool):
    """A simple tool that reverses strings."""

    @property
    def name(self) -> str:
        return "reverse_string"

    @property
    def description(self) -> str:
        return (
            "Reverses a string. Takes a 'text' argument and returns it reversed. "
            "Example: reverse_string(text='hello') returns 'olleh'"
        )

    def execute(self, text: str) -> str:
        """Reverse the input text."""
        return text[::-1]


# %%
# Testing the Tool Directly
# --------------------------

tool = ReverseStringTool()
print(f"Tool name: {tool.name}")
print(f"Tool description: {tool.description}")
print(f"Reverse 'hello': {tool.execute(text='hello')}")

# %%
# Using the Tool with an Agent
# -----------------------------
#
# Now let's use this tool with an agent. Note that for this example,
# we'll skip the actual agent execution since it requires an API key.

# from agentexp import OpenRouterProvider
#
# llm_provider = OpenRouterProvider()
# agent = Agent(llm_provider=llm_provider, tools=[tool])
#
# result = agent.run("Please reverse the string 'smolagent'", verbose=True)
# print(f"Result: {result}")

# %%
# Creating More Complex Tools
# ----------------------------
#
# Tools can be as simple or complex as needed. Here's a tool that
# performs multiple operations.


class TextAnalysisTool(Tool):
    """Analyzes text and returns statistics."""

    @property
    def name(self) -> str:
        return "analyze_text"

    @property
    def description(self) -> str:
        return (
            "Analyzes text and returns statistics including length, word count, "
            "and character counts. Takes a 'text' argument."
        )

    def execute(self, text: str) -> dict:
        """Analyze the text and return statistics."""
        return {
            "length": len(text),
            "words": len(text.split()),
            "unique_chars": len(set(text)),
            "uppercase": sum(1 for c in text if c.isupper()),
            "lowercase": sum(1 for c in text if c.islower()),
        }


# Test the analysis tool
analysis_tool = TextAnalysisTool()
result = analysis_tool.execute(text="Hello World from Smolagent!")
print("\nText Analysis Result:")
for key, value in result.items():
    print(f"  {key}: {value}")

# %%
# Best Practices for Custom Tools
# --------------------------------
#
# 1. **Clear Names**: Use descriptive names for your tools
# 2. **Detailed Descriptions**: Include parameter names and examples
# 3. **Error Handling**: Handle errors gracefully and return helpful messages
# 4. **Type Hints**: Use type hints for better code quality
# 5. **Documentation**: Document your tools well for educational purposes
