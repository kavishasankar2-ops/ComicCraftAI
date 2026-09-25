from typing import Any, Dict

from app.services.image_generator import generate_image


def generate_comic(payload, settings=None) -> Dict[str, Any]:

    if hasattr(payload, "model_dump"):
        data = payload.model_dump()
    else:
        data = payload

    story_prompt = data.get("story_prompt", "")
    character_name = data.get("character_name", "Main Character")
    setting = data.get("setting", "Unknown Setting")
    tone = data.get("tone", "Adventure")
    art_style = data.get("art_style", "Comic Book")

    panels = []

    for i in range(1, 5):

        panel_prompt = (
            f"{art_style} comic panel. "
            f"Character: {character_name}. "
            f"Setting: {setting}. "
            f"Story: {story_prompt}. "
            f"Tone: {tone}. "
            f"Panel {i}."
        )

        try:
            image_path = generate_image(
                prompt=panel_prompt,
                settings=settings,
                name=f"panel_{i}"
            )
        except Exception as e:
            image_path = None
            print(f"Image generation failed for panel {i}: {e}")

        panels.append(
            {
                "panel_number": i,
                "description": panel_prompt,
                "dialogue": "",
                "narration": "",
                "image_prompt": panel_prompt,
                "image_path": image_path,
            }
        )

    return {
        "title": "Generated Comic",
        "prompt": story_prompt,
        "character_name": character_name,
        "setting": setting,
        "tone": tone,
        "art_style": art_style,
        "panels": panels,
    }