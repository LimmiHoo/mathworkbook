# === Stage 56: Алиасы команд ===
# Project: MathWorkbook
"""Team aliases and user abbreviations for MathWorkbook."""

from typing import Dict, List, Optional


class AliasError(Exception):
    """Raised when an alias or abbreviation cannot be resolved."""


class TeamAlias:
    """Maps a short team tag to a full team name."""

    def __init__(self, tag: str, team: str):
        self.tag = tag
        self.team = team

    def __repr__(self) -> str:
        return f"TeamAlias({self.tag!r} -> {self.team!r})"


class AliasRegistry:
    """Stores and resolves team aliases."""

    def __init__(self) -> None:
        self._aliases: Dict[str, str] = {}

    def register(self, tag: str, team: str) -> None:
        normalized_tag = tag.strip().lower()
        if not normalized_tag:
            raise AliasError("Team alias tag must not be empty")
        self._aliases[normalized_tag] = team

    def resolve(self, tag: str) -> Optional[str]:
        return self._aliases.get(tag.strip().lower())

    def has(self, tag: str) -> bool:
        return tag.strip().lower() in self._aliases

    def list(self) -> List[TeamAlias]:
        return [TeamAlias(tag, team) for tag, team in self._aliases.items()]


class UserAbbreviation:
    """Maps a short abbreviation to a full user name."""

    def __init__(self, short: str, name: str):
        self.short = short
        self.name = name

    def __repr__(self) -> str:
        return f"UserAbbreviation({self.short!r} -> {self.name!r})"


class AbbreviationRegistry:
    """Stores and resolves user abbreviations."""

    def __init__(self) -> None:
        self._abbreviations: Dict[str, str] = {}

    def register(self, short: str, name: str) -> None:
        normalized = short.strip().lower()
        if not normalized:
            raise AliasError("Abbreviation must not be empty")
        self._abbreviations[normalized] = name

    def resolve(self, short: str) -> Optional[str]:
        return self._abbreviations.get(short.strip().lower())

    def has(self, short: str) -> bool:
        return short.strip().lower() in self._abbreviations

    def list(self) -> List[UserAbbreviation]:
        return [UserAbbreviation(short, name) for short, name in self._abbreviations.items()]


def expand_abbreviations(text: str, registry: AbbreviationRegistry) -> str:
    """Replace every recognized abbreviation in text with the full name."""
    if not registry:
        return text
    return registry.resolve(text)
