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
    data["username"] = raw_text.split("*")[0]
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
    courses = [(course['id'], course['title']) for course in data]

    FFF = "BATCH-ID  - BATCH-NAME\n"

    for course_id, course_title in courses:
        FFF += f"{course_id} - {course_title}\n"

    await editable.edit(FFF)

    editable1 = await message.reply_text("Now send the Batch ID to Download")
    
    input3: message = await bot.listen(editable1.chat.id)
    raw_text3 = input3.text
    response2 = s.get(f'https://api.penpencil.xyz/v3/batches/{raw_text3}/details', headers=headers).json()["data"]
    response3 = s.get(f'https://api.penpencil.xyz/v3/batches/{raw_text3}/details', headers=headers).json()["data"]["subjects"]
   
    batch = response2['name']
    vj=""
    for data in response3:
        tids = data['_id']
        idid=f"{tids}&"
        if len(f"{vj}{idid}")>4096:
            vj = ""
        vj+=tids
    await editable1.edit(f"**Send the Subject id :-**\n```{vj}```")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    response02 = s.get(f'https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{raw_text4}/topics?page=1', headers=headers).json()["data"]
    
    cool2 = ""
    vj = ""
    for dat in response02:
        FF = "**SUBJECT-ID - SUBJECT NAME - TOTAL VIDEOS - PDFS**"
        aa = f" ```{dat['_id']}```- **{dat['name']} - {dat['videos']} - {dat['notes']}**\n\n"
        idid=f"{dat['_id']}&"
        if len(f"{vj}{idid}")>4096:
            vj = ""
        vj+= idid     
        cool2 += aa
    await editable1.edit(f'{"**You have these Subjects in this Batch:-**"}\n\n{FF}\n\n{cool2}')
    editable2 = await m.reply_text(f"**Enter this to download full batch :-**\n```{vj}```")
    input5 = message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text
    xv = raw_text5.split('&')
    for y in range(0,len(xv)):
      t =xv[y].strip()
      html3 = s.get("https://api.penpencil.xyz/v2/batches/"+raw_text3+"/subject/"+raw_text4+"/contents?page=1&tag="+t+"&contentType=videos",headers=headers).content
      ff = json.loads(html3)
      tpage = (ff["paginate"])["totalCount"]//ff["paginate"]["limit"]+2
      print("Total page:",tpage)
      for i in range(1,tpage)[::-1]:
        html4 = s.get("https://api.penpencil.xyz/v2/batches/"+raw_text3+"/subject/"+raw_text4+"/contents?page="+str(i)+"&tag="+t+"&contentType=videos",headers=headers).json()["data"]
        html4.reverse()
        #break
        for dat in html4:
          try:
            class_title=(dat["topic"])
            class_url=dat["url"].replace("d1d34p8vz63oiq", "d3nzo6itypaz07").replace("mpd", "m3u8").strip()
            cc = f"{dat['topic']}:{dat['url']}"
            with open(f"{mm}-{batch}.txt", 'a') as f:
                f.write(f"{class_title}:{class_url}\n")
          except KeyError:
            pass
    await m.reply_document(f"{mm}-{batch}.txt")
    """

        print("Downloading pdfs")     
        response5 = s.get("https://api.penpencil.xyz/v2/batches/"+raw_text3+"/subject/"+raw_text4+"/contents?page=1&tag="+t+"&contentType=notes",headers=headers).json()
        tpage = response5["paginate"]["totalCount"]//response5["paginate"]["limit"]+2
        print(tpage)
        for i in range(1,tpage)[::-1]:
          response6 = s.get("https://api.penpencil.xyz/v2/batches/"+raw_text3+"/subject/"+raw_text4+"/contents?page="+str(i)+"&tag="+t+"&contentType=notes",headers=headers).json()["data"]
          for data in response6:
            try:
              title=(data["homeworkIds"][0]["topic"])
              baseurl= data["homeworkIds"][0]["attachmentIds"][0]["baseUrl"]
              key = data["homeworkIds"][0]["attachmentIds"][0]["key"]
            except KeyError:
              pass
              with open(f"{batch}.txt", 'a') as f:
                  f.write(f"{title}:{baseurl}{key}\n")
    await m.reply_text("Done")
    """




