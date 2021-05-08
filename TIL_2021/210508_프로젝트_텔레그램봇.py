# 수학문제 제작 텔레그램봇 제작하기
# 수학문제 파일 만들기
# 수학문제 파일 텔레그램으로 전송하기

# 라이브러리 및 api 설정
import telebot

API_KEY = '1644820427:AAEllDn4xGfRAFHGpb9lFxx5QsK-__AG7L8'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

bot.polling()

# Todo : 'TeleBot' object has no attribute 'message_handler'
