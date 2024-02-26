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



ACCOUNT_ID = "6206459123001"
BCOV_POLICY = "BCpkADawqM1474MvKwYlMRZNBPoqkJY-UWm7zE1U769d5r5kqTjG0v8L-THXuVZtdIQJpfMPB37L_VJQxTKeNeLO2Eac_yMywEgyV9GjFDQ2LTiT4FEiHhKAUvdbx9ku6fGnQKSMB8J5uIDd"
bc_url = f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos/"
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}



@app.on_message(filters.command(["cw"]))
async def career_will(_, message):
    try:
        input1 = await app.ask(message.chat.id, text="Send ID & Password in this manner otherwise bot will not respond.\n\nSend like this:-  ID*Password")
        login_url = "https://elearn.crwilladmin.com/api/v3/login-other"
        raw_text = input1.text
        s = requests.Session()
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

            response = s.post(login_url, headers=headers, json=data)
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
    print(data)
    topicid = data["data"]["batchData"]
    
    FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**\n\n"
    for data in topicid:       
        FFF += f"`{data['id']}`  - `{data['batchName']}` \n{data['instructorName']}\n\n"
       
    await message.reply_text(f"HERE IS YOUR BATCH\n\n{FFF}")
    input2 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text2 = input2.text
    topic_url = "https://elearn.crwilladmin.com/api/v3/batch-topic/"+raw_text2+"?type=class"
    response = requests.get(topic_url, headers=headers)
    topic_data = response.json()
    print(data)
    batch_data = topic_data['data']['batch_topic']
    name = topic_data["data"]["batch_detail"]["name"]
    
    BBB = "**TOPIC-ID - TOPIC - VIDEOS**\n\n"
    id_num = ""
    for data in batch_data:
        topic_id = data["id"]
        topic_name = data["topicName"]
        id_num += f"{topic_id}&"
        BBB += f"{topic_id} -  {topic_name} \n\n"

    await message.reply_text(f"Batches details of {name}\n\n{BBB}")
    input3 = await app.ask(message.chat.id, text=f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n`{id_num}`")    
    raw_text3 = input3.text
    
    prog = await message.reply_text("**Extracting Videos Links Please Wait  📥 **")

    try:
        num_id = raw_text3.split('&')
        for x in range(0,len(num_id)):
            id_text = num_id[x]
        
            details_url = "https://elearn.crwilladmin.com/api/v3/batch-detail/"+raw_text2+"?topicId="+id_text
            response = requests.get(details_url, headers=headers)
            data = response.json()
            
            details_list = data["data"]["class_list"]
            batch_name = details_list["batchName"]
            batch_descript = details_list["batchDescription"]
            batch_class = details_list["classes"]
                      
            try:
                for data in batch_class:
                    vid_id = data["id"]
                    lesson_name = data["lessonName"]
                    video_link = data["lessonUrl"]
                    
                    
                    if video_link.startswith("62"):             
                        url = "https://elearn.crwilladmin.com/api/v5/livestreamToken"
                        params = {
                               "base": "web",
                               "module": "batch",
                               "type": "brightcove",
                               "vid": vid_id
                            }

                        response = requests.get(url, headers=headers, params=params)
                        stoken = response.json()["data"]["token"]

                        link = bc_url + video_link + "/master.m3u8?bcov_auth=" + stoken
                           

                    elif video_link.startswith("63"):             
                        url = "https://elearn.crwilladmin.com/api/v5/livestreamToken"
                        params = {
                               "base": "web",
                               "module": "batch",
                               "type": "brightcove",
                               "vid": vid_id
                            }

                        response = requests.get(url, headers=headers, params=params)
                        stoken = response.json()["data"]["token"]
                        
                        link = bc_url + video_link + "/master.m3u8?bcov_auth=" + stoken
                        
                        
                    else:
                        link = "https://www.youtube.com/embed/"+video_link
            
                with open(f"{batch_name}{name}.txt", 'a') as f:
                    f.write(f"{lesson_name}: {link}\n")
                    
            except Exception as e:
                await message.reply_text(str(e))
            c_txt = f"**App Name: CareerWill\n{batch_name}**"
        await message.reply_document(document=f"{batch_name}{name}.txt", caption=c_txt)
        await prog.delete()
        os.remove(f"{batch_name}{name}.txt")
    except Exception as e:
        await message.reply_text(str(e))







        

