from pyrogram import filters
from Downloader import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(photo="https://telegra.ph/file/9456751a4ca1a346e631f.jpg", caption="**ʜᴇʏ ᴛʜᴇʀᴇ!  ᴜɴʟᴇᴀsʜ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏғ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴄᴏᴜʀsᴇ ᴅᴏᴡɴʟᴏᴀᴅ ᴡɪᴢᴀʀᴅ – ɪ'ᴍ ɴᴏᴛ Jᴜsᴛ ʏᴏᴜʀ ᴀᴠᴇʀᴀɢᴇ ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ; ɪ'ᴍ ʏᴏᴜʀ ᴠɪᴘ ᴘᴀss ᴛᴏ ɢʀᴀʙʙɪɴɢ ᴏɴʟɪɴᴇ ᴄᴏᴜʀsᴇs ɪɴ sᴛʏʟᴇ!  ʀᴇᴀᴅʏ ᴛᴏ ᴇʟᴇᴠᴀᴛᴇ ʏᴏᴜʀ ʟᴇᴀʀɴɪɴɢ ɢᴀᴍᴇ? ʟᴇᴛ's ᴅɪᴠᴇ ɪɴᴛᴏ ᴛʜᴇ ᴡᴏʀʟᴅ ᴏғ ᴋɴᴏᴡʟᴇᴅɢᴇ ᴛᴏɢᴇᴛʜᴇʀ! 🎓✨**",
                            reply_markup=InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_")
                ],             
                [
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsXCreations"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                ]
                            ]))



