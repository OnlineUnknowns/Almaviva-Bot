"""Captcha solver module

Abstracts captcha solving; integrate external solver or Turnstile solver here.
"""

def solve_captcha(image_path: str) -> str:
    """Return solved captcha text for given image path.

    Placeholder implementation; integrate Turnstile solver or third-party API.
    """
    return "solved-captcha"
