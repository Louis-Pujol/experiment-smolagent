# Quick Start Guide

Welcome to AgentExp! This guide will help you get started quickly.

## Installation

```bash
# Clone the repository
git clone https://github.com/Louis-Pujol/experiment-agentexp.git
cd experiment-agentexp

# Install in development mode
pip install -e ".[dev]"
```

## Get Your Free API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Set the environment variable:

```bash
export OPENROUTER_API_KEY="your-api-key-here"
```

## Run the Demo

Try the demo script to see the tools in action without needing an API key:

```bash
python demo.py
```

## Your First Agent

Create a file called `my_first_agent.py`:

```python
import os
from agentexp import Agent, OpenRouterProvider
from agentexp.calculator_tools import CalculatorTool, MathFunctionTool

# Initialize the LLM provider
llm = OpenRouterProvider()  # Uses OPENROUTER_API_KEY from environment

# Create tools
tools = [
    CalculatorTool(),
    MathFunctionTool(),
]

# Create the agent
agent = Agent(llm_provider=llm, tools=tools)

# Run a task
result = agent.run("What is the square root of 144 plus 10?", verbose=True)
print(f"\nFinal Answer: {result}")
```

Run it:

```bash
python my_first_agent.py
```

## Try Different Tasks

```python
# Basic arithmetic
agent.run("What is 25 * 4?")

# Using math functions
agent.run("Calculate the factorial of 5")

# Complex multi-step
agent.run("What is the square root of 256 times the factorial of 3?")

# Verification
agent.run("Is 15 * 8 equal to 120?")
```

## Development Workflow

```bash
# Format code
ruff format .

# Check for issues
ruff check .

# Run tests
pytest

# Run tests with coverage
pytest --cov=agentexp

# Install pre-commit hooks
pre-commit install
```

## Next Steps

- Read the [User Guide](docs/user_guide.md) for detailed documentation
- Check out the [Examples](examples/) for more use cases
- Learn how to [create custom tools](examples/plot_custom_tools.py)

## Project Structure

```
agentexp/
├── agent.py              # Core agent orchestration
├── tools.py              # Base tool class
├── llm.py                # LLM provider abstraction
└── calculator_tools.py   # Calculator tool implementations

tests/
├── test_agent.py         # Agent tests
├── test_tools.py         # Tool tests
├── test_llm.py           # LLM provider tests
└── test_calculator_tools.py  # Calculator tool tests

examples/
├── plot_calculator_agent.py  # Calculator agent example
└── plot_custom_tools.py      # Custom tools example

docs/
├── index.rst             # Documentation home
├── getting_started.md    # Getting started guide
├── user_guide.md         # Detailed user guide
└── api_reference.rst     # API documentation
```

## Need Help?

- Check the [documentation](docs/)
- Look at the [examples](examples/)
- Run the [demo](demo.py)
- Read the [tests](tests/) for usage examples
