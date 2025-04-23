from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes as api_routes
from utils.config import app_config
from utils.logger import logger
import uvicorn

app = FastAPI(title="LLM API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
logger.info("CORS middleware configured with permissive settings.")

# Register routes
app.include_router(api_routes.router)
logger.info("API routes registered successfully.")

# Run server
if __name__ == "__main__":
    host = app_config.get("api", {}).get("host", "localhost")
    port = app_config.get("api", {}).get("port", 8000)
    logger.info("Starting FastAPI server at %s:%s", host, port)

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True
    )
