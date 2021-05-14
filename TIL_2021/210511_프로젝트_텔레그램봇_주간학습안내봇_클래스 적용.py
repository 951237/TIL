# 라이브러리 및 api 설정
import telebot
import requests
from bs4 import BeautifulSoup

API_KEY = '1644820427:AAEllDn4xGfRAFHGpb9lFxx5QsK-__AG7L8'
bot = telebot.TeleBot(API_KEY)
chid_id = '428116987'

dic_class_url_12 = {
    '11': 'http://www.asbugok.es.kr/board.list?mcode=272635&cate=272635',
    '12': 'http://www.asbugok.es.kr/board.list?mcode=272642&cate=272642',
    '13': 'http://www.asbugok.es.kr/board.list?mcode=272710&cate=272643',
    '14': 'http://www.asbugok.es.kr/board.list?mcode=272711&cate=272645',
    '21': 'http://www.asbugok.es.kr/board.list?mcode=272636&cate=272636',
    '22': 'http://www.asbugok.es.kr/board.list?mcode=272638&cate=272638',
    '23': 'http://www.asbugok.es.kr/board.list?mcode=272639&cate=272639',
    '24': 'http://www.asbugok.es.kr/board.list?mcode=272640&cate=272640'
}
dic_class_url_34 = {
    '31': 'http://www.asbugok.es.kr/board.list?mcode=272610&cate=272610',
    '32': 'http://www.asbugok.es.kr/board.list?mcode=272611&cate=272611',
    '33': 'http://www.asbugok.es.kr/board.list?mcode=272612&cate=272612',
    '34': 'http://www.asbugok.es.kr/board.list?mcode=272613&cate=272613',
    '35': 'http://www.asbugok.es.kr/board.list?mcode=272614&cate=272614',
    '41': 'http://www.asbugok.es.kr/board.list?mcode=272616&cate=272616',
    '42': 'http://www.asbugok.es.kr/board.list?mcode=272617&cate=272617',
    '43': 'http://www.asbugok.es.kr/board.list?mcode=272618&cate=272618',
    '44': 'http://www.asbugok.es.kr/board.list?mcode=272619&cate=272619',
    '45': 'http://www.asbugok.es.kr/board.list?mcode=272620&cate=272620'
}
dic_class_url_56 = {
    '51': 'http://www.asbugok.es.kr/board.list?mcode=272622&cate=272622',
    '52': 'http://www.asbugok.es.kr/board.list?mcode=272623&cate=272623',
    '53': 'http://www.asbugok.es.kr/board.list?mcode=272624&cate=272624',
    '54': 'http://www.asbugok.es.kr/board.list?mcode=272625&cate=272625',
    '55': 'http://www.asbugok.es.kr/board.list?mcode=272632&cate=272632',
    '61': 'http://www.asbugok.es.kr/board.list?mcode=272628&cate=272628',
    '62': 'http://www.asbugok.es.kr/board.list?mcode=272629&cate=272629',
    '63': 'http://www.asbugok.es.kr/board.list?mcode=272630&cate=272630',
    '64': 'http://www.asbugok.es.kr/board.list?mcode=272631&cate=272631'
}

class Crawling:
    def __init__(self, dic):
        self.dic = dic
    
    def get_jugan(self):
        for k, p_url in self.dic.items():
            result = ""
            res = requests.get(p_url, verify=False) #ssl 인증서 관련 
            res.raise_for_status()  # 정보가 없으면 프로그램 종료
            soup = BeautifulSoup(res.text, "lxml")
            # soup = BeautifulSoup(html, 'html.parser')
            class_name = soup.find("div", {"class" : "titleTop"})
            table = soup.find("table", {"class" : "boardList"})
            titles = table.find_all('td', {'class' : "title"})
            _class = class_name.find('img')['alt']  # 반이름 출력
            result += f'{_class}\n'
            try:
                title = titles[0].find('a').text    # 가장 최신의 글 저장
                result += f'{title}\n'
                # time.sleep(2)
            except:
                result += "에러발생"
        return result

@bot.message_handler(commands=['Greet'])
def greet(message):
  bot.reply_to(message, "Hey! Hows it going?")

@bot.message_handler(commands=['jugan12'])
def check_jugan12(message):
    jugan12 = Crawling(dic_class_url_12)
    result = jugan12.get_jugan()
    bot.send_message(message.chat.id, result)
bot.polling()
