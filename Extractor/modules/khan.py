import json
import os
import requests
from pyrogram import filters
from Extractor import app
from config import SUDO_USERS



async def khan_login(app, message):
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
    data["phone"] = raw_text.split("*")[0]
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

    course_url = "https://khanglobalstudies.com/api/user/v2/courses"
    response = requests.get(course_url, headers=headers)

    data = response.json()
    courses = [(course['id'], course['title']) for course in data]

    FFF = "BATCH-ID  - BATCH-NAME\n\n"

    for course_id, course_title in courses:
        FFF += f"`{course_id}` - **{course_title}**\n\n"

    await message.reply_text(FFF)

    input3 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")    
    raw_text3 = input3.text
    for course in data:
        if course['id'] == raw_text3:
            batch_name = course['title']
        else:
            batch_name = "KHAN-SIR"
    url = "https://khanglobalstudies.com/api/user/courses/"+raw_text3+"/v2-lessons"
    response2 = requests.get(url, headers=headers)
    
    msg = await message.reply_text("**Prepared your course id**")
    bat_id = ""
    for data in response2.json():
        baid = f"{data['id']}&"
        bat_id += baid
          
    await msg.edit_text("**Done your course id\n Now Extracting your course**")
    full = ""
    try:
        xv = bat_id.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
            try:
                url = "https://khanglobalstudies.com/api/lessons/"+t  
                response = requests.get(url, headers=headers)
                data = response.json()
                
        
                videos = data.get('videos', [])
                fuck = ""
                for video in videos: 
                    class_title = video.get('name')
                    class_url = video.get('video_url')
                    fuck += f"{class_title}: {class_url}\n"
        
                full += fuck
            except Exception as e:
                print(str(e))
                pass
                
        with open(f"{batch_name}.txt", 'a') as f:
            f.write(f"{full}")
        
        c_txt = f"**App Name: Khan-Sir\nBatch Name:** `{batch_name}`"
        await message.reply_document(document=f"{batch_name}.txt", caption=c_txt)
        os.remove(f"{batch_name}.txt")

    except Exception as e:
        await message.reply_text(str(e))
