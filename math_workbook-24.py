# === Stage 24: Текстовая гистограмма ===
# Project: MathWorkbook
from collections import Counter


def build_difficulty_histogram(tasks, block="█", gap=1):
    levels = ["easy", "medium", "hard"]
    counts = Counter()
    for task in tasks:
        counts[task.get("difficulty", "easy")] += 1
    total = sum(counts.values())
    if total == 0:
        return ""
    lines = []
    for level in levels:
        bar_len = counts[level] * block
        padding = gap * (counts[level] - 1)
        lines.append(f"{level:8}: {bar_len} {padding} ({counts[level]}/{total})")
    return "\n".join(lines)


def print_difficulty_histogram(tasks):
    print(build_difficulty_histogram(tasks))
