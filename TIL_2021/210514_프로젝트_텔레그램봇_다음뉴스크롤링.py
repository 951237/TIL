# 라이브러리 및 api 설정
import telebot
import requests
from bs4 import BeautifulSoup

API_KEY = '1644820427:AAEllDn4xGfRAFHGpb9lFxx5QsK-__AG7L8'
bot = telebot.TeleBot(API_KEY)
chid_id = '428116987'


@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(commands=['news'])
def today_news(message):
    # 크롤링 정보 받아오기
    def create_soup(p_url):
        res = requests.get(p_url, verify=False)  # ssl 인증서 관련
        res.raise_for_status()  # 정보가 없으면 프로그램 종료
        soup = BeautifulSoup(res.text, "lxml")
        return soup

    try:
        result = ""
        result += f"===== 이시간 주요 뉴스 =====\n"
        URL = "https://news.daum.net"
        soup = create_soup(URL)  # 뷰티플 숩 객체 만들기

        box_headline = soup.find("div", {"class": "box_headline"})
        lis = box_headline.select('ul > li')
        i = 1

        for li in lis:
            content = li.find_all('strong')
            txt = content[0].text.strip().replace('\n', " / ")
            link = li.find('a').get('href')
            result += f'{i}. {txt} / {link}\n\n'
            i += 1
        bot.send_message(message.chat.id, result)

    except Exception as e:
        bot.send_message(message.chat.id, '뉴스 정보 수집 중 오류가 발생했습니다.')

bot.polling()
