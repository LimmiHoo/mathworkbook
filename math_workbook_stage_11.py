# === Stage 11: Теги ===
# Project: MathWorkbook
TASK_TAG = "tag"


def add_tag(task, tag):
    if not isinstance(tag, str) or not tag.strip():
        raise ValueError("tag must be a non-empty string")
    if tag not in task["tags"]:
        task["tags"].append(tag)
    return task


def remove_tag(task, tag):
    if tag in task["tags"]:
        task["tags"].remove(tag)
    return task


def contains_tag(task, tag):
    return tag in task["tags"]


def find_by_tag(tasks, tag):
    result = []
    for task in tasks:
        if contains_tag(task, tag):
            result.append(task)
    return result


def list_tags(task):
    return list(task["tags"])
