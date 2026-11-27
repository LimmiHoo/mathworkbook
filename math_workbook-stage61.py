# === Stage 61: Роли доступа ===
# Project: MathWorkbook
# Stage 61: simple roles (reader, editor) and permission checks before mutating data.
# Self-contained module using only the standard library.

from enum import Enum


class Role(Enum):
    """Access level granted to a user."""

    reader = "reader"
    editor = "editor"


class DataMutationError(Exception):
    """Raised when a user lacks the permission to change data."""


def require_write_permission(role: Role) -> bool:
    """Return True only for roles allowed to mutate data."""
    return role is Role.editor


def check_write_permission(role: Role) -> None:
    """Raise DataMutationError if the role cannot edit data."""
    if not require_write_permission(role):
        raise DataMutationError("permission denied: this role cannot edit data")


def can_read(role: Role) -> bool:
    """Both readers and editors can read data."""
    return role in (Role.reader, Role.editor)


def guard_edit(func, role: Role):
    """Decorator that enforces write permission before running func."""
    def wrapper(*args, **kwargs):
        check_write_permission(role)
        return func(*args, **kwargs)
    return wrapper


def role_from_string(value: str) -> Role:
    """Convert a string token to a Role, defaulting to reader."""
    for candidate in Role:
        if candidate.value == value:
            return candidate
    return Role.reader
