# 라이브러리 및 api 설정
import telebot
import requests

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
@bot.message_handler(commands=['jugan12'])
def check_jugan12(message):
    result = ""
    res = requests.get(p_url, verify=False) #ssl 인증서 관련 
    res.raise_for_status()  # 정보가 없으면 프로그램 종료
    soup = BeautifulSoup(res.text, "lxml")
    # soup = BeautifulSoup(html, 'html.parser')
    class_name = soup.find("div", {"class" : "titleTop"})
    table = soup.find("table", {"class" : "boardList"})
    titles = table.find_all('td', {'class' : "title"})
    _class = class_name.find('img')['alt']  # 반이름 출력
    result.append(_class)
    try:
        title = titles[0].find('a').text    # 가장 최신의 글 저장
        result.append(title)
        time.sleep(2)
    except:
        result.append('에러발생')
        time.sleep(2)
    return result
