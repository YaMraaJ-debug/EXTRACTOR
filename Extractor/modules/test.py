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
bc_url = (f"https://edge.api.brightcove.com/playback/v1/accounts/{ACCOUNT_ID}/videos")
bc_hdr = {"BCOV-POLICY": BCOV_POLICY}


@app.on_message(filters.command(["tw"]) & filters.user(SUDO_USERS))
async def careerwill_account(_, message):
    global cancel
    cancel = False


    editable = await message.reply_text("Send **TOKEN** like This this:-  **TOKEN**" )
    input1: message = await _.listen(editable.chat.id)
    raw_text = input1.text
    token = raw_text
    print(token)
    headers = {
    "Host": "elearn.crwilladmin.com",
    "origintype": "web",
    "usertype": "2",
    "token": raw_text,
    "accept-encoding": "gzip",
    "user-agent": "okhttp/3.9.1"
}

      
        
    batch_url = "https://elearn.crwilladmin.com/api/v3/my-batch"
    response = requests.get(batch_url, headers=headers)
    data = response.json()
    print(data)
    topicid = data["data"]["batchData"]
    
    FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**\n\n"
    for data in topicid:       
        FFF += f"`{data['id']}`  - `{data['batchName']}` \n{data['instructorName']}\n\n"
       
    await editable.edit(f"HERE IS YOUR BATCH\n\n{FFF}")
    editable1= await message.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await _.listen(editable1.chat.id)
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
    editable = await message.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n`{id_num}`")    
    input3 : message = await _.listen(editable.chat.id)
    raw_text3 = input3.text

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
            
            batch_class.reverse()
            count = 1
            
            try:
                for data in batch_class:
                    vid_id = data["id"]
                    lesson_name = data["lessonName"]
                    video_link = data["lessonUrl"]
                    
                    if vid_id.startswith("62"):
                        """
                        try:
                            html5 = requests.get("https://web.careerwill.com/api/v3/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl = json.loads(html5)
                            stoken = surl["data"]["token"]
                                           
                            link = (video_url+"&bcov_auth="+stoken)       
                        except Exception as e:
                            print(str(e))
                        """
                    
                    elif vid_id.startswith("63"):
                        """
                        try:
                            html8 = s.get("https://web.careerwill.com/api/v3/livestreamToken?type=brightcove&vid="+vidid+"&token="+token).content
                            surl1 = json.loads(html8)
                            stoken1 = surl1["data"]["token"]
                            
                            link = (video_url1+"&bcov_auth="+stoken1)  
                        except Exception as e:
                            print(str(e))
                        """
                    
                    else:
                        link=("https://www.youtube.com/embed/"+video_link)
            
                    with open(f"{batch_name}{name}.txt", 'a') as f:
                        f.write(f"{lesson_name}\n{link}\n")
                    
            except Exception as e:
                await message.reply_text(str(e))
            c_txt = f"App: `CareerWill`\n`{batch_name}`"
        await message.reply_document(f"{batch_name}{name}.txt", caption=c_text)
        os.remove(f"{batch_name}{name}.txt")
    except Exception as e:
        await message.reply_text(str(e))


