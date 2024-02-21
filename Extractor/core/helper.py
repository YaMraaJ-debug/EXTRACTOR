import os,time,asyncio,datetime,requests
import aiohttp
import aiofiles
import logging
import subprocess
from Downloader.core.utils import progress_bar
from pyrogram import filters
from Downloader import app
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser




def duration(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)


def get_duration(filepath):
        metadata = extractMetadata(createParser(filepath))
        if metadata.has("duration"):
            return metadata.get('duration').seconds
        else:
            return 0
            

def get_width_height(filename):
    metadata = extractMetadata(createParser(filename))
    if metadata.has("width") and metadata.has("height"):
        return metadata.get("width"), metadata.get("height")
    else:
        return 1280, 720   


async def download(url,name):
    ka = f'{name}.pdf'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(ka, mode='wb')
                await f.write(await resp.read())
                await f.close()
    return ka



async def download_video(url,cmd, name):
    download_cmd = f'{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args "aria2c: -x 16 -j 32"'
    global failed_counter
    print(download_cmd)
    logging.info(download_cmd)
    k = subprocess.run(download_cmd, shell=True)
    if "visionias" in cmd and k.returncode != 0 and failed_counter <= 10:
        failed_counter += 1
        await asyncio.sleep(5)
        await download_video(url, cmd, name)
    failed_counter = 0
    try:
        if os.path.isfile(name):
            return name
        elif os.path.isfile(f"{name}.webm"):
            return f"{name}.webm"
        name = name.split(".")[0]
        if os.path.isfile(f"{name}.mkv"):
            return f"{name}.mkv"
        elif os.path.isfile(f"{name}.mp4"):
            return f"{name}.mp4"
        elif os.path.isfile(f"{name}.mp4.webm"):
            return f"{name}.mp4.webm"

        return name
    except FileNotFoundError as exc:
        return os.path.isfile.splitext[0] + "." + "mp4"




async def send_vid(message, cc, filename, thumb, name, prog):
    subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
    await prog.delete(True)
    reply = await message.reply_text(f"**⥣ Uploading ...** » `{name}`")
    try:
        if thumb == "no":
            thumbnail = f"{filename}.jpg"
        else:
            thumbnail = thumb
    except Exception as e:
        await message.reply_text(str(e))
    dur = int(duration(filename))
    start_time = time.time()
    try:
        await app.send_video(chat_id=message.chat.id, video=filename, caption=cc, supports_streaming=True, height=720, width=1280, thumb=thumbnail, duration=dur, progress=progress_bar, progress_args=(reply, start_time))
    except Exception:
        await app.send_video(chat_id=message.chat.id, video=filename, caption=cc, progress=progress_bar, progress_args=(reply, start_time))
    os.remove(filename)
    os.remove(f"{filename}.jpg")
    await reply.delete(True)


async def take_screen_shot(video_file, name, path, ttl):
        out_put_file_name = f"{path}/{name}.jpg"
        if video_file.upper().endswith(("MKV", "MP4", "WEBM")):
            file_genertor_command = [
                "ffmpeg",
                "-ss",
                str(ttl),
                "-i",
                video_file,
                "-vframes",
                "1",
                out_put_file_name
            ]
            process = await asyncio.create_subprocess_exec(
                *file_genertor_command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            stdout, stderr = await process.communicate()
            e_response = stderr.decode().strip()
            t_response = stdout.decode().strip()

        if os.path.lexists(out_put_file_name):
            return out_put_file_name
        else:
            return None


 
