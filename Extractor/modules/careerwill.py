import os
import requests
import threading
import asyncio
from pyrogram import filters
from Extractor import app
from config import SUDO_USERS


ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd"
bc_url = f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos/"
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}



async def careerdl(app, message, headers, raw_text2, raw_text3, prog, name):
    num_id = raw_text3.split('&')
    for x in range(0, len(num_id)):
        id_text = num_id[x]

        details_url = "https://elearn.crwilladmin.com/api/v3/batch-detail/" + raw_text2 + "?topicId=" + id_text
        response = requests.get(details_url, headers=headers)
        data = response.json()

        details_list = data["data"]["class_list"]
        batch_class = details_list["classes"]

        batch_class.reverse()
        fuck = ""
        try:
            for data in batch_class:
                vid_id = data['id']
                lesson_name = data['lessonName']
                lessonExt = data['lessonExt']
                url = "https://elearn.crwilladmin.com/api/v3/class-detail/" + vid_id
                lessonUrl = requests.get(url, headers=headers).json()['data']['class_detail']['lessonUrl']

                if lessonExt == 'brightcove':
                    url = "https://elearn.crwilladmin.com/api/v3/livestreamToken"
                    params = {
                        "base": "web",
                        "module": "batch",
                        "type": "brightcove",
                        "vid": vid_id
                    }

                    response = requests.get(url, headers=headers, params=params)
                    stoken = response.json()["data"]["token"]

                    link = bc_url + lessonUrl + "/master.m3u8?bcov_auth=" + stoken
                    fuck += f"{lesson_name}: {link}\n"

                elif lessonExt == 'youtube':
                    link = "https://www.youtube.com/embed/" + lessonUrl
                    fuck += f"{lesson_name}: {link}\n"

            if '/' in name:
                name1 = name.replace("/", "")
            else:
                name1 = name
            with open(f"{name1}.txt", 'a') as f:
                f.write(f"{fuck}")

        except Exception as e:
            await message.reply_text(str(e))
    c_txt = f"**App Name: CareerWill\nBatch Name: `{name}`**"
    await app.send_document(message.chat.id, document=f"{name1}.txt", caption=c_txt)
    await prog.delete()
    os.remove(f"{name1}.txt")



async def career_will(app, message):
    try:
        input1 = await app.ask(message.chat.id, text="**Send ID & Password in this manner otherwise bot will not respond.\n\nSend like this:-  ID*Password\n\n OR Send Your Token**")
        login_url = "https://elearn.crwilladmin.com/api/v3/login-other"
        raw_text = input1.text
        if "*" in raw_text:
            headers = {
                "Host": "elearn.crwilladmin.com",
                "origintype": "web",
                "accept": "application/json",
                "content-type": "application/json; charset=utf-8",
                "accept-encoding": "gzip",
                "user-agent": "okhttp/3.9.1"
            }

            email, password = raw_text.split("*")
            data = {
                "deviceType": "web",
                "password": password,
                "deviceModel": "chrome",
                "deviceVersion": "Chrome+119",
                "email": email
            }

            response = requests.post(login_url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error if the request was unsuccessful
            token = response.json()["data"]["token"]
            await message.reply_text(f"**Login Successful**\n\n`{token}`")
        else:
            token = raw_text
    except Exception as e:
        await message.reply_text(f"An error occurred during login: {e}")
        return

    headers = {
        "Host": "elearn.crwilladmin.com",
        "origintype": "web",
        "usertype": "2",
        "token": token,
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.9.1"
    }

    await input1.delete(True)
    batch_url = "https://elearn.crwilladmin.com/api/v3/my-batch"
    response = requests.get(batch_url, headers=headers)
    data = response.json()
    topicid = data["data"]["batchData"]

    FFF = "**BATCH-ID     -     BATCH NAME**\n\n"
    for data in topicid:
        FFF += f"`{data['id']}`     -    **{data['batchName']}**\n\n"

    await message.reply_text(f"**HERE IS YOUR BATCH**\n\n{FFF}")
    input2 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text2 = input2.text
    topic_url = "https://elearn.crwilladmin.com/api/v3/batch-topic/" + raw_text2 + "?type=class"
    response = requests.get(topic_url, headers=headers)
    topic_data = response.json()
    batch_data = topic_data['data']['batch_topic']
    name = topic_data["data"]["batch_detail"]["name"]

    BBB = "**TOPIC-ID - TOPIC**\n\n"
    id_num = ""
    for data in batch_data:
        topic_id = data["id"]
        topic_name = data["topicName"]
        id_num += f"{topic_id}&"
        BBB += f"`{topic_id}` -  **{topic_name}** \n\n"

    await message.reply_text(f"**Batches details of {name}**\n\n{BBB}")
    input3 = await app.ask(message.chat.id, text=f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n`{id_num}`")
    raw_text3 = input3.text

    prog = await message.reply_text("**Extracting Videos Links Please Wait  📥 **")

    try:
        thread = threading.Thread(target=lambda: asyncio.run(careerdl(app, message, headers, raw_text2, raw_text3, prog, name)))
        thread.start()

    except Exception as e:
        await message.reply_text(str(e))
