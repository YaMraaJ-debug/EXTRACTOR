from os import getenv


API_ID = int(getenv("API_ID", "18618422"))
API_HASH = getenv("API_HASH", "f165b1caec3cfa4df943fe1cbe82d22a")
BOT_TOKEN = getenv("BOT_TOKEN", "6331627404:AAGa6ICDHJGzgcO0niT8se0ZL0B4dym_UxA")
OWNER_ID = int(getenv("OWNER_ID", "6050277919"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6050277919 2112898623").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://mohitag24082006:yox8Q1a9P5aLcAzK@cluster0.yafxbo4.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002034072106"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002034072106"))
