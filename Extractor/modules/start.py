import re
import random
from pyrogram import filters
from Extractor import app
from Extractor.core import script
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Extractor.modules.appex import appex_txt
from Extractor.modules.classplus import classplus_txt
from Extractor.modules.pw import pw_mobile, pw_token
from Extractor.modules.exampur import exampur_txt
from Extractor.modules.app_exampur import appexampur_txt
from Extractor.modules.careerwill import career_will
from Extractor.modules.khan import khan_login

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


custom_button = [[
                  InlineKeyboardButton("ᴄʟɪᴄᴋ", callback_data="c_mode")
                ],[
                  InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_")
                ]]


button1 = [              
                [
                    InlineKeyboardButton("ssᴄ ᴍᴀᴋᴇʀ", callback_data="ss_maker"),   
                    InlineKeyboardButton("ᴘᴇʀғᴇᴄᴛ ᴀᴄᴀᴅᴇᴍʏ", callback_data="perfect_acc"),
                ],
                [
                    InlineKeyboardButton("ᴄʟᴀssᴘʟᴜs", callback_data="classplus_"),   
                    InlineKeyboardButton("ᴇ1 ᴄᴏᴀᴄʜɪɴɢ", callback_data="e1_coaching"),     
                ],
                [
                    InlineKeyboardButton("sᴀᴍʏᴀᴋ ʀᴀs", callback_data="samyak_ras"),   
                    InlineKeyboardButton("ᴠᴊ ᴇᴅᴜᴄᴀᴛɪᴏɴ", callback_data="vj_education"),              
                ],
                [
                    InlineKeyboardButton("ɢʏᴀɴ ʙɪɴᴅᴜ", callback_data="gyan_bindu"),   
                    InlineKeyboardButton("ᴅʜᴀɴᴀɴᴊᴀʏ ɪᴀs", callback_data="dhananjay_ias"),                   
                ],
                [
                    InlineKeyboardButton("ᴛʜɪɴᴋ ssᴄ", callback_data="think_ssc"),   
                    InlineKeyboardButton("ᴀsʜɪsʜ sɪɴɢ ʟᴇᴄ.", callback_data="Ashish_lec"),                    
                ],
                [
                    InlineKeyboardButton("ᴛᴜᴛᴏʀs ᴀᴅᴅᴀ", callback_data="tutors_adda"),   
                    InlineKeyboardButton("ɴɪᴍɪsʜᴀ ʙᴀɴsᴀʟ", callback_data="nimisha_bansal"),          
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_3"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_1")
                ]
                ]


button2 = [
                [
                    InlineKeyboardButton("sᴀᴄʜɪɴ ᴀᴄᴀᴅᴇᴍʏ", callback_data="sachin_acc"),   
                    InlineKeyboardButton("ᴀᴄʜᴀʀʏᴀ ᴄʟᴀssᴇs", callback_data="acharya_classes"),
                ],
                [
                    InlineKeyboardButton("ᴛᴀʀɢᴇᴛ ᴘʟᴜs", callback_data="target_plus"),   
                    InlineKeyboardButton("ʀᴡᴀ", callback_data="rwa_"),
                ],
                [
                    InlineKeyboardButton("ᴡɪɴɴᴇʀs", callback_data="winners_"),   
                    InlineKeyboardButton("ᴏᴄᴇᴀɴ ɢᴜʀᴜᴋᴜʟ", callback_data="ocean_gurukul"),     
                ],
                [
                    InlineKeyboardButton("ᴍɢ ᴄᴏɴᴄᴇᴘᴛ", callback_data="mg_concept"),   
                    InlineKeyboardButton("ʏᴏᴅʜᴀ", callback_data="yodha_"),              
                ],
                [
                    InlineKeyboardButton("ɴᴏᴛᴇ ʙᴏᴏᴋ", callback_data="note_book"),   
                    InlineKeyboardButton("ᴜᴄ ʟɪᴠᴇ", callback_data="uc_live"),      
                ],
                [
                    InlineKeyboardButton("sᴘᴀᴄᴇ ɪᴀs", callback_data="space_ias"),   
                    InlineKeyboardButton("ʀɢ ᴠɪᴋʀᴀᴍᴊᴇᴇᴛ", callback_data="rg_vikramjeet"),       
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="manual_"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_2")
                ]
                ]



button3 = [              
                [   
                    InlineKeyboardButton("ᴠɪᴅʏᴀ ʙɪʜᴀʀ", callback_data="vidya_bihar"),
                    InlineKeyboardButton("ᴀᴍᴀɴ sɪʀ", callback_data="aman_sir")
                ],
                [   
                    InlineKeyboardButton("ɴɪʀᴍᴀɴ ɪᴀs", callback_data="nirman_ias"),
                    InlineKeyboardButton("ᴘᴇʀᴍᴀʀ ssᴄ", callback_data="permar_ssc")
                ],
                [
                    InlineKeyboardButton("ɴᴇᴏ sᴘᴀʀᴋ", callback_data="neo_spark"),
                    InlineKeyboardButton("ᴍᴅ ᴄʟᴀssᴇs", callback_data="md_classes")
                ],
                [   
                    InlineKeyboardButton("ɴɢ ʟᴇᴀʀɴᴇʀs", callback_data="ng_learners"),
                    InlineKeyboardButton("ssᴄ ɢᴜʀᴜᴋᴜʟ", callback_data="ssc_gurukul")
                ],
                [
                    InlineKeyboardButton("ᴀʀᴍʏ sᴛᴜᴅʏ ʟɪᴠᴇ", callback_data="army_study"),
                    InlineKeyboardButton("sᴀɴᴋᴀʟᴘ", callback_data="sankalp_")
                ],
                [              
                    InlineKeyboardButton("ᴛᴀʀɢᴇᴛ ᴜᴘsᴄ", callback_data="target_upsc"),
                    InlineKeyboardButton("ɢᴋ ᴄᴀғᴇ", callback_data="gk_cafe")
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_1"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_3")
                ]
                ]



button4 = [              
                [   
                    InlineKeyboardButton("ᴄᴀʀᴇᴇʀᴡɪʟʟ", callback_data="careerwill_"),
                    InlineKeyboardButton("ᴋʜᴀɴ", callback_data="khan_")
                ],
                [   
                    InlineKeyboardButton("ᴘʜʏsɪᴄs ᴡᴀʟʟᴀʜ", callback_data="pw_"),
                    InlineKeyboardButton("ᴇxᴀᴍᴘᴜʀ", callback_data="exampur_")
                ],
                [
                    InlineKeyboardButton("ᴀᴘᴘ ᴇxᴀᴍᴘᴜʀ", callback_data="app_exampur"),
                    InlineKeyboardButton("ɴᴇᴇᴛ ᴋᴀᴋᴀJee", callback_data="neet_kakajee")
                ],
                [   
                    InlineKeyboardButton("ᴏғғɪᴄᴇʀs ᴀᴄᴀᴅᴇᴍʏ", callback_data="officers_acc"),
                    InlineKeyboardButton("ʀᴋ sɪʀ", callback_data="rk_sir")
                ],
                [
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_"),
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_")
                ],
                [              
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_"),
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_2"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="manual_")
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








@app.on_callback_query()
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
        reply_markup = InlineKeyboardMarkup(custom_button)
        await query.message.edit_text(
              script.CUSTOM_TXT,
              reply_markup=reply_markup
            )
        
     
    elif query.data=="manual_":        
        reply_markup = InlineKeyboardMarkup(button1)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="c_mode":        
        api = await app.ask(query.message.chat.id, text="**SEND APPX API\n\n✅ Example:\ntcsexamzoneapi.classx.co.in**")
        api_txt = api.text
        name = api_txt.split('.')[0].replace("api", "") if api else api_txt.split('.')[0]
        await appex_txt(app, query.message, api, name)

      
    elif query.data=="next_1":        
        reply_markup = InlineKeyboardMarkup(button2)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_2":        
        reply_markup = InlineKeyboardMarkup(button3)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_3":        
        reply_markup = InlineKeyboardMarkup(button4)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )

          
        
    elif query.data=="maintainer_":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)


    elif query.data=="careerwill_":
        await career_will(app, query.message)
  
    elif query.data=="khan_":
        await khan_login(app, query.message)

    elif query.data=="ss_maker":     
        api = "sscmakerexampreparationapi.classx.co.in"
        name = "SSC Makers"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="perfect_acc":     
        api = "perfectionacademyapi.appx.co.in"
        name = "Perfection Academy"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="e1_coaching":     
        api = "e1coachingcenterapi.classx.co.in"
        name = "e1 coaching"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="samyak_ras":     
        api = "samyakapi.classx.co.in"
        name = "Samyak"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="vj_education":     
        api = "vjeducationapi.appx.co.in"
        name = "VJ Education"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="gyan_bindu":     
        api = "gyanbinduapi.appx.co.in"
        name = "Gyan Bindu"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="dhananjay_ias":     
        api = "dhananjayiasacademyapi.classx.co.in"
        name = "Dhananjay IAS"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="think_ssc":     
        api = "thinksscapi.classx.co.in"
        name = "Think SSC"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="Ashish_lec":     
        api = "ashishsinghlecturesapi.classx.co.in"
        name = "Ashish Singh"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="tutors_adda":     
        api = "tutorsaddaapi.classx.co.in"
        name = "Tutors Adda"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="nimisha_bansal":     
        api = "nimishabansalapi.appx.co.in"
        name = "Nimisha Bansal"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="sachin_acc":     
        api = "sachinacademyapi.classx.co.in"
        name = "Sachin Academy"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="acharya_classes":     
        api = "acharyaclassesapi.classx.co.in"
        name = "Acharya Classes"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="target_plus":     
        api = "targetpluscoachingapi.classx.co.in"
        name = "Target Plus Coaching"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="rwa_":   
        api = "rozgarapinew.teachx.in"
        name = "Rojgar with Ankit"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="winners_":     
        api = "winnersinstituteapi.classx.co.in"
        name = "Winners"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="ocean_gurukul":     
        api = "oceangurukulsapi.classx.co.in"
        name = "Ocean Gurukul"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="mg_concept":     
        api = "mgconceptapi.classx.co.in"
        name = "MG Concept"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="yodha_":     
        api = "yodhaappapi.classx.co.in"
        name = "Yodha"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="note_book":     
        api = "notebookapi.classx.co.in"
        name = "Note Book"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="uc_live":     
        api = "ucliveapi.classx.co.in"
        name = "UC LIVE"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="space_ias":     
        api = "spaceiasapi.classx.co.in"
        name = "Space IAS"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="rg_vikramjeet":     
        api = "rgvikramjeetapi.classx.co.in"
        name = "RG Vikramjeet"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="vidya_bihar":     
        api = "vidyabiharapi.teachx.in"
        name = "Vidya Vihar"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="aman_sir":     
        api = "amansirenglishapi.classx.co.in"
        name = "Aman Sir English"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="nirman_ias":     
        api = "nirmaniasapi.classx.co.in"
        name = "Nirman IAS"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="permar_ssc":     
        api = "parmaracademyapi.classx.co.in"
        name = "Parmar Academy"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="neo_spark":     
        api = "neosparkapi.classx.co.in"
        name = "Neo Spark"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="md_classes":     
        api = "mdclassesapi.classx.co.in"
        name = "MD Classes"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="ng_learners":     
        api = "nglearnersapi.classx.co.in"
        name = "NG Learners"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="ssc_gurukul":     
        api = "ssggurukulapi.appx.co.in"
        name = "SSC Gurukul"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="army_study":     
        api = "armystudyliveclassesapi.classx.co.in"
        name = "Army Study Live"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="sankalp_":     
        api = "sankalpclassesapi.classx.co.in"
        name = "Sankalp"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="target_upsc":     
        api = "targetupscapi.classx.co.in"
        name = "Target UPSC"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="gk_cafe":     
        api = "gkcafeapi.classx.co.in"
        name = "GK Cafe"
        await appex_txt(app, query.message, api, name)

    elif query.data == 'officers_acc':
        api = "theofficersacademyapi.classx.co.in"
        name = "Officers Academy"
        await appex_txt(app, query.message, api, name)

    elif query.data == 'rk_sir':
        api = "rksirofficialapi.classx.co.in"
        name = "Rk Sir Official"
        await appex_txt(app, query.message, api, name)  
  
    elif query.data == 'exampur_':
        await exampur_txt(app, query.message)

    elif query.data == 'neet_kakajee':
        api = "neetkakajeeapi.classx.co.in"
        name = "Neet Kaka JEE"
        await appex_txt(app, query.message, api, name) 

    elif query.data == 'app_exampur':
        await appexampur_txt(app, query.message)
  
    elif query.data=="classplus_":          
        await classplus_txt(app, query.message)
  
    elif query.data == 'pw_':
        await query.message.reply_text(
            "**CHHOSE FROM BELOW **",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("Mobile No.", callback_data='mobile_'),
                    InlineKeyboardButton("Token", callback_data='token_'),
                ]]))

    elif query.data == 'mobile_':
        await pw_mobile(app, query.message)

    elif query.data == 'token_':
        await pw_token(app, query.message)
        





    elif query.data=="close_data":
        await query.message.delete()
        await query.message.reply_to_message.delete()



