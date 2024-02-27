import datetime
from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

mongo = MongoCli(MONGO_URL)
db = mongo.premium
db = db.premium_db


async def has_premium_access(user_id):
    user_data = await db.users.find_one({"id": user_id})
    if user_data:
        expiry_time = user_data.get("expiry_time")
        if expiry_time is None:
            return False
        elif isinstance(expiry_time, datetime.datetime) and datetime.datetime.now() <= expiry_time:
            return True
        else:
            await db.users.update_one({"id": user_id}, {"$set": {"expiry_time": None}})
    return False

async def update_one(filter_query, update_data):
    try:
        result = await db.users.update_one(filter_query, update_data)
        return result.matched_count == 1
    except Exception as e:
        print(f"Error updating document: {e}")
        return False

async def remove_premium_access(user_id):
    return await update_one({"id": user_id}, {"$set": {"expiry_time": None}})

async def check_trial_status(user_id):
    user_data = await db.users.find_one({"id": user_id})
    if user_data:
        return user_data.get("has_free_trial", False)
    return False

async def give_free_trial(user_id):
    seconds = 5 * 60         
    expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
    user_data = {"id": user_id, "expiry_time": expiry_time, "has_free_trial": True}
    await db.users.update_one({"id": user_id}, {"$set": user_data}, upsert=True)

