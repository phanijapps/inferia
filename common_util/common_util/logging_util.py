import logging


def setup_logger(name=None, log_level=logging.INFO, log_file=None):
    """Setup and return a logger with a specific name, log level, and optional file output."""
    
    logger = logging.getLogger(name)
    
    if not logger.hasHandlers():  # Prevent adding multiple handlers if the logger is already configured
        logger.setLevel(log_level)

        # Define the log format
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(log_format)

        # Stream handler (console)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # Optional file handler
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger

