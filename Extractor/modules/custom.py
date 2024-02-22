from pyrogram import filters
from Extractor import app
from pyromod import listen
from Extractor.core.multi_func import apex_accounts


@app.on_message(filters.command(["custom"]) & filters.user(SUDO_USERS))
async def custom_api(_, message):
  
    editable = await message.reply_text("Send your custom api : like :- https://rksirofficialapi.classx.co.in")
    input1: message = await _.listen(editable.chat.id)
    apex_api = input1
    await apex_accounts(_, message, apex_api)
    



