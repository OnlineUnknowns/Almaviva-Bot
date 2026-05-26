"""Proxy manager

Manage proxy rotation, health checks and selection.
"""

def get_proxy() -> str:
    """Return a proxy URL to be used by browser/service."""
    # TODO: implement proxy pool, rotation and health checks
    return "http://127.0.0.1:8888"
