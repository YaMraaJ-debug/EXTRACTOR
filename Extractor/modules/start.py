import re
from pyrogram import filters
from Extractor import app
from Extractor.core import script
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #

button = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ᴍᴏᴅᴇs", callback_data="modes_")
                ],[
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsCreations"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                ]])


modes_button = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ᴄᴜsᴛᴏᴍ", callback_data="custom_"),
                  InlineKeyboardButton("ᴍᴀɴᴜᴀʟ", callback_data="manual_")
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="home_")
                ]])


course_buttons = [              
                [
                    InlineKeyboardButton("ssᴄ ᴍᴀᴋᴇʀ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴘᴇʀғᴇᴄᴛ ᴀᴄᴀᴅᴇᴍʏ", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴀᴍᴀɴ sɪʀ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ᴄʟᴀssᴘʟᴜs", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴇ1 ᴄᴏᴀᴄʜɪɴɢ", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴘᴇʀᴍᴀʀ ssᴄ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("sᴀᴍʏᴀᴋ ʀᴀs", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴠᴊ ᴇᴅᴜᴄᴀᴛɪᴏɴ", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴍᴅ ᴄʟᴀssᴇs", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ɢʏᴀɴ ʙɪɴᴅᴜ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴅʜᴀɴᴀɴᴊᴀʏ ɪᴀs", callback_data="maintainer_"),
                    InlineKeyboardButton("ssᴄ ɢᴜʀᴜᴋᴜʟ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ᴛʜɪɴᴋ ssᴄ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴀsʜɪsʜ sɪɴɢ ʟᴇᴄ.", callback_data="maintainer_"),
                    InlineKeyboardButton("ɴɢ ʟᴇᴀʀɴᴇʀs", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="modes_"),
                    InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close_data")
                ]
                ]


back_button  = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="modes_"),                    
                ]]



# ------------------------------------------------------------------------------- #




@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(photo="https://graph.org/file/dbd48ba7093582ab20063.jpg", 
                            caption=script.START_TXT.format(message.from_user.mention),
                            reply_markup=button)



@app.on_callback_query(re.compile(r"^(home_|modes_|custom_|manual_|maintainer_|close_data.+)$"))
async def handle_callback(_, query):

    if query.data=="home_":
        buttons = [[
                       InlineKeyboardButton("ᴍᴏᴅᴇs", callback_data="modes_")
                  ],[
                       InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsCreations"),
                       InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                  ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
              script.START_TXT.format(query.from_user.mention),
              reply_markup=reply_markup
            )
        
# ------------------------------------------------------------------------------- #
        
    elif query.data=="modes_":        
        reply_markup = InlineKeyboardMarkup(modes_button)
        await query.message.edit_text(
              scrip.MODES_TXT,
              reply_markup=reply_markup)
        


# ------------------------------------------------------------------------------- #
        
    elif query.data=="custom_":        
        reply_markup = InlineKeyboardMarkup(back_button)
        await query.message.edit_text(
              script.CUSTOM_TXT,
              reply_markup=reply_markup
            )
        


# ------------------------------------------------------------------------------- #
        
    elif query.data=="manual_":        
        reply_markup = InlineKeyboardMarkup(course_buttons)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
        
          
# ------------------------------------------------------------------------------- #

    elif query.data=="maintainer_":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)

  
# ------------------------------------------------------------------------------- #
 
    elif query.data=="close_data":
        await query.message.delete()
        await query.message.reply_to_message.delete()
        
