# === Stage 55: Справка по командам ===
# Project: MathWorkbook
HELP_COMMANDS = {
    "task": "List all tasks in the workbook with their status.",
    "topic": "Show all topics with the number of tasks for each.",
    "add": "Add a new task with a condition, topic, difficulty, and status.",
    "solve": "Record a solution attempt for a task.",
    "error": "Log an error or mistake made while solving a task.",
    "stats": "Display statistics: total tasks, attempts, and errors.",
    "quit": "Exit the workbook application.",
}


def show_help():
    print("Available commands:")
    for command, description in HELP_COMMANDS.items():
        print(f"  {command:<8} {description}")
    print("\nExample usage:")
    print("  task -- list tasks")
    print("  add -- add a new task")
    print("  solve -- record a solution")
    print("  error -- log an error")
    print("  stats -- show statistics")
    print("  quit -- exit the application")
