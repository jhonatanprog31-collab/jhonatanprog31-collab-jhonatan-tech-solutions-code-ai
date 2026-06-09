"""
Utility functions and helpers
"""
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def log_info(message: str, **kwargs):
    """Log info message"""
    logger.info(f"{message} | {kwargs}")


def log_error(message: str, exception: Optional[Exception] = None):
    """Log error message"""
    if exception:
        logger.error(f"{message}: {str(exception)}", exc_info=True)
    else:
        logger.error(message)


def format_response(data: dict, success: bool = True, message: str = ""):
    """Format API response"""
    return {
        "success": success,
        "message": message,
        "data": data
    }
