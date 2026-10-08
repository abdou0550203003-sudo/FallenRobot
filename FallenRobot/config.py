import os


class Config(object):
    LOGGER = True

    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    CASH_API_KEY = ""
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    EVENT_LOGS = ()
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "")
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"
    SUPPORT_CHAT = ""
    TOKEN = os.environ.get("TOKEN", "")
    TIME_API_KEY = ""
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))
    LOG_CHANNEL = ""

    BL_CHATS = []
    DRAGONS = []
    DEV_USERS = []
    DEMONS = []
    TIGERS = []
    WOLVES = []

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
