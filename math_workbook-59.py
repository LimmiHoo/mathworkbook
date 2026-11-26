# === Stage 59: Пошаговый ввод ===
# Project: MathWorkbook
def prompt_task_field(prompt_text):
    return input(prompt_text).strip()


def read_task_condition():
    condition = prompt_task_field("Условие задачи: ")
    while not condition:
        print("Условие не может быть пустым. Попробуйте снова.")
        condition = prompt_task_field("Условие задачи: ")
    return condition


def read_task_topic():
    topic = prompt_task_field("Тема: ")
    while not topic:
        print("Тема не может быть пустой. Попробуйте снова.")
        topic = prompt_task_field("Тема: ")
    return topic


def read_task_difficulty():
    print("Доступные уровни сложности: easy, medium, hard")
    difficulty = prompt_task_field("Сложность: ").lower()
    valid_levels = ("easy", "medium", "hard")
    while difficulty not in valid_levels:
        print(f"Неверный уровень сложности. Доступны: {', '.join(valid_levels)}")
        difficulty = prompt_task_field("Сложность: ").lower()
    return difficulty


def read_task_status():
    print("Доступные статусы: new, in_progress, solved")
    status = prompt_task_field("Статус: ").lower()
    valid_statuses = ("new", "in_progress", "solved")
    while status not in valid_statuses:
        print(f"Неверный статус. Доступны: {', '.join(valid_statuses)}")
        status = prompt_task_field("Статус: ").lower()
    return status


def build_task():
    task = {
        "condition": read_task_condition(),
        "topic": read_task_topic(),
        "difficulty": read_task_difficulty(),
        "status": read_task_status(),
    }
    return task


if __name__ == "__main__":
    new_task = build_task()
    print("Создана задача:")
    for key, value in new_task.items():
        print(f"  {key}: {value}")
