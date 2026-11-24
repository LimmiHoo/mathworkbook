# === Stage 53: Режим dry-run ===
# Project: MathWorkbook
import argparse
from dataclasses import dataclass, field
from typing import List, Callable, TypeVar, Generic


T = TypeVar("T")
R = TypeVar("R")


@dataclass
class Change(Generic[T]):
    entity_type: str
    identifier: str
    field: str
    old_value: object
    new_value: object


@dataclass
class DryRunContext:
    changes: List[Change] = field(default_factory=list)

    def record(self, change: Change) -> None:
        self.changes.append(change)

    def describe(self, verb: str = "would update") -> str:
        if not self.changes:
            return f"{verb} nothing."
        lines = []
        for change in self.changes:
            value = change.old_value
            if value is None:
                value = "absent"
            lines.append(
                f"  - {change.entity_type} #{change.identifier}: "
                f"{change.field} {value!r} -> {change.new_value!r}"
            )
        return f"{verb} {len(self.changes)} change(s):\n" + "\n".join(lines)


def apply_or_dry_run(
    apply_fn: Callable[[T], R],
    change_fn: Callable[[T], Change],
    context: DryRunContext,
    entity: T,
) -> R:
    change = change_fn(entity)
    if context.changes:
        return apply_fn(entity)
    context.record(change)
    return None


def parse_dry_run_flag(args: argparse.Namespace) -> bool:
    return getattr(args, "dry_run", False)
