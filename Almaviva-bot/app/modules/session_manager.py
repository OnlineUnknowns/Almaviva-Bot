"""Session manager

Persist and load user session state (cookies, tokens) to `data/` for reuse.
"""
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "sessions"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_session(user_id: int, session_data: dict):
    path = DATA_DIR / f"session_{user_id}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(session_data, f)


def load_session(user_id: int):
    path = DATA_DIR / f"session_{user_id}.json"
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
