import re
import random
from pyrogram import filters
from Extractor import app
from Extractor.core import script
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #

buttons = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ᴍᴏᴅᴇs", callback_data="modes_")
                ],[
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsCreations"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                ]])


modes_button = [[
                  InlineKeyboardButton("ᴄᴜsᴛᴏᴍ", callback_data="custom_"),
                  InlineKeyboardButton("ᴍᴀɴᴜᴀʟ", callback_data="manual_"),
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="home_")
                ]]


course_button1 = [              
                [
                    InlineKeyboardButton("ssᴄ ᴍᴀᴋᴇʀ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴘᴇʀғᴇᴄᴛ ᴀᴄᴀᴅᴇᴍʏ", callback_data="maintainer_"),
                ],
                [
                    InlineKeyboardButton("ᴄʟᴀssᴘʟᴜs", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴇ1 ᴄᴏᴀᴄʜɪɴɢ", callback_data="maintainer_"),     
                ],
                [
                    InlineKeyboardButton("sᴀᴍʏᴀᴋ ʀᴀs", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴠᴊ ᴇᴅᴜᴄᴀᴛɪᴏɴ", callback_data="maintainer_"),              
                ],
                [
                    InlineKeyboardButton("ɢʏᴀɴ ʙɪɴᴅᴜ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴅʜᴀɴᴀɴᴊᴀʏ ɪᴀs", callback_data="maintainer_"),                   
                ],
                [
                    InlineKeyboardButton("ᴛʜɪɴᴋ ssᴄ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴀsʜɪsʜ sɪɴɢ ʟᴇᴄ.", callback_data="maintainer_"),                    
                ],
                [
                    InlineKeyboardButton("ᴛᴜᴛᴏʀs ᴀᴅᴅᴀ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ɴɪᴍɪsʜᴀ ʙᴀɴsᴀʟ", callback_data="maintainer_"),          
                ],
                [
                    InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="modes_"),
                    InlineKeyboardButton("𝐍 𝐄 𝐗 𝐓", callback_data="next_")
                ]
                ]


course_button2 = [
                [
                    InlineKeyboardButton("sᴀᴄʜɪɴ ᴀᴄᴀᴅᴇᴍʏ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴀᴄʜᴀʀʏᴀ ᴄʟᴀssᴇs", callback_data="maintainer_"),
                ],
                [
                    InlineKeyboardButton("ᴛᴀʀɢᴇᴛ ᴘʟᴜs", callback_data="maintainer_"),   
                    InlineKeyboardButton("ʀᴡᴀ", callback_data="maintainer_"),
                ],
                [
                    InlineKeyboardButton("ᴡɪɴɴᴇʀs", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴏᴄᴇᴀɴ ɢᴜʀᴜᴋᴜʟ", callback_data="maintainer_"),     
                ],
                [
                    InlineKeyboardButton("ᴍɢ ᴄᴏɴᴄᴇᴘᴛ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ʏᴏᴅʜᴀ", callback_data="maintainer_"),              
                ],
                [
                    InlineKeyboardButton("ɴᴏᴛᴇ ʙᴏᴏᴋ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴜᴄ ʟɪᴠᴇ", callback_data="maintainer_"),      
                ],
                [
                    InlineKeyboardButton("sᴘᴀᴄᴇ ɪᴀs", callback_data="maintainer_"),   
                    InlineKeyboardButton("ʀɢ ᴠɪᴋʀᴀᴍᴊᴇᴇᴛ", callback_data="maintainer_"),       
                ],
                [
                    InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="modes_"),
                    InlineKeyboardButton("𝐏 𝐑 𝐄 𝐕", callback_data="manual_")
                ]
                ]



course_button3 = [              
                [   
                    InlineKeyboardButton("ᴠɪᴅʏᴀ ʙɪʜᴀʀ", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴀᴍᴀɴ sɪʀ", callback_data="maintainer_")
                ],
                [   
                    InlineKeyboardButton("ɴɪʀᴍᴀɴ ɪᴀs", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴘᴇʀᴍᴀʀ ssᴄ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ɴᴇᴏ sᴘᴀʀᴋ", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴍᴅ ᴄʟᴀssᴇs", callback_data="maintainer_")
                ],
                [   
                    InlineKeyboardButton("ɴɢ ʟᴇᴀʀɴᴇʀs", callback_data="maintainer_"),
                    InlineKeyboardButton("ssᴄ ɢᴜʀᴜᴋᴜʟ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ᴀʀᴍʏ sᴛᴜᴅʏ ʟɪᴠᴇ", callback_data="maintainer_"),
                    InlineKeyboardButton("sᴀɴᴋᴀʟᴘ", callback_data="maintainer_")
                ],
                [              
                    InlineKeyboardButton("SOON", callback_data="maintainer_"),
                    InlineKeyboardButton("SOON", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="modes_"),
                    InlineKeyboardButton("𝐍 𝐄 𝐗 𝐓", callback_data="next_")
                ]
                ]




back_button  = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="modes_"),                    
                ]]



# ------------------------------------------------------------------------------- #




@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(photo=random.choice(script.IMG), 
                            caption=script.START_TXT.format(message.from_user.mention),
                            reply_markup=buttons)








@app.on_callback_query(re.compile(r"^(home_|modes_|custom_|manual_|maintainer_|close_data|next_.+)$"))
async def handle_callback(_, query):

    if query.data=="home_":        
        
        await query.message.edit_text(
              script.START_TXT.format(query.from_user.mention),
              reply_markup=buttons
            )
        
    elif query.data=="modes_":        
        reply_markup = InlineKeyboardMarkup(modes_button)
        await query.message.edit_text(
              script.MODES_TXT,
              reply_markup=reply_markup)
        
        
    elif query.data=="custom_":        
        reply_markup = InlineKeyboardMarkup(back_button)
        await query.message.edit_text(
              script.CUSTOM_TXT,
              reply_markup=reply_markup
            )
        
        
    elif query.data=="manual_":        
        reply_markup = InlineKeyboardMarkup(course_button1)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_":        
        reply_markup = InlineKeyboardMarkup(course_button2)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
        
    elif query.data=="maintainer_":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)


    elif query.data=="close_data":
        await query.message.delete()
        await query.message.reply_to_message.delete()



