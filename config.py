from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "7128030034:AAFnVgvMp65otGHgEpir9PcbDD2RlTcoQOg")
OWNER_ID = int(getenv("OWNER_ID", "6280103226"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6050277919 6881758615 5783508086 6280103226").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002054493556"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002005441647"))


