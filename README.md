# AgentExp 🤖

An educational, LLM-agnostic agent framework for building AI agents with tool use capabilities.

[![CI](https://github.com/Louis-Pujol/experiment-agentexp/actions/workflows/ci.yml/badge.svg)](https://github.com/Louis-Pujol/experiment-agentexp/actions/workflows/ci.yml)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Tests](https://img.shields.io/badge/tests-pytest-blue.svg)](https://pytest.org/)

## Features

- 🎓 **Educational**: Clean, well-documented code designed for learning
- 🔄 **LLM-Agnostic**: Works with any LLM provider (OpenRouter, OpenAI, Anthropic, etc.)
- 🛠️ **Extensible**: Easy to create and add custom tools
- ✨ **Production-Ready**: Includes ruff linting, pre-commit hooks, and comprehensive tests
- 📚 **Well-Documented**: Sphinx documentation with gallery examples

## Quick Start

### Installation

```bash
pip install -e .
```

For development with all tools:

```bash
pip install -e ".[dev]"
```

### Basic Usage

```python
from agentexp import Agent, OpenRouterProvider
from agentexp.calculator_tools import CalculatorTool, MathFunctionTool

# Set up LLM provider (get free API key at https://openrouter.ai/)
llm = OpenRouterProvider(api_key="your-key")

# Create tools
tools = [CalculatorTool(), MathFunctionTool()]

# Create and run agent
agent = Agent(llm_provider=llm, tools=tools)
result = agent.run("What is the square root of 144?", verbose=True)
print(result)  # Output: The square root of 144 is 12.
```

## Calculator Agent Example

The package includes a complete calculator agent that can:
- Perform basic arithmetic operations
- Use Python math functions (sqrt, sin, cos, log, etc.)
- Verify computation results
- Break down complex multi-step problems

### Example Tasks

```python
# Basic arithmetic
agent.run("What is 15 * 23 + 47?")

# Using math functions
agent.run("Calculate the factorial of 5 plus the square root of 144")

# Verification
agent.run("Is the calculation '25 * 4 = 100' correct?")

# Complex problems
agent.run("Calculate the area of a circle with radius 7")
```

## LLM Providers

### OpenRouter (Recommended)

OpenRouter provides access to multiple LLMs through a single API, including free models:

```python
from agentexp import OpenRouterProvider

# Default free model (Google Gemini Flash)
llm = OpenRouterProvider(api_key="your-key")

# Or choose a specific model
llm = OpenRouterProvider(
    api_key="your-key",
    model="anthropic/claude-3-haiku"
)
```

Get a free API key at [https://openrouter.ai/](https://openrouter.ai/)

### Custom Provider

Implement your own provider by inheriting from `LLMProvider`:

```python
from agentexp import LLMProvider

class MyProvider(LLMProvider):
    def generate(self, messages, **kwargs):
        # Your implementation
        return "response"
```

## Creating Custom Tools

Tools are simple to create:

```python
from agentexp import Tool

class MyTool(Tool):
    @property
    def name(self):
        return "my_tool"

    @property
    def description(self):
        return "Clear description of what the tool does"

    def execute(self, **kwargs):
        # Your logic here
        return result
```

## Development

### Linting and Formatting

The project uses [Ruff](https://github.com/astral-sh/ruff) for linting and formatting:

```bash
# Format code
ruff format .

# Check for issues
ruff check .

# Fix issues automatically
ruff check --fix .
```

### Pre-commit Hooks

Install pre-commit hooks to automatically check code before committing:

```bash
pre-commit install
```

Run manually:

```bash
pre-commit run --all-files
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=agentexp --cov-report=term-missing

# Run specific test file
pytest tests/test_agent.py
```

### Building Documentation

```bash
cd docs
make html
open _build/html/index.html
```

## Documentation

Full documentation is available in the `docs` folder and includes:

- **Getting Started Guide**: Installation and basic usage
- **User Guide**: Detailed explanations of concepts and features
- **API Reference**: Complete API documentation
- **Examples Gallery**: Interactive examples with the calculator agent

## Project Structure

```
experiment-smolagent/
├── src/
│   └── agentexp/           # Main package
│       ├── __init__.py
│       ├── agent.py        # Core agent implementation
│       ├── tools.py        # Base tool class
│       ├── llm.py          # LLM provider abstraction
│       └── calculator_tools.py # Calculator tool implementations
├── tests/                  # Test suite
│   ├── test_agent.py
│   ├── test_tools.py
│   ├── test_llm.py
│   └── test_calculator_tools.py
├── examples/               # Sphinx gallery examples
│   ├── plot_calculator_agent.py
│   └── plot_custom_tools.py
├── docs/                   # Sphinx documentation
│   ├── conf.py
│   ├── index.rst
│   ├── getting_started.md
│   ├── user_guide.md
│   └── api_reference.rst
├── pyproject.toml          # Project configuration
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md               # This file
```

## Key Design Principles

1. **Educational Focus**: Code is written to be clear and understandable, with extensive comments and documentation
2. **LLM-Agnostic**: The framework doesn't depend on any specific LLM provider
3. **Tool-Based**: Agents extend their capabilities through tools
4. **Production Quality**: Includes linting, testing, and documentation best practices

## Contributing

Contributions are welcome! Please ensure:

- Code passes ruff checks: `ruff check .`
- Tests pass: `pytest`
- Pre-commit hooks pass: `pre-commit run --all-files`
- New features include tests and documentation

## License

MIT License - see LICENSE file for details

## Acknowledgments

Inspired by the [smolagents](https://github.com/huggingface/smolagents) library from Hugging Face.
