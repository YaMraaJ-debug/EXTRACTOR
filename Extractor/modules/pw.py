import requests, os, sys, re
import math
import json, asyncio
import subprocess
import datetime
from Extractor import app
from pyrogram import filters
from subprocess import getstatusoutput


async def get_otp(message, phone_no):
    url = "https://api.penpencil.co/v1/users/get-otp"
    query_params = {"smsType": "0"}

    headers = {
        "Content-Type": "application/json",
        "Client-Id": "5eb393ee95fab7468a79d189",
        "Client-Type": "WEB",
        "Client-Version": "2.6.12",
        "Integration-With": "Origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    }

    payload = {
        "username": phone_no,
        "countryCode": "+91",
        "organizationId": "5eb393ee95fab7468a79d189",
    }

    try:
        response = requests.post(url, params=query_params, headers=headers, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        await message.reply_text("**Failed to Generate OTP**")



async def get_token(message, phone_no, otp):
    url = "https://api.penpencil.co/v3/oauth/token"
    payload = {
        "username": phone_no,
        "otp": otp,
        "client_id": "system-admin",
        "client_secret": "KjPXuAVfC5xbmgreETNMaL7z",
        "grant_type": "password",
        "organizationId": "5eb393ee95fab7468a79d189",
        "latitude": 0,
        "longitude": 0
    }

    headers = {
        "Content-Type": "application/json",
        "Client-Id": "5eb393ee95fab7468a79d189",
        "Client-Type": "WEB",
        "Client-Version": "2.6.12",
        "Integration-With": "",
        "Randomid": "990963b2-aa95-4eba-9d64-56bb55fca9a9",
        "Referer": "https://www.pw.live/",
        "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    }

    try:
        r = requests.post(url, json=payload, headers=headers)
        r.raise_for_status()
        resp = r.json()
        token = resp['data']['access_token']
        return token
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        await message.reply_text("**Failed to Generate Token**")


async def pw_mobile(app, message):
    lol = await app.ask(message.chat.id, text="**ENTER YOUR PW MOBILE NO. WITHOUT COUNTRY CODE.**")
    phone_no = lol.text
    await lol.delete()
    await get_otp(message, phone_no)
    lol2 = await app.ask(message.chat.id, text="**ENTER YOUR OTP SENT ON YOUR MOBILE NO.**")
    otp = lol2.text
    await lol2.delete()
    token = await get_token(message, phone_no, otp)
    await message.reply_text(F"**YOUR TOKEN** => `{token}`")
    await pw_login(app, message, token)


async def pw_token(app, message):
    lol3 = await app.ask(message.chat.id, text="**ENTER YOUR PW ACCESS TOKEN**")
    token = lol3.text
    await lol3.delete()
    await pw_login(app, message, token)



async def pw_login(app, message, token):
    headers = {

            'Host': 'api.penpencil.co',

            'authorization': f"Bearer {token}",

            'client-id': '5eb393ee95fab7468a79d189',

            'client-version': '12.84',

            'user-agent': 'Android',

            'randomid': 'e4307177362e86f1',

            'client-type': 'MOBILE',

            'device-meta': '{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}',

            'content-type': 'application/json; charset=UTF-8',

    }

    params = {
       'mode': '1',
       'filter': 'false',
       'exam': '',
       'amount': '',
       'organisationId': '5eb393ee95fab7468a79d189',
       'classes': '',
       'limit': '20',
       'page': '1',
       'programId': '',
       'ut': '1652675230446', 
    }
    response = requests.get('https://api.penpencil.co/v3/batches/my-batches', params=params, headers=headers).json()["data"]
    aa = "**You have these Batches :-\n\nBatch ID   :   Batch Name**\n\n"
    for data in response:
        batch = data["name"]
        aa += f"**{batch}**   :   `{data['_id']}`\n"
    await message.reply_text(aa)
    input3 = await app.ask(message.chat.id, text="**Now send the Batch ID to Download**")
    raw_text3 = input3.text
    response2 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/details', headers=headers, params=params).json()
    subjects = response2.get('data', {}).get('subjects', [])
    bb = "**Subject   :   SubjectId**\n\n"
    vj = ""
    for subject in subjects:
        bb += f"**{subject.get('subject')}**   :   `{subject.get('subjectId')}`\n"
        vj += f"{subject.get('subjectId')}&"
    await message.reply_text(bb)
    input4 = await app.ask(message.chat.id, text=f"Now send the **Subject IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n`{vj}`")
    raw_text4 = input4.text
    xu = raw_text4.split('&')
    hh = ""
    for x in range(0,len(xu)):
        s =xu[x]
        for subject in subjects:
            if subject.get('subjectId') == s:
                hh += f"{subject.get('subjectId')}:{subject.get('tagCount')}&"

    input5 = await app.ask(message.chat.id, text="**Enter resolution**")
    raw_text5 = input5.text
    
    try:
        xv = hh.split('&')
        cc = ""
        cv = ""
        for y in range(0,len(xv)):
            t =xv[y]
            id, tagcount = t.split(':')
            r = int(tagcount) / 20
            rr = math.ceil(r)

            for i in range(1,rr):
                params = {'page': str(i)}
                response3 = requests.get(f"https://api.penpencil.co/v3/batches/{raw_text3}/subject/{id}/topics", params=params, headers=headers).json()["data"]
#                for data in response3:
                with open(f"mm.txt", 'a') as f:
                    f.write(f"{response3}")   
            

            await app.send_document(message.chat.id, document=f"mm.txt")
    except Exception as e:
        await message.reply_text(str(e))





"""
params1 = {'page': '1','tag': '','contentType': 'videos'}
            response3 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/subject/{t}/contents', params=params1, headers=headers).json()["data"]
            
            params2 = {'page': '1','tag': '','contentType': 'notes'}
            response4 = requests.get(f'https://api.penpencil.co/v3/batches/{raw_text3}/subject/{t}/contents', params=params2, headers=headers).json()["data"]

            try:
                for data in response3:
                    class_title = (data["topic"])
                    class_url = data["url"].replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("mpd", "m3u8").strip()
                    cc += f"{data['topic']}:{data['url']}\n"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{cc}")

                for data in response4:
                    class_title = (lol["topic"])
                    for lol in data["homeworkIds"]:
                        concatenated_url = homework["attachmentIds"]["baseUrl"] + homework["attachmentIds"]["key"]
                    cv += f"{data['topic']}:{data['url']}\n"
                    with open(f"{batch}.txt", 'a') as f:
                        f.write(f"{cv}")
            except Exception as e:
               await message.reply_text(str(e))
"""
