"""
Simple demo script for the calculator agent.

This script demonstrates the basic usage of the calculator agent
without requiring an API key (uses mock for demo purposes).
"""

from agentexp.calculator_tools import (
    CalculatorTool,
    MathFunctionTool,
    VerifyCalculationTool,
)


def demo_tools_directly():
    """Demonstrate using the tools directly without an agent."""
    print("=" * 60)
    print("Demo: Using Calculator Tools Directly")
    print("=" * 60)

    # Calculator tool
    calc = CalculatorTool()
    print(f"\nTool: {calc.name}")
    print("Expression: 2 + 2 * 3")
    result = calc.execute(expression="2 + 2 * 3")
    print(f"Result: {result}")

    print("\nExpression: (10 + 5) * 2")
    result = calc.execute(expression="(10 + 5) * 2")
    print(f"Result: {result}")

    # Math function tool
    math_tool = MathFunctionTool()
    print(f"\n\nTool: {math_tool.name}")
    print("Function: sqrt(144)")
    result = math_tool.execute(function="sqrt", value=144)
    print(f"Result: {result}")

    print("\nFunction: factorial(5)")
    result = math_tool.execute(function="factorial", value=5)
    print(f"Result: {result}")

    # Verify calculation tool
    verify = VerifyCalculationTool()
    print(f"\n\nTool: {verify.name}")
    print("Verify: 25 * 4 = 100")
    result = verify.execute(expression="25 * 4", expected=100)
    print(f"Result: {result}")

    print("\nVerify: 25 * 4 = 101 (should be False)")
    result = verify.execute(expression="25 * 4", expected=101)
    print(f"Result: {result}")


def demo_agent_structure():
    """Demonstrate the agent structure (without making actual LLM calls)."""
    print("\n\n" + "=" * 60)
    print("Demo: Agent Structure")
    print("=" * 60)

    # Create tools
    tools = [
        CalculatorTool(),
        MathFunctionTool(),
        VerifyCalculationTool(),
    ]

    print("\nAvailable tools:")
    for tool in tools:
        print(f"  - {tool.name}: {tool.description[:80]}...")

    print("\nTo use the agent with a real LLM:")
    print("  1. Get a free API key from https://openrouter.ai/")
    print("  2. Set environment variable: export OPENROUTER_API_KEY='your-key'")
    print("  3. Run the following code:")
    print()
    print("  from agentexp import Agent, OpenRouterProvider")
    print("  llm = OpenRouterProvider()")
    print("  agent = Agent(llm_provider=llm, tools=tools)")
    print("  result = agent.run('What is 15 * 23 + 47?', verbose=True)")


if __name__ == "__main__":
    # Run demos
    demo_tools_directly()
    demo_agent_structure()

    print("\n" + "=" * 60)
    print("Demo completed! Check the examples/ folder for more.")
    print("=" * 60)
