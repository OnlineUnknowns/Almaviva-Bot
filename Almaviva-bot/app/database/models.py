"""SQLAlchemy models for almaviva-bot."""
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    disabled = Column(Boolean, default=False)


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False)
    appointment_data = Column(String, nullable=False)
    created_at = Column(DateTime)
