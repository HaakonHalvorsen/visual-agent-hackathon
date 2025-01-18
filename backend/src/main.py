import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .presentation.routers.agent_router import agent_router

app = FastAPI(dependencies=[])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


app.include_router(router=agent_router, prefix="/v1")

@app.get("/")
async def root():
    """Root endpoint for the AI agent backend."""
    return {
        "message": "Welcome to the AI agent backend!",
        "description": "This is the root path of the API. Go to /docs.",
    }
