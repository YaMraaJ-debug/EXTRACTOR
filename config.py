"""
from os import getenv


API_ID = int(getenv("API_ID", "23031620"))
API_HASH = getenv("API_HASH", "31cb00c1cbe580394778b43105864bca")
BOT_TOKEN = getenv("BOT_TOKEN", "7035220759:AAEQcpQXZOd8aWgJkXQMmUzoeFuU_ufYego")
OWNER_ID = int(getenv("OWNER_ID", "502980590"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "502980590").split()))
MONGO_URL = mongodb+srv://altafpathan65012:<password>@cluster0.aztmome.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002155787742"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002155787742"))

"""
#




# --------------M----------------------------------

import os
import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("APP_ID", 23031620))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "502980590"))
# ------------------X------------------------------
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "502980590").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002155787742"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002155787742"))
