"""Tests for calculator tools."""

import math

import pytest

from agentexp.calculator_tools import (
    CalculatorTool,
    MathFunctionTool,
    VerifyCalculationTool,
)


class TestCalculatorTool:
    """Test the CalculatorTool class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.tool = CalculatorTool()

    def test_name(self):
        """Test tool name."""
        assert self.tool.name == "calculator"

    def test_description(self):
        """Test tool has a description."""
        assert len(self.tool.description) > 0
        assert "expression" in self.tool.description.lower()

    def test_basic_operations(self):
        """Test basic arithmetic operations."""
        assert self.tool.execute("2 + 2") == 4
        assert self.tool.execute("10 - 3") == 7
        assert self.tool.execute("5 * 4") == 20
        assert self.tool.execute("15 / 3") == 5
        assert self.tool.execute("2 ** 3") == 8

    def test_complex_expression(self):
        """Test complex mathematical expressions."""
        assert self.tool.execute("(2 + 3) * 4") == 20
        assert self.tool.execute("2 + 3 * 4") == 14
        assert self.tool.execute("(10 - 2) / 4") == 2

    def test_invalid_expression(self):
        """Test that invalid expressions raise ValueError."""
        with pytest.raises(ValueError):
            self.tool.execute("import os")

        with pytest.raises(ValueError):
            self.tool.execute("2 +")


class TestMathFunctionTool:
    """Test the MathFunctionTool class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.tool = MathFunctionTool()

    def test_name(self):
        """Test tool name."""
        assert self.tool.name == "math_function"

    def test_description(self):
        """Test tool has a description."""
        assert len(self.tool.description) > 0
        assert "function" in self.tool.description.lower()

    def test_sqrt(self):
        """Test square root function."""
        assert self.tool.execute("sqrt", 16) == 4.0
        assert self.tool.execute("sqrt", 25) == 5.0

    def test_trigonometric(self):
        """Test trigonometric functions."""
        assert abs(self.tool.execute("sin", 0) - 0.0) < 1e-9
        assert abs(self.tool.execute("cos", 0) - 1.0) < 1e-9
        assert abs(self.tool.execute("tan", 0) - 0.0) < 1e-9

    def test_logarithmic(self):
        """Test logarithmic functions."""
        assert abs(self.tool.execute("log", math.e) - 1.0) < 1e-9
        assert abs(self.tool.execute("log10", 100) - 2.0) < 1e-9

    def test_floor_ceil(self):
        """Test floor and ceil functions."""
        assert self.tool.execute("floor", 3.7) == 3
        assert self.tool.execute("ceil", 3.2) == 4

    def test_factorial(self):
        """Test factorial function."""
        assert self.tool.execute("factorial", 5) == 120
        assert self.tool.execute("factorial", 0) == 1

    def test_unknown_function(self):
        """Test that unknown functions raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            self.tool.execute("unknown_func", 5)
        assert "Unknown function" in str(exc_info.value)

    def test_invalid_input(self):
        """Test that invalid inputs raise ValueError."""
        with pytest.raises(ValueError):
            self.tool.execute("sqrt", -1)


class TestVerifyCalculationTool:
    """Test the VerifyCalculationTool class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.tool = VerifyCalculationTool()

    def test_name(self):
        """Test tool name."""
        assert self.tool.name == "verify_calculation"

    def test_description(self):
        """Test tool has a description."""
        assert len(self.tool.description) > 0

    def test_correct_calculation(self):
        """Test verification of correct calculations."""
        assert self.tool.execute("2 + 2", 4) is True
        assert self.tool.execute("5 * 3", 15) is True
        assert self.tool.execute("10 / 2", 5) is True

    def test_incorrect_calculation(self):
        """Test verification of incorrect calculations."""
        assert self.tool.execute("2 + 2", 5) is False
        assert self.tool.execute("5 * 3", 14) is False

    def test_floating_point(self):
        """Test verification with floating point numbers."""
        assert self.tool.execute("1 / 3 * 3", 1.0) is True
        assert self.tool.execute("0.1 + 0.2", 0.3) is True

    def test_invalid_expression(self):
        """Test that invalid expressions return False."""
        assert self.tool.execute("invalid", 0) is False
