"""
Demo module showcasing modern Python tooling.

This module demonstrates features that are caught/improved by:
- Ruff (linting and formatting)
- Pyright (type checking)
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    """User model demonstrating proper type annotations."""

    id: int
    username: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True


def greet_user(user: User) -> str:
    """
    Generate a greeting message for a user.

    Args:
        user: The user to greet

    Returns:
        A personalized greeting message
    """
    status = "active" if user.is_active else "inactive"
    return f"Hello, {user.username}! Your account is {status}."


def calculate_days_since_creation(user: User) -> int:
    """
    Calculate the number of days since the user was created.

    Args:
        user: The user to check

    Returns:
        Number of days since account creation
    """
    now = datetime.now()
    delta = now - user.created_at
    return delta.days


def process_users(users: list[User]) -> dict[str, int]:
    """
    Process a list of users and return statistics.

    Args:
        users: List of users to process

    Returns:
        Dictionary with user statistics
    """
    active_count = sum(1 for user in users if user.is_active)
    total_count = len(users)

    return {
        "total": total_count,
        "active": active_count,
        "inactive": total_count - active_count,
    }


def main() -> None:
    """Main function demonstrating the tooling."""
    # Create sample users
    users = [
        User(id=1, username="alice", email="alice@example.com"),
        User(id=2, username="bob", email="bob@example.com", is_active=False),
        User(
            id=3,
            username="charlie",
            email="charlie@example.com",
            created_at=datetime(2024, 1, 1),
        ),
    ]

    # Greet each user
    for user in users:
        print(greet_user(user))
        days = calculate_days_since_creation(user)
        print(f"  Account age: {days} days")

    # Print statistics
    print("\nUser Statistics:")
    stats = process_users(users)
    for key, value in stats.items():
        print(f"  {key.capitalize()}: {value}")


if __name__ == "__main__":
    main()

