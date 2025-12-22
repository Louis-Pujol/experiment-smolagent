"""Tests for tool base class."""

import pytest

from smolagent.tools import Tool


class TestTool:
    """Test the Tool base class."""

    def test_tool_is_abstract(self):
        """Test that Tool cannot be instantiated directly."""
        with pytest.raises(TypeError):
            Tool()

    def test_concrete_tool_implementation(self):
        """Test that a concrete tool can be implemented."""

        class ConcreteTool(Tool):
            @property
            def name(self):
                return "test_tool"

            @property
            def description(self):
                return "A test tool"

            def execute(self, **kwargs):
                return "executed"

        tool = ConcreteTool()
        assert tool.name == "test_tool"
        assert tool.description == "A test tool"
        assert tool.execute() == "executed"

    def test_tool_repr(self):
        """Test tool string representation."""

        class SimpleTool(Tool):
            @property
            def name(self):
                return "simple"

            @property
            def description(self):
                return "Simple tool"

            def execute(self, **kwargs):
                pass

        tool = SimpleTool()
        assert "SimpleTool" in repr(tool)
        assert "simple" in repr(tool)
