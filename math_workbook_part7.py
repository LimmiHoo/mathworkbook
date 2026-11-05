# === Stage 7: Фильтрация записей ===
# Project: MathWorkbook
def filter_tasks_by_topic(tasks, topic):
    return [task for task in tasks if task["topic"] == topic]


def filter_tasks_by_date_range(tasks, start_date, end_date):
    filtered = []
    for task in tasks:
        task_date = task.get("date")
        if task_date is None:
            continue
        if start_date is not None and task_date < start_date:
            continue
        if end_date is not None and task_date > end_date:
            continue
        filtered.append(task)
    return filtered


def filter_tasks(tasks, topic=None, start_date=None, end_date=None):
    if topic is not None:
        tasks = filter_tasks_by_topic(tasks, topic)
    if start_date is not None or end_date is not None:
        tasks = filter_tasks_by_date_range(tasks, start_date, end_date)
    return tasks


def build_filtered_tasks(tasks, topic=None, start_date=None, end_date=None):
    result = filter_tasks(tasks, topic, start_date, end_date)
    return [dict(task) for task in result]
