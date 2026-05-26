"""Notifier

Send notifications (email, webhook, SMS) on booking events.
"""

def notify(user_id: int, message: str) -> None:
    """Send notification to user or external system."""
    # TODO: implement notification channels (SMTP, webhook, Twilio, etc.)
    print(f"Notify {user_id}: {message}")
