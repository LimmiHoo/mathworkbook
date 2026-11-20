# === Stage 40: Миграции схемы ===
# Project: MathWorkbook
def migrate_problem_fields_v1_to_v2(store):
    for problem in store["problems"].values():
        if "topic" in problem and "topic_slug" not in problem:
            problem["topic_slug"] = slugify_topic(problem["topic"])
    return store


def migrate_problem_fields_v2_to_v3(store):
    for problem in store["problems"].values():
        if "topic_slug" in problem and problem["topic_slug"] is None:
            problem["topic_slug"] = "general"
    return store


def migrate_problem_fields_v3_to_v4(store):
    for problem in store["problems"].values():
        if "topic_slug" in problem:
            problem["topic_slug"] = problem["topic_slug"].strip().lower().replace(" ", "_")
    return store


def migrate_problem_fields_v4_to_v5(store):
    for problem in store["problems"].values():
        problem["topic_slug"] = normalize_topic_slug(problem.get("topic_slug", ""))
    return store


def migrate_problem_fields_v5_to_v6(store):
    for problem in store["problems"].values():
        problem["topic_slug"] = normalize_topic_slug(problem.get("topic_slug", ""))
        problem["topic_slug"] = re.sub(r"[^0-9a-zA-Z_]+", "_", problem["topic_slug"]).strip("_")
    return store


def migrate_problem_fields_v6_to_v7(store):
    for problem in store["problems"].values():
        if not problem.get("topic_slug"):
            problem["topic_slug"] = "general"
        problem["topic_slug"] = re.sub(r"[^0-9a-zA-Z_]+", "_", problem["topic_slug"]).strip("_")
    return store


def migrate_problem_fields_v7_to_v8(store):
    for problem in store["problems"].values():
        problem["topic_slug"] = re.sub(r"[^0-9a-zA-Z_]+", "_", problem["topic_slug"]).strip("_")
    return store


def slugify_topic(topic):
    topic = topic.strip().lower()
    topic = re.sub(r"[^0-9a-zA-Zа-яА-Я]+", " ", topic)
    topic = re.sub(r"[^0-9a-zA-Z_]+", "_", topic).strip("_")
    return topic or "general"


def normalize_topic_slug(slug):
    slug = re.sub(r"[^0-9a-zA-Z_]+", "_", slug).strip("_")
    return slug or "general"
