from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from app.logger import logger

def load_llm(provider, model):
    logger.info("Loading LLM | Provider: %s | Model: %s", provider, model)

    try:
        if provider == "Groq":
            llm = ChatGroq(model=model, temperature=0)
        elif provider == "Ollama":
            llm = ChatOllama(model=model, temperature=0)
        elif provider == "Openai":
            llm = ChatOpenAI(model=model, temperature=0)
        else:
            logger.error("Unsupported LLM provider: %s", provider)
            raise ValueError(f"Unsupported provider: {provider}")

        logger.info("LLM loaded successfully for provider: %s", provider)
        return llm

    except Exception as e:
        logger.exception("Failed to load LLM for provider: %s, model: %s", provider, model)
        raise
