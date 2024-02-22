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


def decode(tn):
  key = "638udh3829162018".encode("utf8")
  iv = "fedcba9876543210".encode("utf8")
  ciphertext = bytearray.fromhex(b64decode(tn.encode()).hex())
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
  url=plaintext.decode('utf-8')
  return url




@app.on_message(filters.command(["teste"]) & filters.user(SUDO_USERS))
async def winners_account(_, message):
    global cancel
    cancel = False
    editable = await message.reply_text("send me your apex link")
    input1: message = await _.listen(editable.chat.id)
    api_url = input1.text
    raw_text = input1.text
    await input1.delete(True)
    editable = await message.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
  
    rwa_url = api_url+"/post/userLogin"
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

    input1: message = await _.listen(editable.chat.id)
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    scraper = cloudscraper.create_scraper()
    res = scraper.post(rwa_url, data=info, headers=hdr).content
    output = json.loads(res)
    
    userid = output["data"]["userid"]
    token = output["data"]["token"]
    hdr1 = {
        "Host": "winnersinstituteapi.classx.co.in",
        "Client-Service": "Appx",
        "Auth-Key": "appxapi",
        "User-Id": userid,
        "Authorization": token
        }
    
    await editable.edit(f"**login Successful {rwa_url}**")
    
    
