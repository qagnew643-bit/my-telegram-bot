import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN', '8923090415:AAGES1KzK5YWh1SUTr3pzbbB4dmawdjTe6U')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "ሰላም! እኔ የሱራፌል ረዳት ቦት ነኝ። እንዴት ልረዳዎት?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"ያሉኝ፡ {message.text}")

if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
