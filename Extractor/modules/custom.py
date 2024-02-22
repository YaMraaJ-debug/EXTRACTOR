from pyrogram import filters
from Extractor import app
from pyromod import listen



@app.on_message(filters.command(["custom"]) & filters.user(SUDO_USERS))
async def custom_api(_, message):
  
    editable = await message.reply_text("Send your custom api : like :- https://rksirofficialapi.classx.co.in")
    await custom_accounts(_, message, apex_api)
    



