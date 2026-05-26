"""FastAPI application entrypoint for almaviva-bot.

This module wires routes and startup/shutdown events. Keep business logic in `app.modules` and long-lived services in `app.services`.
"""
from fastapi import FastAPI
from app.routes import api
from app.utils.logger import configure_logging

app = FastAPI(title="almaviva-bot")

# Configure logging early
configure_logging()

# Include API routes
app.include_router(api.router, prefix="/api")


@app.on_event("startup")
async def startup_event():
    # Initialize services (browser, proxy, DB connections)
    from app.services import browser_manager
    await browser_manager.start()


@app.on_event("shutdown")
async def shutdown_event():
    from app.services import browser_manager
    await browser_manager.stop()
