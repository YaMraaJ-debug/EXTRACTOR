import json
import os
import requests
from pyrogram import filters
from pyromod import listen
from Extractor import app
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode



def decrypt_data(encoded_data, key, iv):
    decoded_data = b64decode(encoded_data)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(decoded_data), AES.block_size)
    return decrypted_data.decode('utf-8')



async def neetkaka_txt(app, message):
    global cancel
    cancel = False
    raw_url = "https://neetkakajeeapi.classx.co.in/post/userLogin"
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
            "Host": "neetkakajeeapi.classx.co.in",
            "Client-Service": "Appx",
            "Auth-Key": "appxapi",
            "User-Id": userid,
            "Authorization": token
            }
    await message.reply_text("**login Successful**")
    res1 = requests.get("https://neetkakajeeapi.classx.co.in/get/mycourseweb?userid="+userid, headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    for data in b_data:
        t_name =data['course_name']
        FFF = "BATCH-ID - BATCH NAME - INSTRUCTOR"
        aa = f"**`{data['id']}`      - `{data['course_name']}`**\n\n"
        if len(f'{cool}{aa}') > 4096:
            print(aa)
            cool = ""
        cool += aa
    await message.reply_text(f'{"**You have these batches :-"}\n\n{FFF}\n\n{cool}')
    input2 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text2 = input2.text
    scraper = cloudscraper.create_scraper()
    html = scraper.get(f"https://neetkakajeeapi.classx.co.in/get/allsubjectfrmlivecourseclass?courseid={raw_text2}",headers=hdr1).content
    output0 = json.loads(html)
    subjID = output0["data"]
    subjID_data = output0["data"]
    cool = ""
    for sub in subjID:
        subjid = sub["subjectid"]
        subjname = sub["subject_name"]
        aa = f"`{subjid}` - `{subjname}`\n\n"
        cool += aa
    await message.reply_text(cool)

    input3 = await app.ask(message.chat.id, text="**Enter the Subject Id Show in above Response")
    raw_text3 = input3.text
    res3 = requests.get("https://neetkakajeeapi.classx.co.in/get/alltopicfrmlivecourseclass?courseid=" +raw_text2+"&subjectid="+raw_text3, headers=hdr1)
    b_data2 = res3.json()['data']
    vj = ""
    vp = ""
    lol = ""   
    for data in b_data2:
        t_name = data["topic_name"]
        tid = data["topicid"]
        zz = len(tid)
        BBB = f"{'**TOPIC-ID    - TOPIC     - VIDEOS**'}\n"
        hh = f'`{tid}`     - **{t_name} - ({zz})**\n'

        vj += f"{tid}&"
        vp += f"{t_name}&"

        if len(f'{lol}{hh}') > 4096:
            lol = ""

        lol += hh

    await message.reply_text(f"Batch details of **{t_name}** are:\n\n{BBB}\n\n{lol}")

    input4 = await app.ask(message.chat.id, text=f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n`{vj}`")
    raw_text4 = input4.text
    input5 = await app.ask(message.chat.id, text="**Now send the Resolution**")
    raw_text5 = input5.text

    vj = ""
    try:
        xv = raw_text4.split('&')
        for y in range(0,len(xv)):
            t =xv[y]
            hdr11 = {
                    "Host": "neetkakajeeapi.classx.co.in",
                    "Client-Service": "Appx",
                    "Auth-Key": "appxapi",
                    "User-Id": userid,
                    "Authorization": token
                    }
            res4 = requests.get("https://neetkakajeeapi.classx.co.in/get/livecourseclassbycoursesubtopconceptapiv3?topicid=" + t + "&start=-1&courseid=" + raw_text2 + "&subjectid=" + raw_text3,headers=hdr11).json()
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
                vj += msg
                
        mm = "NEET Kaka JEE"
        with open(f'{mm}.txt', 'a') as f:
            f.write(f"{vj}")
        await app.send_document(message.chat.id, document=f"{mm}.txt")
        file_path = f"{mm}.txt"
        os.remove(file_path)

    except Exception as e:
        await message.reply_text(str(e))
    await message.reply_text("Done")

