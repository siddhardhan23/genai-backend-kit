# config.py

from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
import json
from pydantic_settings import BaseSettings

# Path to config.json in project root
CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.json"

# Safely load app config
with open(CONFIG_PATH) as f:
    app_config = json.load(f)

# Pydantic environment config
class AppConfig(BaseSettings):
    GROQ_API_KEY: str
    OPENAI_API_KEY: str
    APP_API_KEY: str

    class Config:
        env_file = ".env"

env_config = AppConfig()
