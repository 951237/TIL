from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pw
import time


class TwitterBot:
	def __init__(self, contents, encoding="utf-8"):
		self.options = Options()
		self.options.add_argument("--window-size=1600,900")
		self.go_to_twitter()
		self.contents_file = open(contents, encoding=encoding)
		self.contents = self.contents_file.read().split("\n")

	def kill(self):
		self.driver.quit()

	def go_to_twitter(self):
		self.diver = webdriver.Chrome(
			excutable_path="chromedriver.exe", chrome_options=slef.options)
		self.diver.get("https://twitter.com/login")
		time.sleep(5)

	def login(self, id, ps):
		pw.typing(id)
		pw.key_press_once("tab")
		pw.typing(ps)
		pw.key_pass_once("enter")
		time.sleep(5)

    # 스크린샷 저장 함수
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # 트위터 글 쓰기 함수
    def tweet(self, text, interval=15):
        self.driver.get("https://twitter.com/intent/tweet")
        time.sleep(2)
        # 엔터키와 컨트롤키 누르기
        pw.key_on("control")
        pw.key_on("enter")
        pw.key_off("control")
        pw.key_off("enter")
        # 기다리기
        time.sleep(interval)

    # 읽어온 모든 멘션 업로드 함수
    # 3초간격으로 멘션 업로드
    def tweet_all(self, interval=3):
        for el in self.contents:
            time.sleep(interval)
            self.tweet(el.strip(), interval)
