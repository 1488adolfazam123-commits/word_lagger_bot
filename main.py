import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def word_ladder(message):
    text = message.text
    words = text.split()
    result = "\n".join(words)
    bot.send_message(message.chat.id, result)

print("Бот запущен!")
bot.polling(none_stop=True)