# === Stage 27: Генератор задач ===
# Project: MathWorkbook
import random

THEMES = {
    "arithmetic": lambda: (random.randint(1, 12), random.randint(1, 12)),
    "fractions": lambda: (random.randint(1, 9), random.randint(2, 8)),
    "geometry": lambda: (random.randint(2, 15), random.randint(1, 10)),
    "algebra": lambda: (random.randint(-10, 10), random.randint(1, 6)),
}

LEVELS = ["easy", "medium", "hard"]


def make_arithmetic_problem():
    a, b = THEMES["arithmetic"]()
    return f"What is {a} + {b}?"


def make_fractions_problem():
    num, den = THEMES["fractions"]()
    return f"Reduce the fraction {num}/{den} to its lowest terms."


def make_geometry_problem():
    side, count = THEMES["geometry"]()
    return f"Find the perimeter of a square with side length {side}, using {count} sides."


def make_algebra_problem():
    x, k = THEMES["algebra"]()
    return f"Solve for x: {k}x = {k * x}."


def generate_problems(topic, count=5):
    problem_makers = {
        "arithmetic": make_arithmetic_problem,
        "fractions": make_fractions_problem,
        "geometry": make_geometry_problem,
        "algebra": make_algebra_problem,
    }
    maker = problem_makers.get(topic)
    problems = []
    if maker:
        for _ in range(count):
            problems.append({
                "condition": maker(),
                "topic": topic,
                "difficulty": random.choice(LEVELS),
                "status": "unresolved",
            })
    return problems


if __name__ == "__main__":
    for problem in generate_problems("arithmetic", 3):
        print(f"[{problem['difficulty']}] {problem['condition']}")
