# === Stage 49: Интерактивное меню ===
# Project: MathWorkbook
COMMANDS = {
    "help": "Show available commands",
    "list": "List all problems",
    "add": "Add a new problem",
    "show": "Show details of a problem",
    "status": "Change the status of a problem",
    "quit": "Exit the menu",
}

HELP_TEXT = "Commands: help, list, add, show, status, quit"


def print_help():
    for key, value in COMMANDS.items():
        print(f"{key} - {value}")


def list_problems(problems):
    if not problems:
        print("No problems yet.")
        return
    for problem in problems.values():
        print(f"[{problem['id']}] {problem['title']} "
              f"(topic: {problem['topic']}, "
              f"difficulty: {problem['difficulty']}, "
              f"status: {problem['status']})")


def add_problem(problems):
    problem_id = input("Enter problem id: ").strip()
    title = input("Enter problem title: ").strip()
    topic = input("Enter topic: ").strip()
    difficulty = input("Enter difficulty (easy/medium/hard): ").strip()
    problems[problem_id] = {
        "id": problem_id,
        "title": title,
        "topic": topic,
        "difficulty": difficulty,
        "status": "active",
    }
    print(f"Problem {problem_id} added.")


def show_problem(problems):
    problem_id = input("Enter problem id to show: ").strip()
    if problem_id in problems:
        problem = problems[problem_id]
        print(f"[{problem['id']}] {problem['title']}")
        print(f"Topic: {problem['topic']}")
        print(f"Difficulty: {problem['difficulty']}")
        print(f"Status: {problem['status']}")
    else:
        print("Problem not found.")


def change_status(problems):
    problem_id = input("Enter problem id to update status: ").strip()
    if problem_id not in problems:
        print("Problem not found.")
        return
    new_status = input("Enter new status (active/active_done/error): ").strip()
    problems[problem_id]["status"] = new_status
    print(f"Status of {problem_id} updated to {new_status}.")


def problem_menu(problems):
    print(HELP_TEXT)
    while True:
        choice = input("Enter command: ").strip().lower()
        if choice in COMMANDS:
            if choice == "help":
                print_help()
            elif choice == "list":
                list_problems(problems)
            elif choice == "add":
                add_problem(problems)
            elif choice == "show":
                show_problem(problems)
            elif choice == "status":
                change_status(problems)
            elif choice == "quit":
                print("Exiting problem menu.")
                break
        else:
            print("Unknown command. Use 'help' to see available commands.")
