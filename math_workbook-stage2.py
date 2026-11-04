# === Stage 2: Проверка полей ===
# Project: MathWorkbook
VALID_TOPICS = {"algebra", "geometry", "arithmetic", "trigonometry", "statistics"}
VALID_DIFFICULTIES = {"easy", "medium", "hard"}
VALID_STATUSES = {"draft", "active", "solved"}


def normalize_topic(raw):
    return raw.strip().lower()


def normalize_difficulty(raw):
    return raw.strip().lower()


def normalize_status(raw):
    return raw.strip().lower()


def normalize_condition(raw):
    return raw.strip()


def normalize_task(raw):
    return " ".join(raw.strip().split())


def validate_topic(topic):
    if not topic:
        return "Topic is required."
    normalized = normalize_topic(topic)
    if not normalized:
        return "Topic cannot be empty."
    if normalized not in VALID_TOPICS:
        available = ", ".join(sorted(VALID_TOPICS))
        return f"Invalid topic '{topic}'. Choose from: {available}."
    return None


def validate_difficulty(difficulty):
    if not difficulty:
        return "Difficulty is required."
    normalized = normalize_difficulty(difficulty)
    if not normalized:
        return "Difficulty cannot be empty."
    if normalized not in VALID_DIFFICULTIES:
        available = ", ".join(sorted(VALID_DIFFICULTIES))
        return f"Invalid difficulty '{difficulty}'. Choose from: {available}."
    return None


def validate_status(status):
    if not status:
        return "Status is required."
    normalized = normalize_status(status)
    if not normalized:
        return "Status cannot be empty."
    if normalized not in VALID_STATUSES:
        available = ", ".join(sorted(VALID_STATUSES))
        return f"Invalid status '{status}'. Choose from: {available}."
    return None


def validate_condition(condition):
    if not condition:
        return "Condition is required."
    normalized = normalize_condition(condition)
    if not normalized:
        return "Condition cannot be empty."
    return None


def validate_task(task):
    if not task:
        return "Task description is required."
    normalized = normalize_task(task)
    if not normalized:
        return "Task description cannot be empty."
    return None


def validate_task_fields(condition, topic, difficulty, status):
    errors = []
    condition_error = validate_condition(condition)
    if condition_error:
        errors.append(condition_error)
    topic_error = validate_topic(topic)
    if topic_error:
        errors.append(topic_error)
    difficulty_error = validate_difficulty(difficulty)
    if difficulty_error:
        errors.append(difficulty_error)
    status_error = validate_status(status)
    if status_error:
        errors.append(status_error)
    return errors
