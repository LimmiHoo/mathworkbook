# === Stage 33: Рекомендации ===
# Project: MathWorkbook
"""MathWorkbook stage 33: next action recommendation.

Pure, self-contained module. No external dependencies.
"""

from collections import Counter


def recommend_next_action(tasks, attempts):
    """Return a small list describing the best next step.

    Parameters
    ----------
    tasks : list of dict
        Each task has 'topic', 'difficulty', and 'status' keys.
        'status' is one of 'pending', 'in_progress', 'solved', 'errored'.
    attempts : list of dict
        Each attempt has 'task_id', 'topic', and 'solved' keys.
        'solved' is a boolean.

    Returns
    -------
    list of dict
        Ordered recommendations, each with 'kind', 'topic', 'difficulty',
        and 'reason' keys.
    """

    pending = [t for t in tasks if t.get("status") == "pending"]
    errored = [t for t in tasks if t.get("status") == "errored"]
    in_progress = [t for t in tasks if t.get("status") == "in_progress"]
    solved = [t for t in tasks if t.get("status") == "solved"]

    solved_by_topic = Counter(t["topic"] for t in solved)
    attempts_by_topic = Counter(
        a["topic"] for a in attempts if a.get("solved", False)
    )
    failed_by_topic = Counter(
        a["topic"] for a in attempts if not a.get("solved", False)
    )

    recommendations = []

    if pending:
        hardest = max(pending, key=lambda t: t.get("difficulty", 0))
        recommendations.append(
            {
                "kind": "start",
                "topic": hardest["topic"],
                "difficulty": hardest.get("difficulty", 0),
                "reason": (
                    "Begin with a pending task; pick the hardest one to "
                    "keep progress challenging."
                ),
            }
        )

    if errored:
        most_failed = failed_by_topic.most_common(1)[0]
        recommendations.append(
            {
                "kind": "review",
                "topic": most_failed[0],
                "reason": (
                    "Review the topic with the most failed attempts before "
                    "attempting new problems."
                ),
            }
        )

    mastered = solved_by_topic.most_common(5)
    for topic, count in mastered:
        recommendations.append(
            {
                "kind": "practice",
                "topic": topic,
                "reason": (
                    "Reinforce a well-mastered topic with additional practice."
                ),
            }
        )

    return recommendations
