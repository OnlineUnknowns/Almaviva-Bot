"""Scheduler module

Expose functions to schedule booking attempts. In production use APScheduler or Celery.
"""

def schedule_appointment(user_id: int, datetime_str: str) -> dict:
    """Schedule an appointment attempt.

    This is a placeholder. Replace with APScheduler/Celery integration.
    """
    return {"status": "scheduled", "when": datetime_str}
