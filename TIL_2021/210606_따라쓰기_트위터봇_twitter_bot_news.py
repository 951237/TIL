from selenium import webdriver
from selenium.webdriver.chrome.option import options
import pywinmacro as pw
import time
import pyperclip


# 뉴스봇 클래스
class NewBot:
    def __init__(self):
        self.query = "https://www.google.com/search?tbm=news&q=" # 구글 검색 쿼리 앞부분
        self.option = options() # 크롬 웹드라이버 옵션 
        self.option.add_argument("--window-size = 1600, 900") # 크롬 웹드라이버 창 크기
        self.driver = webdriver.Chrome(excutable_path= "chromedriver.exe", chrome_options=self.options) # 크롬 웹드라이버 프로그램 설치 경로.  현재경로에 같이 있음. 
        self.new_list = [] # 뉴스 기사 담을 리스트
        self.new_text = "" # 뉴스 기사 텍스트 변스 

    def kill(self): # 크롬 웹드라이버 끄기 
        self.driver.quit()

    def search(self, keyword):
        self.driver.get(self.query + keyword)
        time.sleep(3)

    def refresh(self):
        pw.key_press_once("f5")

    def copy_all(self):
        pw_ctrl_a()
        time.sleep(1)
        pw_ctrl_c()
        time.sleep(1)
        pw_ctrl_c()
        time.sleep(1)
        pw_ctrl_c()
        time.sleep(1)

    def scrap_new(self):
        self.copy_all()
        self.new_text = pyperchip.paste()
        splt = self.new_text.split("\n")

        for i, line in enumerate(splt):
            if len(line.strip()) < 3:
                continue
            
            
            _list.append(new_news)
                
    def news_crawler(self, kewyword):
        self.search(keyword)
        self.scrap_new()

    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def go_to_twitter(self):
        self.driver.get("https://twitter.com/home")

    def login(self, id, ps):
        self.go_to_twitter()
        pw.typing(id)
        pw.key_press_once("tab")
        pw.typing(ps)
        pw.key_press_once("enter")
        time.sleep(5)

    def tweet(self, text, interval):
        self.driver.get("https://twitter.com/intent/tweet")
        time.sleep(2)
        pw.type_int(text)
        time.sleep(1)
        pw.key_on("control")
        pw.key_on("enter")
        pw.key_off("control")
        pw.key_off("enter")
        time.sleep(interval)

    def tweet_all(self, hashtags = "", interval=15):
        for el in self.views_list:
            self.tweet(el.strip() + " "+hashtags, interval)

    def tweet_all_news(self, keyword, hashtags=" ", interval=15):
        self.news_crawler(keyword)
        self.twitter_home()
        self.tweet_all(hashtags, interval)
        time.sleep(interval)