import json
import os
import requests
from pyrogram import filters
from Extractor import app
from config import SUDO_USERS



async def en_login(app, message):
    input1 = await app.ask(message.chat.id, text="**Send ID & Password in this manner otherwise bot will not respond.\n\nSend like this:-  ID*Password**")

    login_url = "https://khanglobalstudies.com/api/login-with-password"
    raw_text = input1.text

    headers = {
        "Host": "khanglobalstudies.com",
        "content-type": "application/x-www-form-urlencoded",
        "content-length": "36",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.9.1"
    }

    data = {
        "password": "",
        "phone": ""
    }
    data["email"] = raw_text.split("*")[0]
    data["password"] = raw_text.split("*")[1]
    await input1.delete(True)

    response = requests.post(login_url, headers=headers, data=data)
    if response.status_code == 200:
        data = response.json()
        token = data["token"]
        await message.reply_text("**Login Successful**")
    else:
        await message.reply_text("Go back to response")

    headers = {
        "Host": "khanglobalstudies.com",
        "authorization": f"Bearer {token}",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.9.1"
    }

  
