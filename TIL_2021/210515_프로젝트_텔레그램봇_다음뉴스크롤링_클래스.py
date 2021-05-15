# 라이브러리 및 api 설정
import telebot
import requests
from bs4 import BeautifulSoup

API_KEY = ''
bot = telebot.TeleBot(API_KEY)
chid_id = '428116987'

class Crawling:
    def __init__(self, url):
        self.url = url

    def get_soup(self):
        res = requests.get(self.url, verify=False)  # ssl 인증서 관련
        res.raise_for_status()  # 정보가 없으면 프로그램 종료
        soup = BeautifulSoup(res.text, "lxml")
        return soup
    
    def get_news(self):
        soup = self.get_soup()
        try:
            result = ""
            result += f"===== 이시간 주요 뉴스 =====\n"
            box_headline = soup.find("div", {"class": "box_headline"})
            lis = box_headline.select('ul > li')
            i = 1
            for li in lis:
                content = li.find_all('strong')
                txt = content[0].text.strip().replace('\n', " / ")
                link = li.find('a').get('href')
                result += f'{i}. {txt} / {link}\n'
                i += 1
            return result

        except Exception as e:
            return '뉴스 정보 수집 중 오류가 발생했습니다.'

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")


@bot.message_handler(commands=['news'])
def today_news(message):
    URL = "https://news.daum.net"
    news = Crawling(URL)  # 뷰티플 숩 객체 만들기
    result = news.get_news()
    bot.send_message(message.chat.id, result)
        
bot.polling()
