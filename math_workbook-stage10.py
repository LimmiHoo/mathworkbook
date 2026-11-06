# === Stage 10: Поиск по нескольким словам ===
# Project: MathWorkbook
def find_problem_by_words(problem, keywords, exclude=None):
    """Return the first problem matching all keywords, unless excluded.

    Each keyword must appear in the problem statement. A keyword prefixed
    with a dash excludes problems containing that word. Matching is case
    insensitive and word based.
    """
    exclude = exclude or []
    statement = problem.get("statement", "")
    words = set(token.lower() for token in statement.split())

    if any(word not in words for word in keywords):
        return None

    if any(word in words for word in exclude):
        return None

    return problem


def select_problems(problems, keywords, exclude=None):
    """Return a list of problems matching keywords, honouring exclusions."""
    exclude = exclude or []
    return [
        problem
        for problem in problems
        if find_problem_by_words(problem, keywords, exclude) is not None
    ]


def matches_keywords(statement, keywords, exclude=None):
    """Case-insensitive, word-based check for keywords against a statement."""
    exclude = exclude or []
    words = set(token.lower() for token in statement.split())
    if any(word not in words for word in keywords):
        return False
    if any(word in words for word in exclude):
        return False
    return True


if __name__ == "__main__":
    sample = [
        {
            "id": "prob-001",
            "statement": "Solve the quadratic equation to find the roots.",
            "topic": "Algebra",
            "difficulty": "medium",
            "status": "active",
        },
        {
            "id": "prob-002",
            "statement": "Compute the derivative of the given function.",
            "topic": "Calculus",
            "difficulty": "hard",
            "status": "active",
        },
        {
            "id": "prob-003",
            "statement": "Find the roots of the polynomial equation.",
            "topic": "Algebra",
            "difficulty": "easy",
            "status": "archived",
        },
    ]

    print(select_problems(sample, ["equation", "-roots"]))
    print(select_problems(sample, ["roots"]))
    print(select_problems(sample, ["derivative", "-function"]))
