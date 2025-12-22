# User Guide

## Core Concepts

### Agent

The `Agent` is the main orchestrator that uses an LLM to decide which tools
to use and how to accomplish tasks. It follows a reasoning loop:

1. Receive a task
2. Think about what to do
3. Use a tool (if needed)
4. Observe the result
5. Repeat until task is complete

### Tools

Tools are capabilities that the agent can use. Each tool has:

- A **name**: How the agent identifies the tool
- A **description**: Helps the LLM understand when to use it
- An **execute** method: Performs the actual work

### LLM Provider

The LLM Provider is an abstraction that allows the agent to work with
any LLM service. It provides a simple interface for generating text
responses from a list of messages.

## Using Different LLM Providers

### OpenRouter (Default)

OpenRouter provides access to multiple LLMs through a single API:

```python
from smolagent import OpenRouterProvider

# Use default free model
llm = OpenRouterProvider(api_key="your-key")

# Or specify a different model
llm = OpenRouterProvider(
    api_key="your-key",
    model="anthropic/claude-3-haiku"
)
```

### Custom Provider

You can create your own provider by inheriting from `LLMProvider`:

```python
from smolagent import LLMProvider

class CustomProvider(LLMProvider):
    def generate(self, messages, **kwargs):
        # Your implementation here
        pass
```

## Creating Custom Tools

Creating custom tools is straightforward:

```python
from smolagent import Tool

class MyTool(Tool):
    @property
    def name(self):
        return "my_tool"

    @property
    def description(self):
        return "A clear description of what this tool does"

    def execute(self, **kwargs):
        # Your tool logic here
        return result
```

### Tool Best Practices

1. **Clear descriptions**: Include parameter names and examples
2. **Error handling**: Handle errors gracefully
3. **Type hints**: Use type hints for better code quality
4. **Documentation**: Add docstrings for educational purposes

## Agent Configuration

### Max Iterations

Control how many reasoning steps the agent can take:

```python
agent = Agent(llm_provider, tools, max_iterations=10)
```

### Verbose Mode

Enable verbose mode to see the agent's reasoning process:

```python
result = agent.run("Your task here", verbose=True)
```

## Calculator Tools

The package includes three calculator tools:

### CalculatorTool

Evaluates basic mathematical expressions:

```python
from smolagent.calculator_tools import CalculatorTool

tool = CalculatorTool()
result = tool.execute(expression="2 + 2 * 3")  # Returns 8
```

### MathFunctionTool

Applies mathematical functions like sqrt, sin, log, etc.:

```python
from smolagent.calculator_tools import MathFunctionTool

tool = MathFunctionTool()
result = tool.execute(function="sqrt", value=16)  # Returns 4.0
```

### VerifyCalculationTool

Verifies if a calculation is correct:

```python
from smolagent.calculator_tools import VerifyCalculationTool

tool = VerifyCalculationTool()
is_correct = tool.execute(expression="2 + 2", expected=4)  # Returns True
```

## Development Workflow

### Linting with Ruff

Format your code:

```bash
ruff format .
```

Check for issues:

```bash
ruff check .
```

Fix issues automatically:

```bash
ruff check --fix .
```

### Running Tests

Run all tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=smolagent
```

### Pre-commit Hooks

Install pre-commit hooks:

```bash
pre-commit install
```

Run hooks manually:

```bash
pre-commit run --all-files
```

### Building Documentation

Build the documentation:

```bash
cd docs
make html
```

View the documentation:

```bash
open _build/html/index.html
```
