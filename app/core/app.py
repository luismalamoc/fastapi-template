from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.tasks.router import router as tasks_router
from app.core.error_handlers import add_exception_handlers

def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add routers
    app.include_router(tasks_router, prefix="/api")

    # Add exception handlers
    add_exception_handlers(app)

    # Health check endpoint
    @app.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "ok"}

    return app
