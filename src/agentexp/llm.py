"""
LLM Provider abstraction for agent framework.

This module provides an abstract interface for LLM providers and concrete
implementations for popular services like OpenRouter.
"""

import os
from abc import ABC, abstractmethod
from typing import Any, Optional

import requests


class LLMProvider(ABC):
    """
    Abstract base class for LLM providers.

    This allows the agent to work with any LLM service by implementing
    a simple interface.
    """

    @abstractmethod
    def generate(self, messages: list[dict[str, str]], **kwargs: Any) -> str:
        """
        Generate a response from the LLM.

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            **kwargs: Provider-specific generation parameters

        Returns:
            The generated text response
        """
        pass


class OpenRouterProvider(LLMProvider):
    """
    OpenRouter LLM provider implementation.

    OpenRouter provides access to many LLMs through a single API.
    Default model is "google/gemini-2.0-flash-exp:free" which is free to use.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "google/gemini-2.0-flash-exp:free",
        base_url: str = "https://openrouter.ai/api/v1",
    ):
        """
        Initialize OpenRouter provider.

        Args:
            api_key: OpenRouter API key. If None, reads from OPENROUTER_API_KEY env var
            model: Model identifier (default: free Google Gemini Flash model)
            base_url: OpenRouter API base URL
        """
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError(
                "OpenRouter API key must be provided or set in OPENROUTER_API_KEY "
                "environment variable. Get a free key at https://openrouter.ai/"
            )
        self.model = model
        self.base_url = base_url

    def generate(
        self,
        messages: list[dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs: Any,
    ) -> str:
        """
        Generate a response using OpenRouter.

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            temperature: Sampling temperature (0.0 to 2.0)
            max_tokens: Maximum tokens to generate
            **kwargs: Additional OpenRouter parameters

        Returns:
            The generated text response

        Raises:
            requests.HTTPError: If the API request fails
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            **kwargs,
        }

        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=data,
            timeout=30,
        )
        response.raise_for_status()

        result = response.json()
        return result["choices"][0]["message"]["content"]
