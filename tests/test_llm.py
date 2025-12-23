"""Tests for LLM providers."""

import os
from unittest.mock import Mock, patch

import pytest

from agentexp.llm import OpenRouterProvider


class TestOpenRouterProvider:
    """Test the OpenRouterProvider class."""

    def test_initialization_with_api_key(self):
        """Test provider can be initialized with API key."""
        provider = OpenRouterProvider(api_key="test-key")
        assert provider.api_key == "test-key"
        assert provider.model == "google/gemini-2.0-flash-exp:free"

    def test_initialization_with_env_var(self):
        """Test provider can be initialized from environment variable."""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "env-key"}):
            provider = OpenRouterProvider()
            assert provider.api_key == "env-key"

    def test_initialization_without_api_key(self):
        """Test provider raises error without API key."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError) as exc_info:
                OpenRouterProvider()
            assert "API key" in str(exc_info.value)

    def test_custom_model(self):
        """Test provider can be initialized with custom model."""
        provider = OpenRouterProvider(api_key="test-key", model="custom-model")
        assert provider.model == "custom-model"

    @patch("agentexp.llm.requests.post")
    def test_generate_success(self, mock_post):
        """Test successful generation."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Generated response"}}]
        }
        mock_post.return_value = mock_response

        provider = OpenRouterProvider(api_key="test-key")
        messages = [{"role": "user", "content": "Hello"}]
        result = provider.generate(messages)

        assert result == "Generated response"
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        assert call_args[1]["json"]["model"] == "google/gemini-2.0-flash-exp:free"
        assert call_args[1]["json"]["messages"] == messages

    @patch("agentexp.llm.requests.post")
    def test_generate_with_params(self, mock_post):
        """Test generation with custom parameters."""
        mock_response = Mock()
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Response"}}]
        }
        mock_post.return_value = mock_response

        provider = OpenRouterProvider(api_key="test-key")
        messages = [{"role": "user", "content": "Hello"}]
        provider.generate(messages, temperature=0.5, max_tokens=500)

        call_args = mock_post.call_args
        assert call_args[1]["json"]["temperature"] == 0.5
        assert call_args[1]["json"]["max_tokens"] == 500

    @patch("agentexp.llm.requests.post")
    def test_generate_http_error(self, mock_post):
        """Test generation handles HTTP errors."""
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("HTTP Error")
        mock_post.return_value = mock_response

        provider = OpenRouterProvider(api_key="test-key")
        messages = [{"role": "user", "content": "Hello"}]

        with pytest.raises(Exception) as exc_info:
            provider.generate(messages)
        assert "HTTP Error" in str(exc_info.value)
