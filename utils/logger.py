import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
LOG_PATH = os.path.join(LOG_DIR, "app.log")

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("llm_api")
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(LOG_PATH, maxBytes=5_000_000, backupCount=5)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
