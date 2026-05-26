"""Browser manager

Manage Playwright browser lifecycle and provide helper functions to acquire pages/contexts.
This service is intended to be long-lived and reused across requests.
"""
from playwright.async_api import async_playwright, Browser
import asyncio

_playwright = None
_browser: Browser | None = None


async def start():
    global _playwright, _browser
    if _playwright is not None:
        return
    _playwright = await async_playwright().start()
    _browser = await _playwright.chromium.launch(headless=True)


async def stop():
    global _playwright, _browser
    if _browser:
        await _browser.close()
        _browser = None
    if _playwright:
        await _playwright.stop()
        _playwright = None


async def new_context(proxy: dict | None = None):
    """Create and return a new browser context.

    The `proxy` dict can include Playwright's proxy options.
    """
    if _browser is None:
        await start()
    return await _browser.new_context(**({"proxy": proxy} if proxy else {}))


async def new_page(proxy: dict | None = None):
    ctx = await new_context(proxy)
    return await ctx.new_page()
