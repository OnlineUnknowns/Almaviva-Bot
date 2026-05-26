"""Run entry for almaviva-bot.

This file runs the FastAPI app using Uvicorn in production or development.
"""
import os
import uvicorn

if __name__ == '__main__':
    host = os.getenv('ALMAVIVA_HOST', '0.0.0.0')
    port = int(os.getenv('ALMAVIVA_PORT', 8000))
    uvicorn.run('app.main:app', host=host, port=port, reload=os.getenv('ALMAVIVA_DEBUG', '1') == '1')
