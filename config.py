from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "6373343474:AAHONd62VYjN69252RNhWDHy6ybEPi-cDEc")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6280048819 6691393517 6050277919 2015585738").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")


