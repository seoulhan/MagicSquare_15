"""Tests for the User entity."""

import pytest

from entity.user import User


def test_user_trims_username() -> None:
    """Verify that usernames are normalized when a user is created."""
    # Arrange
    username = "  alice  "

    # Act
    user = User(user_id=1, username=username)

    # Assert
    assert user.username == "alice"


def test_user_rejects_non_positive_user_id() -> None:
    """Verify that a user id must be positive."""
    # Arrange
    user_id = 0

    # Act / Assert
    with pytest.raises(ValueError, match="user_id must be a positive integer"):
        User(user_id=user_id, username="alice")


def test_user_rejects_empty_username() -> None:
    """Verify that a username must contain visible characters."""
    # Arrange
    username = "   "

    # Act / Assert
    with pytest.raises(ValueError, match="username must not be empty"):
        User(user_id=1, username=username)


def test_user_can_create_magic_square() -> None:
    """Verify that a valid user can create a magic square."""
    # Arrange
    user = User(user_id=1, username="alice")

    # Act
    can_create = user.can_create_magic_square()

    # Assert
    assert can_create is True
