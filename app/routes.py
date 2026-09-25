from pathlib import Path

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import get_settings
from app.schemas import PromptRequest
from app.services.comic_service import generate_comic


router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    story_prompt: str = Form(...),
    character_name: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...),
):

    payload = PromptRequest(
        story_prompt=story_prompt,
        character_name=character_name,
        setting=setting,
        tone=tone,
        art_style=art_style,
    )

    result = generate_comic(payload)

    return templates.TemplateResponse(
        request=request,
        name="comic_preview.html",
        context={
            "comic": result
        },
    )


