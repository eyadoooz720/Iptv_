import telebot
import os

# ضع التوكن الخاص ببوتك هنا
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً! البوت يعمل الآن بنجاح على سيرفر Render.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "تم استلام رسالتك: " + message.text)

# تشغيل البوت
if __name__ == "__main__":
    bot.polling()
