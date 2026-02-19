"""
Python Tooling Example - Demo package for modern Python tooling tech talk.

This package demonstrates:
- uv for fast package management
- Ruff for linting and formatting
- Pyright for type checking
- pre-commit for automated quality checks
"""

__version__ = "0.1.0"

from python_tooling_example.main import User, greet_user, process_users

__all__ = ["User", "greet_user", "process_users", "__version__"]
