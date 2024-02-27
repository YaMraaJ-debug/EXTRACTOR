from config import CHANNEL_ID, SUDO_USERS 
from Extractor.core import script
from pyrogram.errors import UserNotParticipant
from pyrogram.types import *
from Extractor.core.mongo.plans_db import premium_users




async def chk_user(query, user_id):
    user = await premium_users()
    if user_id in user or user_id in SUDO_USERS:
        await query.answer("Premium User!!")
        return 0
    else:
        await query.answer("Sir, you don't have premium access!!", show_alert=True)
        return 1




async def gen_link(app,chat_id):
   link = await app.export_chat_invite_link(chat_id)
   return link

async def subscribe(app, message):
   update_channel = CHANNEL_ID
   url = await gen_link(app, update_channel)
   if update_channel:
      try:
         user = await app.get_chat_member(update_channel, message.from_user.id)
         if user.status == "kicked":
            await message.reply_text("Sorry Sir, You are Banned. Contact My Support Group @DevsOops")
            return 1
      except UserNotParticipant:
         await message.reply_photo(photo="https://telegra.ph/file/b7a933f423c153f866699.jpg",caption=script.FORCE_MSG.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🤖 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ 🤖", url=f"{url}")]]))
         return 1
      except Exception:
         await message.reply_text("Something Went Wrong. Contact My Support Group")
         return 1



async def get_seconds(time_string):
    def extract_value_and_unit(ts):
        value = ""
        unit = ""

        index = 0
        while index < len(ts) and ts[index].isdigit():
            value += ts[index]
            index += 1

        unit = ts[index:].lstrip()

        if value:
            value = int(value)

        return value, unit

    value, unit = extract_value_and_unit(time_string)

    if unit == 's':
        return value
    elif unit == 'min':
        return value * 60
    elif unit == 'hour':
        return value * 3600
    elif unit == 'day':
        return value * 86400
    elif unit == 'month':
        return value * 86400 * 30
    elif unit == 'year':
        return value * 86400 * 365
    else:
        return 0







