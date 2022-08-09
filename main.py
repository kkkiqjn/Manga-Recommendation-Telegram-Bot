API_KEY = os.environ['API_KEY']
bot=telebot.TeleBot(API_KEY)
# @bot.message_handler(commands=["greet"])
# def greet(message):
#   bot.reply_to(message,"How are you doing!")
def checker(message):
  msg=message.text
  if "manga" in msg.lower()   :
    return True
  else:
    return False
def checker0(message):
  msg=message.text
  if len(msg.split())==1:
    return True
  else:
    return False
@bot.message_handler(commands=['hello',"Hello","start"])
def sendmsg(message):
  bot.send_message(message.chat.id,"Hello Mate!,get your Manga Recommendations.\nCheck about section  of this Bot before typing")
@bot.message_handler(func=checker)
def sendreply(message):
  msg=message.text.lower()
  if("action" in msg):
     bot.send_message(message.chat.id,"Solo levelling")
     # sendImageRemoteFile("https://wall.alphacoders.com/big.php?i=1093511",message.chat.id,"solo levelling")
     bot.send_message(message.chat.id,"One Piece")
     bot.send_message(message.chat.id,"One Punch Man")
  elif("hentai" in msg):
    bot.send_message(message.chat.id,"Hang out crisis")
    bot.send_message(message.chat.id,"Bokura No Hentai")
    bot.send_message(message.chat.id,"Henshin No News")
  elif("fantasy" in msg)  :
    bot.send_message(message.chat.id,"Chainsaw Man")
    bot.send_message(message.chat.id,"Fullmetal Alchemist")
    bot.send_message(message.chat.id,"Attack on titan")
  elif("horror" in msg) :
    bot.send_message(message.chat.id,"Demon Slayer:Kimetsu na yaiba")
    bot.send_message(message.chat.id,"land of lustrous")
    bot.send_message(message.chat.id,"Made in Abyss")

  elif("scifi" in msg or "sci-fi" in msg):
    bot.send_message(message.chat.id,"20th century boys")
    bot.send_message(message.chat.id,"The promised Never Land")
    bot.send_message(message.chat.id,"Asassination Classroom ")
  elif("comedy" in msg):
    bot.send_message(message.chat.id,"Haikyuu")
    bot.send_message(message.chat.id,"Sign")
    bot.send_message(message.chat.id,"Natsumes book of friends")
  elif("adventure" in msg):
    bot.send_message(message.chat.id,"Vagabond")
    bot.send_message(message.chat.id,"Omniscient Reader")
    bot.send_message(message.chat.id,"Vinland Saga")
  elif("romance" in msg):
    bot.send_message(message.chat.id,"Yana of the Dawn")
    bot.send_message(message.chat.id,"19 Days")
    bot.send_message(message.chat.id,"A silent voice")
  else:
    bot.send_message(message.chat.id,"Sorry? we have not got what you are looking for")
    
    
    
  
  
  
# def sendImageRemoteFile(img_url,id,caption):
#     url = r"https://api.telegram.org/bot"+API_KEY+"/sendPhoto?chat_id="+str(id)+"&caption="+caption
#     remote_image = requests.get(img_url)
#     photo = io.BytesIO(remote_image.content)
#     photo.name = 'img.png'
#     files = {'photo': photo}
#     data = {'chat_id' : "YOUR_CHAT_ID"}
#     r= requests.post(url, files=files, data=data)
#     print(r.status_code, r.reason, r.content)  
@bot.message_handler(func=checker0)
def entry(message):
  bot.send_message(message.chat.id,"Type like this---> [genre] manga or manga [genre]")
  
bot.polling()
