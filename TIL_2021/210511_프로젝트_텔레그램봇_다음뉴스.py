# 라이브러리 및 api 설정
import telebot

API_KEY = '1644820427:AAEllDn4xGfRAFHGpb9lFxx5QsK-__AG7L8'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

# 오늘 뉴스
@bot.message_handler(commands=['news'])
def today_news(message):
    pass

bot.polling()
