
import os
import telebot
from telebot import types

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# /start ወይም /help ሲባል የሚመጣ ሰላምታ እና ሜኑ
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('👋 ሰላምታ')
    itembtn2 = types.KeyboardButton('ℹ️ ስለ እኛ')
    itembtn3 = types.KeyboardButton('📞 አድራሻ')
    itembtn4 = types.KeyboardButton('❓ እርዳታ')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    
    bot.reply_to(message, "እንኳን ወደ ቦታችን በደህና መጡ! 👋\nእባክዎን ከታች ካሉት አማራጮች አንዱን ይምረጡ፡", reply_markup=markup)

# የሚላኩ መልእክቶችን ማስተናገጃ
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text

    if text == '👋 ሰላምታ':
        bot.reply_to(message, "ሰላም! ጤና ይስጥልኝ፤ እንዴት ልረዳዎት?")
    elif text == 'ℹ️ ስለ እኛ':
        bot.reply_to(message, "ይህ በ Telegram Bot API የተሰራ አውቶሜቲክ የቴሌግራም ቦት ነው!")
    elif text == '📞 አድራሻ':
        bot.reply_to(message, "ለበለጠ መረጃ እና አድራሻ በቴሌግራም መልእክት ይላኩልን።")
    elif text == '❓ እርዳታ':
        bot.reply_to(message, "ማንኛውንም ጥያቄ እዚህ መጻፍ ይችላሉ፤ በቅርቡ እንመልስልዎታለን!")
    else:
        bot.reply_to(message, f"መልእክትዎ ደርሶናል፡ '{text}'\nለበለጠ መረጃ ከታች ያሉትን ቁልፎች ይጠቀሙ።")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
