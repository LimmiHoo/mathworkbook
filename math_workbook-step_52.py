# === Stage 52: Подкоманды изменения ===
# Project: MathWorkbook
def handle_report(workbook, args):
    task = workbook.get_task(args.task_id)
    if not task:
        print(f"Task {args.task_id} not found")
        return
    attempts = workbook.get_attempts(args.task_id)
    if not attempts:
        print(f"No attempts recorded for task {args.task_id}")
        return
    total_attempts = len(attempts)
    solved_attempts = sum(1 for a in attempts if a["solved"])
    print(f"Task {args.task_id}: {solved_attempts}/{total_attempts} attempts solved")
    for attempt in attempts:
        print(f"  attempt {attempt['id']}: solved={attempt['solved']}")


def handle_edit(workbook, args):
    task = workbook.get_task(args.task_id)
    if not task:
        print(f"Task {args.task_id} not found")
        return
    if args.condition is not None:
        task["condition"] = args.condition
    if args.topic is not None:
        task["topic"] = args.topic
    if args.difficulty is not None:
        task["difficulty"] = args.difficulty
    print(f"Task {args.task_id} updated")


def handle_delete(workbook, args):
    if not workbook.delete_task(args.task_id):
        print(f"Task {args.task_id} not found")
        return
    print(f"Task {args.task_id} deleted")
