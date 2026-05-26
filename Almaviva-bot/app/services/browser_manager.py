"""Service wrapper for browser_manager module.

This file provides a single place to import the browser lifecycle functions used by the app.
"""
from app.modules import browser_manager as _bm

start = _bm.start
stop = _bm.stop
new_context = _bm.new_context
new_page = _bm.new_page
