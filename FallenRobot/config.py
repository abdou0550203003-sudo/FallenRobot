class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 33686933
    API_HASH = "ce2ed30620c2070104d2ceca6577e4c7"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "ضع_هنا_رابط_Internal_Database_URL"  # من Render PostgreSQL

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://admin:Admin12345@cluster0.tav7z8i.mongodb.net/?appName=Cluster0"

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "8804157165:AAHLoV_cQ3y-Vc1lUexRoH8QDl3bf4s2QX0"

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 8941553269  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

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
