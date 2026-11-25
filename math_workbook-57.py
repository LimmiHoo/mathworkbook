# === Stage 57: Отмена и повтор ===
# Project: MathWorkbook
def undo_and_redo_stack():
    """Support undo/redo of the last operation on the operations stack."""
    class Operation:
        def __init__(self, label, apply):
            self.label = label
            self.apply = apply

        def run(self, state):
            return self.apply(state)

    class Workbook:
        def __init__(self):
            self.operations = []
            self.redo_stack = []

        def add_operation(self, label, apply):
            self.operations.append(Operation(label, apply))
            self.redo_stack.clear()

        def undo(self):
            if not self.operations:
                return False
            last = self.operations.pop()
            self.redo_stack.append(last)
            return True

        def redo(self):
            if not self.redo_stack:
                return False
            op = self.redo_stack.pop()
            self.operations.append(op)
            return True

        def is_undoable(self):
            return bool(self.operations)

        def is_redoable(self):
            return bool(self.redo_stack)

    workbook = Workbook()
    workbook.add_operation("add", lambda s: s + 1)
    workbook.add_operation("double", lambda s: s * 2)
    print(workbook.is_undoable(), workbook.is_redoable())
    workbook.undo()
    print(workbook.is_undoable(), workbook.is_redoable())
    workbook.redo()
    print(workbook.is_undoable(), workbook.is_redoable())
    workbook.undo()
    workbook.undo()
    print(workbook.is_undoable(), workbook.is_redoable())
