from app.config import app_config

def fetch_llm_options():
    llm_config = app_config["llm"]
    return llm_config
