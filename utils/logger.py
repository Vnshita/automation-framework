import logging
import os
from datetime import datetime


class Logger:

    @staticmethod
    def get_logger(name):
        os.makedirs("logs", exist_ok=True)

        log_file = f"logs/test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        return logger