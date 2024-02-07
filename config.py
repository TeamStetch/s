import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6822435599:AAFRKwqBMyRblFCDuZdZQsEdYG5Qui4QDjU")

    APP_ID = int(os.environ.get("APP_ID", 14837825))

    API_HASH = os.environ.get("API_HASH", "0ed849f5e7ab2df61d969317de2ca64c")
