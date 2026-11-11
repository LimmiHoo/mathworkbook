# === Stage 16: Массовое обновление ===
# Project: MathWorkbook
def build_condition_filter(query):
    tokens = query.replace(",", " ").split()
    conditions = {}
    for token in tokens:
        if "=" in token:
            key, value = token.split("=", 1)
            conditions[key.strip()] = value.strip()
    return conditions


def normalize_field(field_name):
    mapping = {
        "topic": "theme",
        "subject": "theme",
        "difficulty": "difficulty",
        "level": "difficulty",
        "status": "status",
    }
    return mapping.get(field_name, field_name.strip())


def collect_changes(existing_task, new_condition):
    changes = []
    field_map = {
        "condition": "statement",
        "text": "statement",
        "theme": "theme",
        "difficulty": "difficulty",
        "status": "status",
    }
    for raw_key, raw_value in new_condition.items():
        if raw_key not in field_map:
            continue
        target_key = field_map[raw_key]
        old_value = getattr(existing_task, target_key, None)
        new_value = raw_value
        if old_value != new_value:
            changes.append((target_key, old_value, new_value))
    return changes


def preview_updates(tasks, condition):
    preview = []
    for task in tasks:
        changes = collect_changes(task, condition)
        if changes:
            preview.append({
                "id": task.get("id"),
                "theme": task.get("theme"),
                "changes": changes,
            })
    return preview


def apply_updates(tasks, condition):
    normalized = {}
    for field_name, value in condition.items():
        normalized[normalize_field(field_name)] = value
    updated = []
    for task in tasks:
        if task.get("condition") == condition:
            task["statement"] = normalized.get("statement", task.get("statement"))
            task["theme"] = normalized.get("theme", task.get("theme"))
            task["difficulty"] = normalized.get("difficulty", task.get("difficulty"))
            task["status"] = normalized.get("status", task.get("status"))
            updated.append(task)
    return updated
