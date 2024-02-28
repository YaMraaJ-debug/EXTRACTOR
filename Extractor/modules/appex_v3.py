import json
import os
import requests
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode
from pyrogram import filters
from Extractor import app


async def decrypt_data(encoded_data):
    key = "638udh3829162018".encode("utf8")
    iv = "fedcba9876543210".encode("utf8")
    decoded_data = b64decode(encoded_data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(decoded_data), AES.block_size)
    return decrypted_data.decode('utf-8')



async def course_content(app, api, message, raw_text2, parent_Id, hdr1):
    try:
        scraper = cloudscraper.create_scraper()
        html = scraper.get(f"https://{api}/get/folder_contentsv2?course_id={raw_text2}&parent_id={parent_Id}", headers=hdr1).content
        output = json.loads(html)
        data_list = output.get('data', [])
        vj = ""
        for data in data_list:
            if data['material_type'] == 'FOLDER':
                id = data["id"]
                await course_content(app, api, message, raw_text2, id, hdr1)
            elif data['material_type'] == 'VIDEO':
                tid = data.get("Title")
                plink = data.get("pdf_link", "").split(':')
                if len(plink) == 2:
                    encoded_part, encrypted_part = plink
                    vs = decrypt_data(encoded_part)
                if data.get('ytFlag') == 0:
                    dlink = next((link['path'] for link in data.get('download_links', []) if link.get('quality') == "720p"), None)
                    if dlink:
                        parts = dlink.split(':')
                        if len(parts) == 2:   
                            encoded_part, encrypted_part = parts
                            cool2 = decrypt_data(encoded_part)
                        else:
                            print(f"Unexpected format: {plink}\n{tid}")
                elif data.get('ytFlag') == 1:
                    dlink = data.get('file_link')
                    if dlink:
                        encoded_part, encrypted_part = dlink.split(':')
                        cool2 = decrypt_data(encoded_part)
                    else:
                        print(f"Missing video_id for {tid}")
                else:
                    print("Unknown ytFlag value")
                msg = f"{tid} : {cool2}\n{tid} : {vs}\n"
                vj += msg

            elif data['material_type'] == 'PDF':
                tid = data.get("Title")
                plink = data.get("pdf_link", "").split(':')
                if len(plink) == 2:
                    encoded_part, encrypted_part = plink
                    vs = decrypt_data(encoded_part)
                msg = f"{tid} : {vs}\n"
                vj += msg

        mm = "mm"
        cap = f"**App Name :- ff\nBatch Name :-** `ff`"
        with open(f'{mm}.txt', 'a') as f:
            f.write(f"{vj}")
        await app.send_document(message.chat.id, document=f"{mm}.txt", caption=cap)
        await prog.delete()
        file_path = f"{mm}.txt"
        os.remove(file_path)
        await message.reply_text("Done")

    except Exception as e:
        print(str(e))
        await message.reply_text("An error occurred. Please try again later.")


async def appex_v3_txt(app, message, api, name):
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
    res1 = requests.get(f"https://{api}/get/get_all_purchases?userid="+userid+"&item_type=10", headers=hdr1)
    b_data = res1.json().get('data', [])
    
    FFF = "BATCH-ID - BATCH NAME\n\n"
    for data in b_data:
        cdatas = data['coursedt']
        for cdata in cdatas:      
            FFF += f"**`{cdata['id']}`      - `{cdata['course_name']}`**\n\n"
            
    await message.reply_text(f"**YOU HAVE THESE BATCHES:\n\n{FFF}")
    input2 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text2 = input2.text
    scraper = cloudscraper.create_scraper()
    html = scraper.get(f"https://{api}/get/folder_contentsv2?course_id={raw_text2}&parent_id=-1", headers=hdr1).content
    output0 = json.loads(html)
    parent_Id = output0['data'][0]['id']
    await course_content(app, api, message, raw_text2, parent_Id, hdr1)
