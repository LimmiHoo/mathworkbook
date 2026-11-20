# === Stage 38: Сохранение в файл ===
# Project: MathWorkbook
import json
import os
import tempfile
from pathlib import Path


class StateStore:
    """Persist MathWorkbook state to a local JSON file with atomic writes."""

    def __init__(self, path):
        self.path = Path(path)
        self._load()

    def _load(self):
        if self.path.exists():
            try:
                with open(self.path, "r", encoding="utf-8") as file:
                    self.data = json.load(file)
            except (json.JSONDecodeError, OSError):
                self.data = {}
        else:
            self.data = {}

    def save(self, data):
        self.data = data
        directory = self.path.parent
        directory.mkdir(parents=True, exist_ok=True)
        fd, temp_path = tempfile.mkstemp(
            dir=str(directory),
            prefix=".mathworkbook-",
            suffix=".tmp",
        )
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=2, ensure_ascii=False)
                file.flush()
                os.fsync(file.fileno())
            os.replace(temp_path, self.path)
        except OSError:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise

    def load(self):
        return self.data
