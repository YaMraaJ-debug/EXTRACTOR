import datetime
from config import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

mongo = MongoCli(MONGO_URL)
db = mongo.premium
db = db.premium_db


async def add_premium(user_id, expire_date):
    await db.insert_one({"_id": user_id, "expire_date": expire_date})


async def remove_premium(user_id):
    await db.delete_one({"_id": user_id})


async def check_premium(user_id):
    x = await t.find_one({"_id": user_id})
    return x["_id"]


async def premium_users():
    async for data in db.find():
        return data["_id"]

