import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_healthz import (
    HealthCheckRegistry,
    HealthCheckDatabase,
    health_check_route
)

from app.config.settings import settings
from app.config.database import engine, Base
from app.routes import task_router
from app.utils.error_handler import add_exception_handlers
from app.config.logger import logger

def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application
    """
    # Create database tables
    Base.metadata.create_all(bind=engine)
    
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
    app.include_router(task_router, prefix="/api")

    # Add exception handlers
    add_exception_handlers(app)

    # Add health check endpoints
    health_registry = HealthCheckRegistry()
    
    # Add SQLite database health check
    health_registry.add(HealthCheckDatabase(uri=settings.DATABASE_URL))
    
    # Add health check route
    app.add_api_route(
        "/healthz", 
        endpoint=health_check_route(registry=health_registry),
        tags=["Health"],
        summary="Health Check",
        description="Checks the health status of the application and its dependencies"
    )
    
    logger.info("Application started successfully")
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
