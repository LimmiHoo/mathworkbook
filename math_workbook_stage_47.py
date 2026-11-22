# === Stage 47: Журнал действий ===
# Project: MathWorkbook
import logging
import sys

LOGGER_NAME = "mathworkbook"

def configure_logger(name: str = LOGGER_NAME, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger

def get_logger(name: str = LOGGER_NAME) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        configure_logger(name)
    return logger

def log_task_started(task_id: str, topic: str, difficulty: str) -> None:
    get_logger().info("task started | id=%s | topic=%s | difficulty=%s", task_id, topic, difficulty)

def log_task_solved(task_id: str, attempts: int) -> None:
    get_logger().info("task solved | id=%s | attempts=%d", task_id, attempts)

def log_attempt(task_id: str, success: bool, message: str = "") -> None:
    if success:
        get_logger().debug("attempt success | id=%s | %s", task_id, message)
    else:
        get_logger().warning("attempt failed | id=%s | %s", task_id, message)

def log_error(module: str, error_type: str, message: str = "") -> None:
    get_logger().error("error | module=%s | type=%s | %s", module, error_type, message)

def log_info(message: str) -> None:
    get_logger().info(message)

def main() -> None:
    configure_logger()
    log_info("MathWorkbook logger configured")
    log_task_started("task_001", "arithmetic", "easy")
    log_attempt("task_001", success=False, message="wrong answer")
    log_attempt("task_001", success=True, message="correct")
    log_task_solved("task_001", attempts=2)
    log_error("arithmetic", "ValueError", "invalid operand")

if __name__ == "__main__":
    main()
