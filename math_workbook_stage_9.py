# === Stage 9: Текстовый поиск ===
# Project: MathWorkbook
import re


def build_case_query(text, highlight=False):
    """Build a case-insensitive search query for a task text field.

    Returns a compiled regular expression that matches the search term
    anywhere inside the given text, ignoring case. When ``highlight`` is
    enabled the pattern additionally captures the matched span so the
    calling layer can wrap it with highlight markup.

    Args:
        text: The task description to search within. May be None.
        highlight: If True, the returned pattern captures the match.

    Returns:
        A compiled regex object, or None when there is nothing to search.
    """
    if text is None:
        return None

    cleaned = re.sub(r"\s+", " ", text).strip()
    if not cleaned:
        return None

    pattern = re.escape(cleaned)
    flags = re.IGNORECASE
    if highlight:
        pattern = r"(?P<match>" + pattern + ")"
    return re.compile(pattern, flags)


def highlight_line(line, query):
    """Return a line with every occurrence of the query highlighted.

    The ``query`` argument must be a compiled regular expression. Matches
    are wrapped in SPAN tags so a terminal or web layer can render them
    with emphasis. Non-matching text is passed through unchanged.

    Args:
        line: The original string to search and highlight.
        query: A compiled regex produced by ``build_case_query``.

    Returns:
        The highlighted string, or the original line when the query is
        None or has no matches.
    """
    if query is None:
        return line

    def replacement(match):
        return f"<mark>{match.group('match')}</mark>"

    return re.sub(query, replacement, line)


if __name__ == "__main__":
    demo_tasks = [
        "Solve quadratic equation ax^2 + bx + c = 0",
        "Find the derivative of sin(x)",
        "Integrate by parts",
    ]

    search = build_case_query("QUADRATIC", highlight=True)
    if search is None:
        print("No query available")
    else:
        for task in demo_tasks:
            print(task)
            print("  -> " + highlight_line(task, search))
