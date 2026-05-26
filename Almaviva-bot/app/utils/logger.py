"""Logging utilities.

Configure rotating file handler writing to `data/logs` and console output.
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parents[2] / "data" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)


def configure_logging(level: int = logging.INFO):
    logger = logging.getLogger()
    if logger.handlers:
        return

    logger.setLevel(level)
    fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")

    fh = RotatingFileHandler(LOG_DIR / "almaviva-bot.log", maxBytes=10 * 1024 * 1024, backupCount=5)
    fh.setLevel(level)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(fmt)
    logger.addHandler(ch)
