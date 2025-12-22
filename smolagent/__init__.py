"""
Smolagent - An educational LLM-agnostic agent framework.

This package provides a simple, educational framework for building AI agents
that can use tools to accomplish tasks. The framework is designed to be:

- LLM-agnostic: Works with any LLM provider
- Educational: Clean, well-documented code for learning
- Extensible: Easy to add new tools and capabilities
"""

__version__ = "0.1.0"

from smolagent.agent import Agent
from smolagent.llm import LLMProvider, OpenRouterProvider
from smolagent.tools import Tool

__all__ = ["Agent", "LLMProvider", "OpenRouterProvider", "Tool"]
