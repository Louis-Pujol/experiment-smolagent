"""
Calculator Agent Example
========================

This example demonstrates a calculator agent that can perform mathematical
computations and verify results using Python's math functions.

The agent is LLM-agnostic and uses OpenRouter by default with a free model.
"""

# %%
# Setting up the Agent
# --------------------
#
# First, we need to set up our agent with the LLM provider and calculator tools.
# The OpenRouter provider uses a free model by default, so you just need to
# set the OPENROUTER_API_KEY environment variable.

import os

from agentexp import Agent, OpenRouterProvider
from agentexp.calculator_tools import (
    CalculatorTool,
    MathFunctionTool,
    VerifyCalculationTool,
)

# Check if API key is available
HAS_API_KEY = os.environ.get("OPENROUTER_API_KEY") is not None

if HAS_API_KEY:
    # Initialize the LLM provider
    llm_provider = OpenRouterProvider(
        model="google/gemini-2.0-flash-exp:free"  # Free model
    )

    # Create the calculator tools
    tools = [
        CalculatorTool(),
        MathFunctionTool(),
        VerifyCalculationTool(),
    ]

    # Create the agent
    agent = Agent(llm_provider=llm_provider, tools=tools, max_iterations=10)
else:
    print("Note: OPENROUTER_API_KEY not set. Examples will show code only.")
    print("Get a free API key at https://openrouter.ai/")

# %%
# Basic Arithmetic
# ----------------
#
# Let's start with a simple arithmetic problem.

if HAS_API_KEY:
    print("=== Basic Arithmetic ===")
    result = agent.run("What is 15 * 23 + 47?", verbose=True)
    print(f"\nFinal Answer: {result}")
else:
    print("Example code:")
    print('agent.run("What is 15 * 23 + 47?", verbose=True)')

# %%
# Verifying Calculations
# ----------------------
#
# The agent can verify if calculations are correct.

if HAS_API_KEY:
    print("\n=== Verifying Calculations ===")
    result = agent.run(
        "Is the calculation '25 * 4 = 100' correct? Please verify.",
        verbose=True,
    )
    print(f"\nFinal Answer: {result}")
else:
    print("Example code:")
    print("agent.run(\"Is the calculation '25 * 4 = 100' correct?\", verbose=True)")

# %%
# Advanced Math Functions
# -----------------------
#
# The agent can use Python's math functions for more complex operations.

if HAS_API_KEY:
    print("\n=== Advanced Math Functions ===")
    result = agent.run(
        "What is the square root of 144 plus the factorial of 5?",
        verbose=True,
    )
    print(f"\nFinal Answer: {result}")
else:
    print("Example code:")
    print('agent.run("What is the square root of 144 plus the factorial of 5?")')

# %%
# Complex Multi-Step Problems
# ---------------------------
#
# The agent can break down complex problems into steps.

if HAS_API_KEY:
    print("\n=== Complex Problem ===")
    result = agent.run(
        "Calculate the area of a circle with radius 7. Use pi = 3.14159",
        verbose=True,
    )
    print(f"\nFinal Answer: {result}")
else:
    print("Example code:")
    print('agent.run("Calculate the area of a circle with radius 7")')

# %%
# Key Takeaways
# -------------
#
# - The agent is LLM-agnostic and can work with any provider
# - OpenRouter provides easy access to multiple LLMs including free models
# - Tools allow the agent to perform and verify calculations
# - The agent can handle multi-step reasoning
