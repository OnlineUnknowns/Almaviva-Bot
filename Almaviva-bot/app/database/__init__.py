"""Database initialization and helpers using SQLAlchemy (sync).

For production, consider using Alembic for migrations and an RDBMS like Postgres.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./data/almaviva_bot.db')

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith('sqlite') else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    # Import models here to ensure they are registered on Base.metadata
    from app.database import models
    Base.metadata.create_all(bind=engine)


# Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
