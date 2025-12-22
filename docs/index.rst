Smolagent Documentation
=======================

Welcome to Smolagent's documentation! Smolagent is an educational,
LLM-agnostic agent framework that demonstrates how to build AI agents
with tool use capabilities.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   user_guide
   api_reference
   auto_examples/index

Key Features
------------

- **LLM-Agnostic**: Works with any LLM provider
- **Educational**: Clean, well-documented code for learning
- **Extensible**: Easy to add new tools and capabilities
- **Production-Ready**: Includes linting, testing, and documentation

Quick Start
-----------

Install the package:

.. code-block:: bash

   pip install -e .

Set up your OpenRouter API key (get a free key at https://openrouter.ai/):

.. code-block:: bash

   export OPENROUTER_API_KEY="your-api-key"

Create a simple calculator agent:

.. code-block:: python

   from smolagent import Agent, OpenRouterProvider
   from smolagent.calculator_tools import CalculatorTool

   # Initialize LLM provider and tools
   llm = OpenRouterProvider()
   tools = [CalculatorTool()]

   # Create and run agent
   agent = Agent(llm_provider=llm, tools=tools)
   result = agent.run("What is 25 * 4?")
   print(result)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
