import os
from dotenv import load_dotenv

load_dotenv()

def get_settings():
    return {
        "HF_API_KEY": os.getenv("HF_API_KEY")
    }