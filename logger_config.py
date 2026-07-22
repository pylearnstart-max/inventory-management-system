import logging

logger = logging.getLogger("inventory")

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("inventory.log")

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)