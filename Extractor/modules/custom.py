from pyrogram import filters
from Extractor import app
#from pyromod import listen
from config import SUDO_USERS
#from Extractor.core.multi_func import apex_accounts

import json
import os
import requests
from pyrogram import listen
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

def decode(tn):
    key = "638udh3829162018".encode("utf8")
    iv = "fedcba9876543210".encode("utf8")
    ciphertext = bytearray.fromhex(b64decode(tn.encode()).hex())
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    url = plaintext.decode('utf-8')
    return url

async def apex_accounts(_, message, apex_api):
    global cancel
    cancel = False
    editable = await message.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")

    rwa_url = f"{apex_api}/post/userLogin"
    hdr = {"Auth-Key": "appxapi",
           "User-Id": "-2",
           "Authorization": "",
           "User_app_category": "",
           "Language": "en",
           "Content-Type": "application/x-www-form-urlencoded",
           "Content-Length": "233",
           "Accept-Encoding": "gzip, deflate",
           "User-Agent": "okhttp/4.9.1"
          }
    info = {"email": "", "password": ""}

    input1 = await _.listen(editable.chat.id)
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    scraper = cloudscraper.create_scraper()
    res = scraper.post(rwa_url, data=info, headers=hdr).content
    output = json.loads(res)
    
    userid = output["data"]["userid"]
    token = output["data"]["token"]
    api_url = apex_api
    clean_url = api_url.replace("https://", "").replace("http://", "")
    hdr1 = {
        "Host": clean_url,
        "Client-Service": "Appx",
        "Auth-Key": "appxapi",
        "User-Id": userid,
        "Authorization": token
        }
    
    await editable.edit("**login Successful**")
    
    res1 = requests.get(f"{apex_api}/get/mycourse?userid="+userid, headers=hdr1)
    batch_data = res1.json()['data']
    
    FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**"
    for data in batch_data:
        title_name = data['course_name']
        FFF += f" {data['id']}  -  **{data['course_name']}**\n\n"
                    
    await editable.edit(f"YOU HAVE THIS {title_name}\n\n{FFF}")
    
    editable1 = await message.reply_text("**Now send the Batch ID to Download**")
    input2 = await _.listen(editable1.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    await editable1.delete(True)
    
    html = scraper.get(f"{apex_api}/get/course_by_id?id=" + raw_text2,headers=hdr1).json()
    course_title = html["data"][0]["course_name"]
    scraper = cloudscraper.create_scraper()
    html = scraper.get(f"{apex_api}/get/allsubjectfrmlivecourseclass?courseid=" + raw_text2,headers=hdr1).content
    output0 = json.loads(html)
    subjID = output0["data"]
    
    cool = "CHOOSE YOUR TOPIC ID\n\n"
    sub_id = ""
    for sub in subjID:
        subjid = sub["subjectid"]
        idid = f"{subjid}&"
        subjname = sub["subject_name"]
        cool += f"*{subjid}*  - **{subjname}**\n\n"
        sub_id += idid
      
    await editable.edit(cool)
    editable1 = await message.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n`{sub_id}`")
    input3 = await _.listen(editable1.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    await editable1.delete(True)
    prog = await editable.edit("**Extracting Videos Links Please Wait  📥 **")
  
    mm_url = api_url.replace("https://", "").replace("http://", "")
    mm_name = mm_url.split('.')[0].replace("api", "")
    try:
        mm = f"{mm_name}"
        xv = raw_text3.split('&')
        for y in range(0,len(xv)):
            raw_text3 = xv[y]
            res3 = requests.get(f"{apex_api}/get/alltopicfrmlivecourseclass?courseid={raw_text2}&subjectid={raw_text3}", headers=hdr1)
            b_data2 = res3.json()['data']
            for data in b_data2:
                t_name = (data["topic_name"])
                tid = (data["topicid"])
                print(tid, t_name)
                hdr11 = {
                        "Host": clean_url,
                        "Client-Service": "Appx",
                        "Auth-Key": "appxapi",
                        "User-Id": userid,
                        "Authorization": token
                        }
                        
                res4 = requests.get(f"{apex_api}/get/livecourseclassbycoursesubtopconceptapiv3?courseid={raw_text2}&subjectid={raw_text3}&topicid={tid}&start=-1",headers=hdr11).json()
                topicid = res4["data"]
                print(topicid)
                for data in topicid:
                    tid = (data["Title"])
                    with open(f'{mm} - {title_name}.txt', 'a') as f:
                        if len(data["download_link"]) > 0:
                            tn = (data["download_link"])
                            try:
                                url = decode(tn)
                            except Exception as e:
                                print("Error decoding download link:", e)
                                continue
                            mtext = f"{tid}:{url}\n"
                            f.write(mtext)
                        if len(data["pdf_link"]) > 0:
                            tn = (data["pdf_link"])
                            try:
                                url = decode(tn)
                            except Exception as e:
                                print("Error decoding PDF link:", e)
                                continue
                            mtext = f"{tid}:{url}\n"
                            f.write(mtext)
        await prog.delete(True)        
        await message.reply_document(f"{mm} - {course_title}.txt", caption=f"`{mm} - {course_title}`")
        os.remove(f"{mm} - {course_title}.txt")
        await editable.delete(True)
    except Exception as e:
        await message.reply_text(str(e))



@app.on_message(filters.command(["custom"]) & filters.user(SUDO_USERS))
async def custom_api(_, message):
  
    editable = await message.reply_text("Send your custom api : like :- https://rksirofficialapi.classx.co.in")
    input1: message = await _.listen(editable.chat.id)
    apex_api = input1
    await apex_accounts(_, message, apex_api)
    



