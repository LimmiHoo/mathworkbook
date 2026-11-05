# === Stage 6: Генерация идентификаторов ===
# Project: MathWorkbook
PROJECT_PREFIX = "mathwb"


def generate_unique_id(prefix: str, count: int = 1) -> list[str]:
    """Generate unique identifiers with the given prefix.

    Returns a list of unique identifiers. Each identifier is formed by
    combining the prefix with an incrementing counter.
    """
    used: set[str] = set()
    generated: list[str] = []
    counter = 0
    while len(generated) < count:
        counter += 1
        candidate = f"{prefix}-{counter}"
        if candidate not in used:
            used.add(candidate)
            generated.append(candidate)
    return generated


def has_collision(ids: list[str]) -> bool:
    """Check if there are duplicate identifiers in the given list."""
    return len(ids) != len(set(ids))


def get_unique_id(prefix: str, existing: set[str], counter: int = 1) -> str:
    """Get a unique identifier that does not exist in the given set.

    Keeps incrementing the counter until a non-colliding identifier is found.
    """
    while True:
        candidate = f"{prefix}-{counter}"
        counter += 1
        if candidate not in existing:
            return candidate
