# === Stage 50: Разбор ошибок ===
# Project: MathWorkbook
from collections import defaultdict, Counter


def group_errors_by_topic(errors):
    grouped = defaultdict(list)
    for error in errors:
        topic = error.get("topic")
        grouped[topic].append(error)
    return dict(grouped)


def summarize_weaknesses(grouped):
    summary = {}
    for topic, topic_errors in grouped.items():
        if not topic_errors:
            continue
        counts = Counter()
        for error in topic_errors:
            counts[error.get("category", "unknown")] += 1
        summary[topic] = dict(counts.most_common())
    return summary


def find_weak_topics(summary, threshold=None):
    weak_topics = []
    for topic, category_counts in summary.items():
        total_attempts = sum(category_counts.values())
        if threshold is None:
            weak_topics.append((topic, category_counts))
        else:
            if total_attempts >= threshold:
                weak_topics.append((topic, category_counts))
    weak_topics.sort(key=lambda item: sum(item[1].values()), reverse=True)
    return weak_topics


def display_weakness_report(summary, weak_topics):
    print("MathWorkbook - Weakness Report")
    print("=" * 40)
    if not weak_topics:
        print("No weak topics detected.")
        return
    for topic, category_counts in weak_topics:
        print(f"\nTopic: {topic}")
        for category, count in category_counts.items():
            print(f"  {category}: {count} error(s)")


def main():
    sample_errors = [
        {"id": 1, "topic": "Algebra", "category": "Equation solving", "severity": "high"},
        {"id": 2, "topic": "Algebra", "category": "Factoring", "severity": "medium"},
        {"id": 3, "topic": "Algebra", "category": "Equation solving", "severity": "low"},
        {"id": 4, "topic": "Geometry", "category": "Area calculation", "severity": "high"},
        {"id": 5, "topic": "Geometry", "category": "Angle properties", "severity": "medium"},
        {"id": 6, "topic": "Geometry", "category": "Area calculation", "severity": "low"},
        {"id": 7, "topic": "Trigonometry", "category": "Identity application", "severity": "high"},
        {"id": 8, "topic": "Algebra", "category": "Inequalities", "severity": "medium"},
    ]

    grouped_errors = group_errors_by_topic(sample_errors)
    summary = summarize_weaknesses(grouped_errors)
    weak_topics = find_weak_topics(summary)
    display_weakness_report(summary, weak_topics)


if __name__ == "__main__":
    main()
