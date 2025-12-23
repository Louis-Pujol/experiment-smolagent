"""
Base Tool class for creating agent tools.

Tools are the building blocks that allow agents to interact with the world.
Each tool represents a specific capability (e.g., math operations, web search).
"""

from abc import ABC, abstractmethod
from typing import Any


class Tool(ABC):
    """
    Abstract base class for all agent tools.

    Tools must implement a name, description, and execute method.
    The description is used by the LLM to understand when to use the tool.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the tool."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Return a description of what the tool does and when to use it."""
        pass

    @abstractmethod
    def execute(self, **kwargs: Any) -> Any:
        """
        Execute the tool with the given arguments.

        Args:
            **kwargs: Tool-specific arguments

        Returns:
            The result of executing the tool
        """
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
