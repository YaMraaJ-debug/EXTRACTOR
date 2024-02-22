from pyrogram import filters
from Extractor import app
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #

button = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_")
                ],[
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsCreations"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                ]])


course_buttons = [              
                [
                    InlineKeyboardButton("Ocean", callback_data="maintainer_"),   
                    InlineKeyboardButton("Classplus", callback_data="maintainer_"),
                    InlineKeyboardButton("winners", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("khan", callback_data="maintainer_"),   
                    InlineKeyboardButton("Mg concept", callback_data="maintainer_"),
                    InlineKeyboardButton("Vidhya", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("Vikramjeet", callback_data="maintainer_"),   
                    InlineKeyboardButton("Neet Kakaji", callback_data="maintainer_"),
                    InlineKeyboardButton("pythics wala", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]


back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]


help_txt = """**
**Multiple Course Extract commands** 
"""
# ------------------------------------------------------------------------------- #




@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(photo="https://telegra.ph/file/9456751a4ca1a346e631f.jpg", caption="**ʜᴇʏ ᴛʜᴇʀᴇ!  ᴜɴʟᴇᴀsʜ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏғ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴄᴏᴜʀsᴇ ᴅᴏᴡɴʟᴏᴀᴅ ᴡɪᴢᴀʀᴅ – ɪ'ᴍ ɴᴏᴛ Jᴜsᴛ ʏᴏᴜʀ ᴀᴠᴇʀᴀɢᴇ ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ; ɪ'ᴍ ʏᴏᴜʀ ᴠɪᴘ ᴘᴀss ᴛᴏ ɢʀᴀʙʙɪɴɢ ᴏɴʟɪɴᴇ ᴄᴏᴜʀsᴇs ɪɴ sᴛʏʟᴇ!  ʀᴇᴀᴅʏ ᴛᴏ ᴇʟᴇᴠᴀᴛᴇ ʏᴏᴜʀ ʟᴇᴀʀɴɪɴɢ ɢᴀᴍᴇ? ʟᴇᴛ's ᴅɪᴠᴇ ɪɴᴛᴏ ᴛʜᴇ ᴡᴏʀʟᴅ ᴏғ ᴋɴᴏᴡʟᴇᴅɢᴇ ᴛᴏɢᴇᴛʜᴇʀ! 🎓✨**",
                            reply_markup=button)



@app.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        try:
            await query.edit_message_text(
                start_txt.format(query.from_user.mention),
                reply_markup=button
            )
        except MessageNotModified:
            pass


# ------------------------------------------------------------------------------- #
        
    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(course_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

# ------------------------------------------------------------------------------- #

    elif query.data=="maintainer_":
            await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)

  
# ------------------------------------------------------------------------------- #
 
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass
