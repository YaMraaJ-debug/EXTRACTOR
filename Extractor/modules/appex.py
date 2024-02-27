import json
import os
import requests
import threading
import asyncio
from pyrogram import filters
from pyrogram.types import Message
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import config
from Extractor import app

def decrypt_data(encoded_data):
    key = "638udh3829162018".encode("utf8")
    iv = "fedcba9876543210".encode("utf8")
    decoded_data = b64decode(encoded_data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(decoded_data), AES.block_size)
    return decrypted_data.decode('utf-8')

async def appex_down(app, message, hdr1, api, raw_text2, fuk, batch_name, name, prog):
    vt = ""
    try:
        xx = fuk.split('&')
        for v in range(len(xx)):
            f = xx[v]
            res3 = requests.get(f"https://{api}/get/alltopicfrmlivecourseclass?courseid=" + raw_text2 + "&subjectid=" + f, headers=hdr1)
            b_data2 = res3.json()['data']
            vp = ""
            for data in b_data2:
                tid = data["topicid"]
                vp += f"{tid}&"

            vj = ""
            try:
                xv = vp.split('&')
                for y in range(len(xv)):
                    t = xv[y]
                    res4 = requests.get(f"https://{api}/get/livecourseclassbycoursesubtopconceptapiv3?topicid=" + t + "&start=-1&courseid=" + raw_text2 + "&subjectid=" + f, headers=hdr1).json()
                    topicid = res4["data"]
                    for data in topicid:
                        type = data['material_type']
                        tid = data["Title"]
                        idid = f"{tid}"
                        if type == 'VIDEO':
                            plink = data["pdf_link"].split(':')
                            encoded_part, encrypted_part = plink
                            bp = decrypt_data(encoded_part)
                            vs = f"{bp}"

                            if data['ytFlag'] == '0':
                                dlin = [data['download_links']]
                                dlinks = [link['path'] for link in data['download_links'] if link['quality'] == "720p"]
                                for dlink in dlinks:
                                    encoded_part, encrypted_part = dlink.split(':')
                                    b = decrypt_data(encoded_part)
                                    cool2 = f"{b}"
                            elif data['ytFlag'] == '1':
                                dlink = data['video_id']
                                encoded_part, encrypted_part = dlink.split(':')
                                b = decrypt_data(encoded_part)
                                cool2 = f"{b}"

                            msg = f"{idid} : {cool2}\n{idid} : {vs}\n"
                            vj += msg

                        elif type == 'PDF':
                            plink = data["pdf_link"].split(':')
                            encoded_part, encrypted_part = plink
                            bp = decrypt_data(encoded_part)
                            vs = f"{bp}"
                            msg = f"{idid} : {vs}\n"
                            vj += msg
            except Exception as e:
                print(str(e))  
  
            vt += vj

        mm = batch_name
        cap = f"**App Name :- {name}\nBatch Name :-** `{batch_name}`"
        with open(f'{mm}.txt', 'a') as f:
            f.write(f"{vt}")
        await app.send_document(message.chat.id, document=f"{mm}.txt", caption=cap)
        await prog.delete()
        file_path = f"{mm}.txt"
        os.remove(file_path)
        await message.reply_text("Done")
    except Exception as e:
        print(str(e))



async def appex_txt(app, message, api, name):
    global cancel
    cancel = False
    raw_url = f"https://{api}/post/userLogin"
    hdr = {
        "Auth-Key": "appxapi",
        "User-Id": "-2",
        "Authorization": "",
        "User_app_category": "",
        "Language": "en",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "okhttp/4.9.1"
    }
    info = {"email": "", "password": ""}
    input1 = await app.ask(message.chat.id, text="Send **ID & Password** in this manner, otherwise, the bot will not respond.\n\nSend like this: **ID*Password**")
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    scraper = cloudscraper.create_scraper()
    res = scraper.post(raw_url, data=info, headers=hdr).content
    output = json.loads(res)
    userid = output["data"]["userid"]
    token = output["data"]["token"]
    hdr1 = {
            "Host": api,
            "Client-Service": "Appx",
            "Auth-Key": "appxapi",
            "User-Id": userid,
            "Authorization": token
            }
    await message.reply_text("**login Successful**")
    res1 = requests.get(f"https://{api}/get/mycourseweb?userid="+userid, headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    for data in b_data:
        t_name = data['course_name']
        FFF = "BATCH-ID - BATCH NAME - INSTRUCTOR"
        aa = f"**`{data['id']}`      - `{data['course_name']}`**\n\n"
        if len(f'{cool}{aa}') > 4096:
            print(aa)
            cool = ""
        cool += aa
    await message.reply_text(f"**YOU HAVE THESE BATCHES:**\n\n{FFF}\n\n{cool}")
    input2 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text2 = input2.text
    for data in b_data:
        if data['id'] == raw_text2:
            batch_name = data['course_name']
    scraper = cloudscraper.create_scraper()
    html = scraper.get(f"https://{api}/get/allsubjectfrmlivecourseclass?courseid={raw_text2}",headers=hdr1).content
    output0 = json.loads(html)
    subjID = output0["data"]
    subjID_data = output0["data"]
    cool = ""
    fuk = ""
    for sub in subjID:
        subjid = sub["subjectid"]
        fuk += f"{subjid}&"

    prog = await message.reply_text("**Extracting Videos Links Please Wait  📥 **") 
    thread = threading.Thread(target=lambda: asyncio.run(appex_down(app, message, hdr1, api, raw_text2, fuk, batch_name, name, prog)))
    thread.start()
