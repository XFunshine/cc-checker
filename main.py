import requests,re
from hh import keep_alive
try:
    import telebot
except:
    import os
    os.system("pip install pyTelegramBotAPI")
from telebot import *
from NEW412 import Tele
from colorama import Fore
sto = {"stop":False}
token = "6481205043:AAEP6O66EeKJc9jraQ-PXsZOSPuplZ5RLmE" 
id =  5551232924
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["stop"])
def start(message):
    sto.update({"stop":True})
    bot.reply_to(message,'BSDK STOP😂HOGAYA ')
@bot.message_handler(commands=["start"])
def start(message):
 bot.send_message(message.chat.id,"SEND YOUR CC .TXT FILE, BOT MADE BY @PvT_VICtORY ".format(message.chat.first_name),reply_markup=telebot.types.InlineKeyboardMarkup())
@bot.message_handler(content_types=["document"])
def main(message):
 first_name = message.from_user.first_name
 last_name = message.from_user.last_name
 name=f"{first_name} {last_name}"
 risk=0
 bad=0
 nok=0
 ok = 0
 ko = (bot.reply_to(message,f"#－ WELCOME {name} LET MEE CHECK YOU'RE CC HA").message_id)
 ee=bot.download_file(bot.get_file(message.document.file_id).file_path)
 with open("combo.txt","wb") as w:
     w.write(ee)
 print(message.chat.id)
 sto.update({"stop":False})
 if message.chat.id == id:
   with open("combo.txt") as file:
       lino = file.readlines()
       lino = [line.rstrip() for line in lino]
       total = len(lino)
       for cc in lino:
           if sto["stop"] == False:
               pass
           else:
               break
           bin=cc[:6]
           url=f"https://lookup.binlist.net/{bin}"
           try:
           	req=requests.get(url).json()
           except:
           	pass
           try:
           	inf = req['scheme']
           except:
           	inf = "------------"
           try:
           	type = req['type']
           except:
           	type = "-----------"
           try:
           	brand = req['brand']
           except:
           	brand = '-----'
           try:
           	info = inf + '-' + type + '-' + brand
           except:
           	info = "-------"
           try:
           	ii = info.upper()
           except:
           	ii = "----------"
           try:
           	bank = req['bank']['name'].upper()
           except:
           	bank = "--------"
           try:
           	do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
           except:
           	do = "-----------"
           mes = types.InlineKeyboardMarkup(row_width=1)
           GALD1 = types.InlineKeyboardButton(f"• {cc} •",callback_data='u8')
           #res = types.InlineKeyboardButton(f"• {last} •",callback_data='u1')
           GALD3 = types.InlineKeyboardButton(f" Success ✅ - ↯[ {ok} ] ",callback_data='u2')
           GALD4 = types.InlineKeyboardButton(f" Declined - ↯ [ {bad} ] ",callback_data='u1')
           risk6 = types.InlineKeyboardButton(f" Risk - ↯ [ {risk} ] ",callback_data='u1')
           GALD5 = types.InlineKeyboardButton(f" TOTAL - ↯ [ {total} ] ",callback_data='u1')
           mes.add(GALD1,GALD3,GALD4,risk6,GALD5)
           bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text=f'''HELLO {name}, PLEASE WAIT FOR CHECK COMBO AND SEND HIT.
    ''',parse_mode='markdown',reply_markup=mes)
           
           try:
             last = str(Tele(cc))
           except Exception as e:
               print(e)
               try:
                  last = str(Tele(cc))
               except Exception as e:
                  print(e)
                  bot.reply_to(message,f"CARD IS DEAD AND I SKIPPED >> {cc}")
           if "risk" in last:
           	risk += 1
           	print(Fore.YELLOW+cc+"->"+Fore.CYAN+last)
           elif "Shit Insufficient Funds" in last:
               ok +=1
               respo = f'''
⧱━━━━━━━𝙑𝙄𝘾𝙏𝙊𝙍𝙔━━━━━━━⧱
┣𝘚𝘜𝘊𝘊𝘌𝘚𝘚 (𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦 0.01$)
┗━━━━━━━━━━━━━━━━━━━━
┣𝘊𝘊 - ↯ {cc}
┗━━━━━━━━━━━━━━━━━━━━
┣𝘚𝘵𝘢𝘵𝘶𝘴 - ↯ 𝘈𝘱𝘱𝘳𝘰𝘷𝘦𝘥! ✅
┗━━━━━━━━━━━━━━━━━━━━
┣𝘔𝘦𝘴𝘴𝘢𝘨𝘦 - ↯ 𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦-𝘈𝘶𝘵𝘩-𝘚𝘜𝘊𝘊𝘌𝘚𝘚 ✅
┗━━━━━━━━━━━━━━━━━━━━
'''
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
               with open("hit.txt", "a") as f:
               	f.write(f'''
⧱━━━━━━━𝙑𝙄𝘾𝙏𝙊𝙍𝙔━━━━━━━⧱
┣𝘚𝘜𝘊𝘊𝘌𝘚𝘚 (𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦 0.01$)
┗━━━━━━━━━━━━━━━━━━━━
┣𝘊𝘊 - ↯ {cc}
┗━━━━━━━━━━━━━━━━━━━━
┣𝘚𝘵𝘢𝘵𝘶𝘴 - ↯ 𝘈𝘱𝘱𝘳𝘰𝘷𝘦𝘥! ✅
┗━━━━━━━━━━━━━━━━━━━━
┣𝘔𝘦𝘴𝘴𝘢𝘨𝘦 - ↯ 𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦-𝘈𝘶𝘵𝘩-𝘚𝘜𝘊𝘊𝘌𝘚𝘚 ✅
┗━━━━━━━━━━━━━━━━━━━━
''')
           elif "TRUE" in last:
               ok += 1
               respo = (f'''
⧱━━━━━━━𝙑𝙄𝘾𝙏𝙊𝙍𝙔━━━━━━━⧱
┣𝘚𝘜𝘊𝘊𝘌𝘚𝘚 (𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦 0.01$)
┗━━━━━━━━━━━━━━━━━━━━
┣𝘊𝘊 - ↯ {cc}
┗━━━━━━━━━━━━━━━━━━━━
┣𝘚𝘵𝘢𝘵𝘶𝘴 - ↯ 𝘈𝘱𝘱𝘳𝘰𝘷𝘦𝘥! ✅
┗━━━━━━━━━━━━━━━━━━━━
┣𝘔𝘦𝘴𝘴𝘢𝘨𝘦 - ↯ 𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦-𝘈𝘶𝘵𝘩-𝘚𝘜𝘊𝘊𝘌𝘚𝘚 ✅
┗━━━━━━━━━━━━━━━━━━━━
''')
               print(Fore.YELLOW+cc+"->"+Fore.GREEN+last)
               bot.reply_to(message,respo)
               with open("hit.txt", "a") as f:
               	f.write(f'''
⧱━━━━━━━𝙑𝙄𝘾𝙏𝙊𝙍𝙔━━━━━━━⧱
┣𝘚𝘜𝘊𝘊𝘌𝘚𝘚 (𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦 0.01$)
┗━━━━━━━━━━━━━━━━━━━━
┣𝘊𝘊 - ↯ {cc}
┗━━━━━━━━━━━━━━━━━━━━
┣𝘚𝘵𝘢𝘵𝘶𝘴 - ↯ 𝘈𝘱𝘱𝘳𝘰𝘷𝘦𝘥! ✅
┗━━━━━━━━━━━━━━━━━━━━
┣𝘔𝘦𝘴𝘴𝘢𝘨𝘦 - ↯ 𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦-𝘈𝘶𝘵𝘩-𝘚𝘜𝘊𝘊𝘌𝘚𝘚 ✅
┗━━━━━━━━━━━━━━━━━━━━
''')
           else:
                   bad +=1
                   print(Fore.YELLOW+cc+"->"+Fore.RED+last)
       if sto["stop"] == False:
           bot.reply_to(message,'𝘾𝙝𝙚𝙘𝙠 𝙃𝙤𝙜𝙖𝙮𝙖 ✅, 𝙎𝙚𝙣𝙙 𝘼𝙣𝙤𝙩𝙝𝙚𝙧 𝘾𝘾 𝘾𝙤𝙢𝙗𝙤')
           bot.reply_to(message,'@a4checkerbot  𝘽𝙔  @a4hay 𝘿𝙈 𝙏𝙊 𝘽𝙐𝙔 𝙎𝘾𝙍𝙄𝙋𝙏\n @𝙋𝙫𝙏_𝙑𝙄𝘾𝙩𝙊𝙍𝙔')
 else:
     bot.reply_to(message,'@a4checkerbot  𝘽𝙔  @a4hay 𝘿𝙈 𝙏𝙊 𝘽𝙐𝙔 𝙎𝘾𝙍𝙄𝙋𝙏\n @𝙋𝙫𝙏_𝙑𝙄𝘾𝙩𝙊𝙍𝙔')
keep_alive()
print("𝙎𝙏𝘼𝙍𝙏𝙀𝘿 𝘽𝙊𝙏 𝘽𝙔  @a4hay")
bot.infinity_polling()
