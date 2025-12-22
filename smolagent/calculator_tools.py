"""
Calculator tools for mathematical operations.

These tools provide access to Python's math functions and allow
the agent to perform and verify computations.
"""

import math
from typing import Union

from smolagent.tools import Tool


class CalculatorTool(Tool):
    """
    A tool for performing basic arithmetic calculations.

    This tool can evaluate mathematical expressions and return the result.
    It uses Python's eval with a restricted namespace for safety.
    """

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return (
            "Evaluates a mathematical expression and returns the result. "
            "Supports basic operations (+, -, *, /, **), parentheses, and numbers. "
            "Example: calculator(expression='2 + 2 * 3')"
        )

    def execute(self, expression: str) -> Union[float, int]:
        """
        Evaluate a mathematical expression.

        Args:
            expression: The mathematical expression to evaluate

        Returns:
            The result of the calculation

        Raises:
            ValueError: If the expression is invalid or unsafe
        """
        # Create a safe namespace with only allowed operations
        safe_namespace = {
            "__builtins__": {},
            "abs": abs,
            "round": round,
            "min": min,
            "max": max,
            "sum": sum,
            "pow": pow,
        }

        try:
            result = eval(expression, safe_namespace, {})
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}") from e


class MathFunctionTool(Tool):
    """
    A tool for advanced mathematical functions.

    Provides access to common math functions like sin, cos, sqrt, log, etc.
    from Python's math module.
    """

    @property
    def name(self) -> str:
        return "math_function"

    @property
    def description(self) -> str:
        return (
            "Applies a mathematical function to a number. "
            "Available functions: sqrt, sin, cos, tan, log, log10, exp, "
            "floor, ceil, factorial, degrees, radians. "
            "Example: math_function(function='sqrt', value=16)"
        )

    def execute(self, function: str, value: float) -> float:
        """
        Apply a math function to a value.

        Args:
            function: Name of the math function to apply
            value: The input value

        Returns:
            The result of applying the function

        Raises:
            ValueError: If the function is unknown or invalid
        """
        # Map of allowed functions
        allowed_functions = {
            "sqrt": math.sqrt,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "log10": math.log10,
            "exp": math.exp,
            "floor": math.floor,
            "ceil": math.ceil,
            "factorial": math.factorial,
            "degrees": math.degrees,
            "radians": math.radians,
            "abs": abs,
        }

        if function not in allowed_functions:
            available = ", ".join(allowed_functions.keys())
            raise ValueError(f"Unknown function: {function}. Available: {available}")

        try:
            func = allowed_functions[function]
            result = func(value)
            return result
        except Exception as e:
            raise ValueError(f"Error applying {function} to {value}: {str(e)}") from e


class VerifyCalculationTool(Tool):
    """
    A tool for verifying the result of a calculation.

    This tool checks if a claimed result matches the actual result
    of evaluating an expression.
    """

    @property
    def name(self) -> str:
        return "verify_calculation"

    @property
    def description(self) -> str:
        return (
            "Verifies if a calculation result is correct. "
            "Takes an expression and an expected result, returns True if correct. "
            "Example: verify_calculation(expression='2 + 2', expected=4)"
        )

    def execute(self, expression: str, expected: Union[float, int]) -> bool:
        """
        Verify if a calculation is correct.

        Args:
            expression: The mathematical expression
            expected: The expected result

        Returns:
            True if the calculation is correct, False otherwise
        """
        calculator = CalculatorTool()
        try:
            actual = calculator.execute(expression)
            # Use approximate equality for floating point
            if isinstance(actual, float) or isinstance(expected, float):
                return abs(actual - expected) < 1e-9
            return actual == expected
        except Exception:
            return False
