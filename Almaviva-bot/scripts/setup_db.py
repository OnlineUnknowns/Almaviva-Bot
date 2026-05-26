"""DB helper script to initialize database tables.

Run `python scripts/setup_db.py` to create tables defined in `app.database.models`.
"""
from app.database import init_db


if __name__ == '__main__':
    init_db()
    print("Database initialized")
