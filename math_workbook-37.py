# === Stage 37: Импорт из CSV ===
# Project: MathWorkbook
def parse_csv_task_line(line):
    if line is None:
        return None
    stripped = line.strip()
    if not stripped:
        return None
    parts = stripped.split(",")
    if len(parts) < 4:
        return None
    title = parts[0].strip()
    topic = parts[1].strip()
    difficulty = parts[2].strip()
    status = parts[3].strip()
    if not title or not topic or not difficulty or not status:
        return None
    return {
        "title": title,
        "topic": topic,
        "difficulty": difficulty,
        "status": status,
    }


def parse_csv_tasks(csv_text, header_map):
    if not csv_text:
        return []
    header_keys = list(header_map.keys())
    rows = csv_text.strip().splitlines()
    if len(rows) < 2:
        return []
    for index, raw_line in enumerate(rows[1:], start=2):
        if not raw_line.strip():
            continue
        parts = raw_line.strip().split(",")
        if len(parts) < len(header_keys):
            continue
        record = {}
        for position, key in enumerate(header_keys):
            source_key = header_map.get(key)
            if source_key is None or position >= len(parts):
                record[key] = None
                continue
            record[key] = parts[position].strip()
        if not record.get("title") or not record.get("topic"):
            continue
        record["line_number"] = index
        tasks.append(record)
    return tasks


def build_header_map(header_row):
    header_keys = [item.strip() for item in header_row.split(",")]
    header_map = {}
    for key in header_keys:
        header_map[key] = key
    return header_map
