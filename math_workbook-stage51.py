# === Stage 51: Подкоманды argparse ===
# Project: MathWorkbook
import argparse

SUBCOMMANDS = ("add", "list", "show")


def build_parser():
    parser = argparse.ArgumentParser(prog="mathwork", description="Math workbook tasks")
    tasks = parser.add_subparsers(dest="task_command", metavar="task")

    add_parser = tasks.add_parser("add", help="Add a new task")
    add_parser.add_argument("--condition", required=True, help="Task condition")
    add_parser.add_argument("--topic", required=True, help="Task topic")
    add_parser.add_argument("--difficulty", required=True, choices=("easy", "medium", "hard"), help="Task difficulty")
    add_parser.add_argument("--status", default="open", choices=("open", "done"), help="Task status")

    tasks.add_parser("list", help="List all tasks")
    tasks.add_parser("show", help="Show a single task by id")

    return parser


def parse_args(argv):
    parser = build_parser()
    return parser.parse_args(argv)
