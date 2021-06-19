#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "clonebot-ui.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")

    # Comma separated User Ids
    ALLOWED = os.environ.get("ALLOWED_USERS","0")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
