import logging
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, "errors.log"),
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

def log_error(context: str, error: Exception) -> None:
    """
    Writes an error message to the log file.

    :param context: Name of the function or context where the error occurred
    :param error: Exception object
    """
    logging.error(f"{context}: {str(error)}")