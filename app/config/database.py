from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.config.settings import settings

# Create SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)

# Create Base class for models
Base = declarative_base()

# Create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db():
    """
    Dependency for getting a database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
