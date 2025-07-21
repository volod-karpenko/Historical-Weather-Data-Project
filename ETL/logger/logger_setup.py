import logging

def setup_logging(log_level: str = "ERROR"):
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.FileHandler("logs.txt")]
    )