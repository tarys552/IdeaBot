"""
Telegram-бот
Основная задача бота - отправлять текстовые сообщения
с данными о погоде в ответ на каманду 'погода на сегодня'
или 'погода на завтра' на основе гео-позиции пользователя
"""
import telebot
import settings
import requests
import re
try:
    bot = telebot.TeleBot(token=settings.token)  # pogoda_bot
except AttributeError:
    print("Ошибка в получении token")
fn = "idia.txt"

# RE_LINE = re.compile(r'(-?\d{1,3}) (-?\d{1,3})')


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет можешь скидывать мне свои идеи я их запишу')


@bot.message_handler(commands=["add"])
def get_message(message):
    bot.send_message(message.chat.id, 'Отправ мне сообщение с идеей')


@bot.message_handler(commands=["read"])
def get_message(message):
    with open(fn, 'r') as file:
        text = file
        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=["text"])
def get_message(message):

    with open(fn, 'a') as f:
        f.write(message.text + " \n")


if __name__ == '__main__':
    bot.polling(none_stop=True)
