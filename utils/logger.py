import logging

import logging
import os

LOG_DIR = "Logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:  # Prevent adding multiple handlers
        logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler(os.path.join(LOG_DIR, "test.log"))
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.propagate = False
    return logger












    # @staticmethod
    # def loggen():
    #     log_dir = os.path.join(os.getcwd(), "Logs")
    #     os.makedirs(log_dir, exist_ok=True)
    #
    #     logfile = os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    #
    #     logging.basicConfig(
    #         filename=logfile,
    #         format='%(asctime)s - %(levelname)s - %(message)s',
    #         datefmt='%Y-%m-%d %H:%M:%S',
    #         level=logging.INFO
    #     )
    #     logger = logging.getLogger()
    #     return logger
