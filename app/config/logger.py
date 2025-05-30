import logging
import sys

from app.config.settings import settings

# Configure logger
def setup_logger():
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
    
    # Create formatter for console output
    console_formatter = logging.Formatter(
        "%(levelname)s: %(message)s"
    )
    
    # Create console handler only
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    return logger

# Create logger instance
logger = setup_logger()
