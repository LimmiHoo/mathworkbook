# === Stage 54: Подсказки команд ===
# Project: MathWorkbook
from difflib import SequenceMatcher

HINT_THRESHOLD = 0.6


def find_typo_hints(query: str, known_commands: list) -> list:
    """Return a list of suggested commands for a misspelled query.

    The query is compared against each known command using a ratio
    derived from difflib.SequenceMatcher. Suggestions whose ratio meets
    or exceeds HINT_THRESHOLD are returned, sorted by descending ratio.

    Args:
        query: The user-supplied command name, possibly misspelled.
        known_commands: The list of valid command names to compare against.

    Returns:
        A list of (command, ratio) tuples, best match first. Empty if
        no suggestion reaches the threshold.
    """
    query = query.strip().lower()
    if not query:
        return []

    scored = []
    for command in known_commands:
        normalized = command.strip().lower()
        if normalized == query:
            return [(command, 1.0)]

        ratio = SequenceMatcher(None, query, normalized).ratio()
        if ratio >= HINT_THRESHOLD:
            scored.append((command, ratio))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored


def format_typo_hint(query: str, suggestions: list) -> str:
    """Build a human-readable hint string from suggestions.

    Args:
        query: The original (possibly misspelled) command name.
        suggestions: List of (command, ratio) tuples.

    Returns:
        A hint message. If suggestions is empty, returns a message
        telling the user to check the spelling.
    """
    if not suggestions:
        return "No matching command found. Please check your spelling."

    names = ", ".join(command for command, _ in suggestions)
    return f"Did you mean: {names}?"
