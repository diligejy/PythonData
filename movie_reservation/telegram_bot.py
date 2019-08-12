import telegram

bot = telegram.Bot(token = '966509765:AAFWw_t5QlhBo8f_QLI1bT-AFdQuXatGhUE')

# for i in bot.getUpdates():
#    print(i.message)

bot.sendMessage(chat_id = 959425455, text = '테스트입네다')