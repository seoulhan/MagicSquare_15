"""User entity for the MagicSquare domain."""

from __future__ import annotations

from dataclasses import dataclass


MIN_USERNAME_LENGTH = 1


@dataclass(frozen=True)
class User:
    """Represents a user of the MagicSquare program.

    Attributes:
        user_id: Unique identifier for the user.
        username: Display name used by the user.
    """

    user_id: int
    username: str

    def __post_init__(self) -> None:
        """Validate user invariants after initialization.

        Raises:
            ValueError: If the user id or username is invalid.
        """
        if self.user_id <= 0:
            raise ValueError("user_id must be a positive integer.")

        normalized_username = self.username.strip()
        if len(normalized_username) < MIN_USERNAME_LENGTH:
            raise ValueError("username must not be empty.")

        object.__setattr__(self, "username", normalized_username)

    def can_create_magic_square(self) -> bool:
        """Return whether the user can create a magic square.

        Returns:
            True when the user satisfies the entity invariants.
        """
        return True
