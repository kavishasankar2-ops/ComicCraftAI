from pydantic import BaseModel
from typing import Optional


class PromptRequest(BaseModel):
    story_prompt: str
    character_name: str
    setting: str
    tone: str
    art_style: str


class ImageRequest(BaseModel):
    prompt: str
    style: Optional[str] = "comic"