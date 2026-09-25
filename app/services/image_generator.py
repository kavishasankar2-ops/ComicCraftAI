import os
from pathlib import Path

from huggingface_hub import InferenceClient


def generate_image(prompt, settings=None, name="image"):
    """
    Generate an image using Hugging Face Inference Providers.
    """

    token = os.getenv("HF_TOKEN")

    if not token and settings:
        token = getattr(settings, "HF_TOKEN", None)

    if not token:
        raise ValueError("HF_TOKEN is missing in your .env file")

    model = os.getenv(
        "HF_IMAGE_MODEL",
        "black-forest-labs/FLUX.1-schnell"
    )

    if settings:
        model = getattr(settings, "HF_IMAGE_MODEL", model)

    # Let Hugging Face automatically choose an available provider
    client = InferenceClient(
        provider="auto",
        api_key=token
    )

    image = client.text_to_image(
        prompt=prompt,
        model=model
    )

    output_dir = Path("static/generated")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{name}.png"

    image.save(output_file)

    return str(output_file)