# Getting Started

## Installation

You can install the package in development mode:

```bash
pip install -e .
```

Or install with development dependencies:

```bash
pip install -e ".[dev]"
```

## Setting up OpenRouter

Smolagent uses OpenRouter by default, which provides access to multiple LLMs
including free models. To get started:

1. Go to [https://openrouter.ai/](https://openrouter.ai/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Set the environment variable:

```bash
export OPENROUTER_API_KEY="your-api-key"
```

## Your First Agent

Here's a simple example to get you started:

```python
from smolagent import Agent, OpenRouterProvider
from smolagent.calculator_tools import CalculatorTool, MathFunctionTool

# Initialize the LLM provider
llm = OpenRouterProvider()

# Create tools
tools = [
    CalculatorTool(),
    MathFunctionTool(),
]

# Create the agent
agent = Agent(llm_provider=llm, tools=tools)

# Run a task
result = agent.run("What is the square root of 144?", verbose=True)
print(f"Answer: {result}")
```

## Next Steps

- Check out the [User Guide](user_guide.md) for more details
- See the [Examples](auto_examples/index.rst) for more use cases
- Read the [API Reference](api_reference.rst) for detailed documentation
