"""
from os import getenv


API_ID = int(getenv("API_ID", "23031620"))
API_HASH = getenv("API_HASH", "31cb00c1cbe580394778b43105864bca")
BOT_TOKEN = getenv("BOT_TOKEN", "6865731231:AAEDdXn48VOzOf0jRo0CvxkU0VxIFsikTvg")
OWNER_ID = int(getenv("OWNER_ID", "502980590"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "502980590").split()))
MONGO_URL = mongodb+srv://altafpathan65012:<password>@cluster0.aztmome.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002155787742"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002155787742"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("23031620"))
# ------------------------------------------------
API_HASH = os.environ.get("31cb00c1cbe580394778b43105864bca)
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("6865731231:AAEDdXn48VOzOf0jRo0CvxkU0VxIFsikTvg)
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("pathansavebot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("502980590"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "502980590").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("-1002155787742"))
# ------------------------------------------------
MONGO_URL = os.environ.get("mongodb+srv://altafpathan65012:<password>@cluster0.aztmome.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("-1002155787742"))

