"""
Example: Using the Calculator Agent

This script demonstrates how to use the calculator agent with OpenRouter.
You need to set the OPENROUTER_API_KEY environment variable to run this.

Get a free API key at: https://openrouter.ai/
"""

import os
import sys

from agentexp import Agent, OpenRouterProvider
from agentexp.calculator_tools import (
    CalculatorTool,
    MathFunctionTool,
    VerifyCalculationTool,
)


def main():
    # Check if API key is set
    if not os.environ.get("OPENROUTER_API_KEY"):
        print("ERROR: OPENROUTER_API_KEY environment variable is not set!")
        print("\nTo use this example:")
        print("1. Get a free API key from https://openrouter.ai/")
        print("2. Set the environment variable:")
        print("   export OPENROUTER_API_KEY='your-api-key-here'")
        print("\nOr run the demo.py script to see the tools without an API key.")
        sys.exit(1)

    # Initialize the LLM provider
    print("Initializing OpenRouter LLM provider...")
    llm = OpenRouterProvider()

    # Create calculator tools
    tools = [
        CalculatorTool(),
        MathFunctionTool(),
        VerifyCalculationTool(),
    ]

    # Create the agent
    agent = Agent(llm_provider=llm, tools=tools, max_iterations=10)

    # Example tasks
    tasks = [
        "What is 15 * 23 + 47?",
        "Calculate the square root of 144",
        "What is the factorial of 5 plus 10?",
        "Is the calculation '25 * 4 = 100' correct?",
    ]

    print("\n" + "=" * 70)
    print("Calculator Agent Examples")
    print("=" * 70)

    for i, task in enumerate(tasks, 1):
        print(f"\n\nTask {i}: {task}")
        print("-" * 70)
        try:
            result = agent.run(task, verbose=True)
            print(f"\n✓ Final Answer: {result}")
        except Exception as e:
            print(f"\n✗ Error: {str(e)}")

    print("\n" + "=" * 70)
    print("Examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()
