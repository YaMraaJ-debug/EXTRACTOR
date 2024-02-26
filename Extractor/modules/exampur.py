import json
import os
import requests
from pyrogram import filters
from pyrogram.types import Message
from pyromod import listen
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
import config
from TXT import app


def decrypt_data(encoded_data, key, iv):
    decoded_data = b64decode(encoded_data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(decoded_data), AES.block_size)
    return decrypted_data.decode('utf-8')



async def appexampur_txt(app, message):
    global cancel
    cancel = False
    raw_url = "https://exampurapi.classx.co.in/post/userLogin"
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
            "Host": "exampurapi.classx.co.in",
            "Client-Service": "Appx",
            "Auth-Key": "appxapi",
            "User-Id": userid,
            "Authorization": token
            }
    await message.reply_text("**login Successful**")
    res1 = requests.get(f"https://exampurapi.classx.co.in/get/get_all_purchases?userid="+userid+"&item_type=10", headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    for data in b_data:
        cdatas = data['coursedt']
        for cdata in cdatas:
            t_name = cdata['course_name']
            FFF = "BATCH-ID - BATCH NAME"
            aa = f"**`{cdata['id']}`      - `{cdata['course_name']}`**\n\n"
            if len(f'{cool}{aa}') > 4096:
                print(aa)
                cool = ""
            cool += aa
            btch = cdata['course_name']
    await message.reply_text(f'{"**You have these batches :-"}\n\n{FFF}\n\n{cool}')
    input2 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text2 = input2.text
    scraper = cloudscraper.create_scraper()
    html = scraper.get(f"https://exampurapi.classx.co.in/get/folder_contentsv2?course_id={raw_text2}&parent_id=-1", headers=hdr1).content
    output0 = json.loads(html)
    parent_Id = output0['data'][0]['id']
    scraper2 = cloudscraper.create_scraper()
    html2 = scraper2.get(f"https://exampurapi.classx.co.in/get/folder_contentsv2?course_id={raw_text2}&parent_id={parent_Id}", headers=hdr1).content
    output1 = json.loads(html2)
    subjID = output1['data']
    cool = ""
    for sub in subjID:
        subjid = sub["id"]
        subjname = sub["Title"]
        aa = f"`{subjid}` - `{subjname}`\n\n"
        cool += aa
    await message.reply_text(cool)
    input3 = await app.ask(message.chat.id, text="**Enter the Subject Id Show in above Response**")
    raw_text3 = input3.text
    try:
        scraper3 = cloudscraper.create_scraper()
        html3 = scraper3.get(f"https://exampurapi.classx.co.in/get/folder_contentsv2?course_id={raw_text2}&parent_id={raw_text3}", headers=hdr1).content
        output2 = json.loads(html3)
        b_data2 = output2['data']
        vj = ""
        lol = ""   
        for data in b_data2:
            if data['material_type'] == 'FOLDER':
                t_name = data["Title"]
                tid = data["id"]
                zz = data['videos_count']
                BBB = f"{'**TOPIC-ID    - TOPIC     - VIDEOS**'}\n"
                hh = f'`{tid}`     - **{t_name} - ({zz})**\n'
                vj += f"{tid}&"

                if len(f'{lol}{hh}') > 4096:
                    lol = ""
                lol += hh

        await message.reply_text(f"Batch details of **{t_name}** are:\n\n{BBB}\n\n{lol}")
        input4 = await app.ask(message.chat.id, text=f"**Now send the **Subject Ids** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n`{vj}`")
        raw_text4 = input4.text
    except:
        raw_text4 = raw_text3
    input5 = await app.ask(message.chat.id, text="**Now send the Resolution**")
    raw_text5 = input5.text

    vj = ""
    try:
        xv = raw_text4.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
            hdr11 = {
                    "Host": "exampurapi.classx.co.in",
                    "Client-Service": "Appx",
                    "Auth-Key": "appxapi",
                    "User-Id": userid,
                    "Authorization": token
                    }
            res4 = requests.get("https://exampurapi.classx.co.in/get/folder_contentsv2?course_id="+raw_text2+"&parent_id="+t, headers=hdr11).json()
            topicid = res4["data"]

            for data in topicid:
                tids = (data["Title"])
                plinks = [data["pdf_link"]]
                dlin = [data['download_links']]
                key = "638udh3829162018".encode("utf8")
                iv = "fedcba9876543210".encode("utf8")

                idid = f"{tids}"
                if plinks:
                    for plink in plinks:
                        parts = plink.split(':')
                        if len(parts) == 2:
                            encoded_part, encrypted_part = parts
                            bp = decrypt_data(encoded_part, key, iv)
                        else:
                            print(f"Unexpected format: {plink}")
                        vs = f"{bp}"
                else:
                    vs = "NO PDF LINK"
                if dlin:
                    dlinks = [link['path'] for link in data['download_links'] if link['quality'] == f"{raw_text5}p"]
                    for dlink in dlinks:
                        parts = dlink.split(':')
                        if len(parts) == 2:
                            encoded_part, encrypted_part = parts
                            b = decrypt_data(encoded_part, key, iv)
                        else:
                            print(f"Unexpected format: {dlink}")
                        cool2 = f"{b}"
                else:
                    cool2 = "NO DOWNLOAD LINK"

                msg = f"{idid} : {cool2}\n{idid} : {vs}\n\n"
#                msg = f"{idid} : {cool2}\n\n"
                vj += msg
                
        mm = "Exampur"
        with open(f'{mm}.txt', 'a') as f:
            f.write(f"{vj}")
        await app.send_document(message.chat.id, document=f"{mm}.txt")
        file_path = f"{mm}.txt"
        os.remove(file_path)

    except Exception as e:
        await message.reply_text(str(e))
    await message.reply_text("Done")


