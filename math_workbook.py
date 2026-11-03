# === Stage 1: Каркас модуля ===
# Project: MathWorkbook
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Problem:
    """Math task entity."""
    statement: str
    topic: str
    difficulty: str
    status: Optional[str] = None

    def show(self) -> None:
        print(f"[{self.difficulty}] {self.topic}: {self.statement} -> {self.status}")


def make_demo_problems() -> list[Problem]:
    """Create a few demonstration tasks."""
    return [
        Problem("Solve for x: 2x + 6 = 0", "Linear equations", "easy"),
        Problem("Compute the area of a circle with radius 3", "Geometry", "easy"),
        Problem("Find the roots of x^2 - 5x + 6 = 0", "Quadratics", "medium"),
        Problem("Prove the Pythagorean theorem", "Geometry", "hard"),
    ]


def main() -> None:
    problems = make_demo_problems()
    print("MathWorkbook demo problems:")
    for problem in problems:
        problem.show()


if __name__ == "__main__":
    main()
