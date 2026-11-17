# === Stage 32: Что требует внимания ===
# Project: MathWorkbook
from collections import defaultdict


def summarize_attention(records):
    """Build a summary of records that require attention.

    A record requires attention if it is overdue, stuck, or incomplete.
    Each input record is a mapping with the fields:
      condition, topic, difficulty, status.
    The function returns a dict with three keys: overdue, stuck, incomplete.
    """
    overdue = []
    stuck = []
    incomplete = []

    for record in records:
        status = record.get("status")
        attempts = record.get("attempts", 0)
        max_attempts = record.get("max_attempts", 1)

        if status is None:
            incomplete.append(record)
        elif status == "stuck":
            stuck.append(record)
        elif status == "overdue":
            overdue.append(record)

    return {
        "overdue": overdue,
        "stuck": stuck,
        "incomplete": incomplete,
    }


def count_attempts(records):
    """Return the total number of attempts across all records."""
    total = 0
    for record in records:
        total += record.get("attempts", 0)
    return total


def find_stuck(records, threshold):
    """Return records whose attempts are within threshold of the maximum.

    A record is considered stuck when it has been attempted many times
    without success, meaning it is close to exhausting its attempts.
    """
    stuck = []
    for record in records:
        attempts = record.get("attempts", 0)
        max_attempts = record.get("max_attempts", 1)
        if max_attempts > 0:
            ratio = attempts / max_attempts
            if ratio >= threshold:
                stuck.append(record)
    return stuck


def group_by_topic(records):
    """Group records by their topic and return a dict of topic to records."""
    grouped = defaultdict(list)
    for record in records:
        topic = record.get("topic", "unknown")
        grouped[topic].append(record)
    return dict(grouped)


def summarize_attention_counts(records):
    """Summarize how many records require attention grouped by category.

    Returns a dict with the counts for overdue, stuck, and incomplete.
    """
    summary = summarize_attention(records)
    return {
        "overdue": len(summary["overdue"]),
        "stuck": len(summary["stuck"]),
        "incomplete": len(summary["incomplete"]),
    }


def format_attention_summary(counts):
    """Format a counts summary into a readable string."""
    lines = []
    lines.append("Attention Summary")
    lines.append("=================")
    lines.append(f"Overdue: {counts.get('overdue', 0)}")
    lines.append(f"Stuck: {counts.get('stuck', 0)}")
    lines.append(f"Incomplete: {counts.get('incomplete', 0)}")
    return "\n".join(lines)


def analyze_workbook(records):
    """Analyze a set of records and return a comprehensive summary.

    Combines attention summary with topic grouping and attempt counts.
    """
    attention = summarize_attention_counts(records)
    grouped = group_by_topic(records)
    total_attempts = count_attempts(records)

    return {
        "attention": attention,
        "topics": grouped,
        "total_attempts": total_attempts,
    }
