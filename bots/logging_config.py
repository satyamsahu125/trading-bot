import logging
import logging.config
import os

os.makedirs("logs" ,exist_ok=True)


logging.basicConfig(
    filename  = "logs/bots.log",
    level = logging.INFO,
    format = "%(asctime)s | %(levelname)s  | %(message)s"
)

logger = logging.getLogger(__name__)