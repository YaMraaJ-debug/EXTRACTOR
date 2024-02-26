import json
import os
import requests
from pyrogram import filters
from pyromod import listen
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
from Extractor import app
from config import SUDO_USERS

@app.on_message(filters.command(["test"]))
async def khan_login(_, message):
    editable = await message.reply_text("Send ID & Password in this manner otherwise bot will not respond.\n\nSend like this:-  ID*Password")

    login_url = "https://khanglobalstudies.com/api/login-with-password"
    input1 = await _.listen(editable.chat.id)
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
    data["phone"] = raw_text.split("*")[0]
    data["password"] = raw_text.split("*")[1]
    await input1.delete(True)

    response = requests.post(login_url, headers=headers, data=data)
    if response.status_code == 200:
        data = response.json()
        token = data["token"]
        await editable.edit("**Login Successful**")
    else:
        await message.reply_text("Go back to response")

    headers = {
        "Host": "khanglobalstudies.com",
        "authorization": f"Bearer {token}",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.9.1"
    }

    course_url = "https://khanglobalstudies.com/api/user/v2/courses"
    response = requests.get(course_url, headers=headers)

    data = response.json()
    mm = "Khan-Sir"
    courses = [(course['id'], course['title']) for course in data]

    FFF = "BATCH-ID  - BATCH-NAME\n\n"

    for course_id, course_title in courses:
        FFF += f"{course_id} - {course_title}\n\n"

    await editable.edit(FFF)

    editable1 = await message.reply_text("Now send the Batch ID to Download")    
    input3: message = await _.listen(editable1.chat.id)
    raw_text3 = input3.text

    url = "https://khanglobalstudies.com/api/user/courses/"+raw_text3+"/v2-lessons"
    response2 = requests.get(url, headers=headers)
    
    msg = await message.reply_text("Prepared your course id")
    bat_id = ""
    for data in response2.json():
        baid = f"{data['id']}&"
        bat_id +=baid
        
    print(bat_id)    
    await msg.edit_text("Done your course id\n Now Extracting your course")
    xv = bat_id.split('&')
    for y in range(0,len(xv)):
        t =xv[y].strip()
        
        url = "https://khanglobalstudies.com/api/lessons/"+t  
        response = requests.get(url, headers=headers)
        data = response.json()
        
        for dat in data:
            try:
                class_title = dat["name"]
                class_url = dat["video_url"]
                with open(f"{mm}-test.txt", 'a') as f:
                    f.write(f"{class_title}: {class_url}\n")
            except KeyError:
                pass
    await message.reply_document(f"{mm}-test.txt")
    await msg.delete()

