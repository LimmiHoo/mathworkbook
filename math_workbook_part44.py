# === Stage 44: Цветной вывод ===
# Project: MathWorkbook
import os
import sys

_ANSI_RESET = "\033[0m"
_ANSI_COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "gray": "\033[90m",
    "bold": "\033[1m",
}


def color_enabled() -> bool:
    return os.environ.get("NO_COLOR") is None and sys.stdout.isatty()


def colorize(text: str, color: str) -> str:
    if not color_enabled() or color not in _ANSI_COLORS:
        return text
    return f"{_ANSI_COLORS[color]}{text}{_ANSI_RESET}"


def section(title: str, color: str = "cyan", indent: int = 0) -> str:
    prefix = "  " * indent
    return f"{prefix}{colorize(title, color)}\n"


def status_line(status: str, detail: str, color: str = "gray", indent: int = 1) -> str:
    prefix = "  " * indent
    return f"{prefix}{colorize(status, color)}  {detail}\n"


def render_problem(problem: dict) -> str:
    lines = [section("PROBLEM", "bold", 0)]
    lines.append(status_line("STATUS", problem.get("status", "unknown"),
                             "yellow" if problem.get("status") == "solved" else "blue"))
    lines.append(section("TOPIC", "magenta", 1))
    lines.append(section("DIFFICULTY", "yellow", 1))
    lines.append(status_line("CONDITION", problem.get("condition", "n/a"), indent=1))
    return "".join(lines)


def render_solution(solution: str) -> str:
    lines = [section("SOLUTION", "green", 0)]
    lines.append(solution if solution else "no solution yet")
    return "".join(lines)


def render_error(error: str) -> str:
    lines = [section("ERROR", "red", 0)]
    lines.append(error if error else "no errors recorded")
    return "".join(lines)


def render_attempt(attempt: dict) -> str:
    lines = [section("ATTEMPT", "cyan", 0)]
    lines.append(status_line("RESULT", attempt.get("result", "pending"),
                             "green" if attempt.get("result") == "correct" else "red"))
    return "".join(lines)
