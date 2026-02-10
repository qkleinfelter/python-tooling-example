"""
Example module showing common code issues that Ruff catches and fixes.

This file demonstrates:
- Import sorting (Ruff/isort)
- Unused imports (Ruff/flake8)
- Type hints (Ty)
- Code formatting (Ruff/Black)
- Common code smells
"""

from typing import Any


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of the two numbers
    """
    return a + b


def format_name(first: str, last: str) -> str:
    """
    Format a person's full name.

    Args:
        first: First name
        last: Last name

    Returns:
        Formatted full name
    """
    return f"{first.capitalize()} {last.capitalize()}"


def safe_divide(a: float, b: float) -> float | None:
    """
    Safely divide two numbers.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        Result of division, or None if division by zero
    """
    if b == 0:
        return None
    return a / b


def process_data(data: list[dict[str, Any]]) -> list[str]:
    """
    Process a list of data dictionaries.

    Args:
        data: List of dictionaries containing data

    Returns:
        List of processed strings
    """
    results = []
    for item in data:
        if "name" in item:
            results.append(str(item["name"]))
    return results


def get_config() -> dict[str, str | int | bool]:
    """
    Get application configuration.

    Returns:
        Configuration dictionary
    """
    return {
        "debug": True,
        "max_connections": 100,
        "timeout": 30,
        "app_name": "Python Tooling Demo",
    }


class Calculator:
    """Simple calculator class demonstrating typed methods."""

    def __init__(self, initial_value: float = 0.0) -> None:
        """
        Initialize calculator.

        Args:
            initial_value: Starting value for calculations
        """
        self.value = initial_value

    def add(self, amount: float) -> "Calculator":
        """
        Add to current value.

        Args:
            amount: Amount to add

        Returns:
            Self for method chaining
        """
        self.value += amount
        return self

    def subtract(self, amount: float) -> "Calculator":
        """
        Subtract from current value.

        Args:
            amount: Amount to subtract

        Returns:
            Self for method chaining
        """
        self.value -= amount
        return self

    def get_result(self) -> float:
        """
        Get current value.

        Returns:
            Current calculator value
        """
        return self.value


if __name__ == "__main__":
    # Example usage
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")

    name = format_name("john", "doe")
    print(f"Formatted name: {name}")

    calc = Calculator(10)
    final = calc.add(5).subtract(3).get_result()
    print(f"Calculator result: {final}")
