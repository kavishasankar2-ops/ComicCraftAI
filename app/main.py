
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import router


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Static directory
STATIC_DIR = BASE_DIR / "static"

# Create static directory automatically if it doesn't exist
STATIC_DIR.mkdir(parents=True, exist_ok=True)


app = FastAPI(
    title="ComicCraft API",
    description=(
        "AI comic story creator using "
        "Gemini and image generation."
    ),
    version="1.0.0",
)


# API routes
app.include_router(router)


# Static files
app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)


@app.get("/health")
async def health():
    return {
        "status": "ok",
    }