import requests, os, sys, re
import json, asyncio
import subprocess
import datetime
from pyromod import listen
from Downloader import app
from config import SUDO_USERS
from pyrogram import filters, idle
from subprocess import getstatusoutput




api = 'https://api.classplusapp.com/v2'

# ------------------------------------------------------------------------------------------------------------------------------- #


def get_datetime_str():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d%H%M%S")

def create_html_file(file_name, batch_name, contents):
    tbody = ''
    for line in contents:
        text, url = [item.strip('\n').strip() for item in line.split(':', 1)]
        tbody += f'<tr><td><a href="{url}">{text}</a></td></tr>'

    with open('template.html') as fp:
        file_content = fp.read()

    with open(file_name, 'w') as fp:
        fp.write(file_content.replace('tbody_content', tbody).replace('batch_name', batch_name))

 # ------------------------------------------------------------------------------------------------------------------------------- #


def get_course_content(session, course_id, folder_id=0):
        fetched_contents = []

        params = {
            'courseId': course_id,
            'folderId': folder_id,
        }

        res = session.get(f'{api}/course/content/get', params=params)

        if res.status_code == 200:
            res_json = res.json() 

            contents = res_json.get('data', {}).get('courseContent', [])

            for content in contents:
                if content['contentType'] == 1:
                    resources = content.get('resources', {})

                    if resources.get('videos') or resources.get('files'):
                        sub_contents = get_course_content(session, course_id, content['id'])
                        fetched_contents += sub_contents
                else:
                    name = content.get('name', '')
                    url = content.get('url', '')
                    fetched_contents.append(f'{name}:{url}\n')

        return fetched_contents



# ------------------------------------------------------------------------------------------------------------------------------- #



@app.on_message(filters.command(["classplus"])& filters.user(SUDO_USERS))
async def classplus_txt(app, message):   

    headers = {
        'accept-encoding': 'gzip',
        'accept-language': 'EN',
        'api-version'    : '35',
        'app-version'    : '1.4.73.2',
        'build-number'   : '35',
        'connection'     : 'Keep-Alive',
        'content-type'   : 'application/json',
        'device-details' : 'Xiaomi_Redmi 7_SDK-32',
        'device-id'      : 'c28d3cb16bbdac01',
        'host'           : 'api.classplusapp.com',
        'region'         : 'IN',
        'user-agent'     : 'Mobile-Android',
        'webengage-luid' : '00000187-6fe4-5d41-a530-26186858be4c'
    }

    
    try:
        editable = await message.reply_text("SEND YOUR CREDENTIALS AS SHOWN BELOW\n\nORGANISATION CODE:\n\nPHONE NUMBER:\n\nACCESS TOKEN:")
        input : message = await app.listen(editable.chat.id)

        creds = input.text
        session = requests.Session()
        session.headers.update(headers)

        logged_in = False

        if '\n' in creds:
            org_code, phone_no = [cred.strip() for cred in creds.split('\n')]

            if org_code.isalpha() and phone_no.isdigit() and len(phone_no) == 10:
                res = session.get(f'{api}/orgs/{org_code}')

                if res.status_code == 200:
                    res = res.json()

                    org_id = int(res['data']['orgId'])

                    data = {
                        'countryExt': '91',
                        'mobile'    : phone_no,
                        'viaSms'    : 1,
                        'orgId'     : org_id,
                        'eventType' : 'login',
                        'otpHash'   : 'j7ej6eW5VO'
                    }
        
                    res = session.post(f'{api}/otp/generate', data=json.dumps(data))

                    if res.status_code == 200:
                        res = res.json()

                        session_id = res['data']['sessionId']

                        editable = await message.reply_text("Send your otp ")
                        user_otp : message = await app.listen(editable.chat.id)

                        if user_otp.text.isdigit():
                            otp = user_otp.text.strip()

                            data = {
                                'otp'          : otp,
                                'sessionId'    : session_id,
                                'orgId'        : org_id,
                                'fingerprintId': 'a3ee05fbde3958184f682839be4fd0f7',
                                'countryExt'   : '91',
                                'mobile'       : phone_no,
                            }

                            res = session.post(f'{api}/users/verify', data=json.dumps(data))

                            if res.status_code == 200:
                                res = res.json()

                                user_id = res['data']['user']['id']
                                token = res['data']['token']
                                session.headers['x-access-token'] = token

                                await message.reply_text(f"Your access token for future uses -\n\n{token}")
                                
                                logged_in = True

                            else:
                                raise Exception('Failed to verify OTP.')  
                        raise Exception('Failed to validate OTP.')
                    raise Exception('Failed to generate OTP.')    
                raise Exception('Failed to get organization Id.')
            raise Exception('Failed to validate credentials.')

        else:

            token = creds.strip()
            session.headers['x-access-token'] = token


            res = session.get(f'{api}/users/details')

            if res.status_code == 200:
                res = res.json()

                user_id = res['data']['responseData']['user']['id']
                logged_in = True
            
            else:
                raise Exception('Failed to get user details.')


        if logged_in:

            params = {
                'userId': user_id,
                'tabCategoryId': 3
            }

            res = session.get(f'{api}/profiles/users/data', params=params)

            if res.status_code == 200:
                res = res.json()

                courses = res['data']['responseData']['coursesData']

                if courses:
                    text = ''

                    for cnt, course in enumerate(courses):
                        name = course['name']
                        text += f'{cnt + 1}. {name}\n'

                    editable = await message.reply_text(f"send index number of the course to download\n\n{text}")
                    num : message = await app.listen(editable.chat.id)
                        
                    if num.text.isdigit() and len(num.text) <= len(courses):

                        selected_course_index = int(num.text.strip())

                        course = courses[selected_course_index - 1]

                        selected_course_id = course['id']
                        selected_course_name = course['name']

                        msg  = await message.reply_text("Now your extracting your course")
                            

                        course_content = get_course_content(session, selected_course_id)
                        await msg.delete()

                        if course_content:

                            caption = (f"App Name : Classplus\nBatch Name : {selected_course_name}")

                            
                            text_file = f'downloads/{get_datetime_str()}.txt'
                            open(text_file, 'w').writelines(course_content)

                            await app.send_document(message.chat.id, text_file, caption=caption,
                                file_name=f"{selected_course_name}.txt",
                            )

                            html_file = f'downloads/{get_datetime_str()}.html'
                            create_html_file(html_file, selected_course_name, course_content)

                            await app.send_document(message.chat.id, html_file, caption=caption,
                                file_name=f"{selected_course_name}.html",
                            )

                            os.remove(text_file)
                            os.remove(html_file)
                            

                        else:
                            raise Exception('Did not found any content in course.')
                    raise Exception('Failed to validate course selection.')
                raise Exception('Did not found any course.')
            raise Exception('Failed to get courses.')
            

   
    except Exception as e:
        await message.reply_text(f"Error: {e}")
            





          
