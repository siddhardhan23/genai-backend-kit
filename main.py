from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes as api_routes
from app.config import app_config
import uvicorn

app = FastAPI(title="LLM API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(api_routes.router)

# Run server
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=app_config.get("host", "0.0.0.0"),
        port=app_config.get("port", 8000),
        reload=True
    )
