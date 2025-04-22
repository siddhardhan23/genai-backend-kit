from app.logger import logger
from app.llm.llm_factory import load_llm


def get_answer(provider, model, question):
    logger.info(f"Received request for answer generation. Provider: {provider}, Model: {model}, Question: {question}")

    try:
        llm = load_llm(provider=provider, model=model)
        logger.debug(f"LLM loaded successfully for Provider: {provider}, Model: {model}")

        response = llm.invoke(question)
        answer = response.content

        logger.info(f"Answer generated successfully.")
        logger.debug(f"Answer: {answer}")

        return {"answer": answer}
    except Exception as e:
        logger.exception(f"Error occurred while generating answer: {e}")
        return {"error": "Failed to generate answer. Please try again later."}


# from app.config import app_config

# ans = get_answer("Groq", "gemma2-9b-it", "What is ML?")
# ans = get_answer("Ollama", "gemma:2b", "What is ML?")
# ans = get_answer("Openai", "gpt-4.1-nano-2025-04-14", "What is ML?")
# print(ans)
