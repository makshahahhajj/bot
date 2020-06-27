import telebot
import time
from telebot import apihelper
import weather
from googletrans import Translator

# apihelper.proxy = {'https': 'socks5://157.230.154.241:9050'}
bot = telebot.TeleBot('1198680007:AAGRpE0wePCAs3zT5rFMcqD-scB8areWovk')
translator = Translator()


@bot.message_handler(commands=['start'])
def start_message( message ):
    bot.send_message(message.from_user.id, 'Привет, чтобы узнать погоду, напиши город')
    print(message.from_user.id)

@bot.message_handler(content_types=["text"])
def print_weather( message ):
        try:
            result = translator.translate(message.text)
            wet = weather.Weather(result.text)
            temperature = wet.load_weather()
            bot.send_message(message.chat.id, temperature)
        except Exception as e:
            bot.send_message(message.from_user.id, 'Город не найден')

while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(e.args)
        time.sleep(20)
