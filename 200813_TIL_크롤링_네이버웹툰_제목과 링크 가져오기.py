import requests
from bs4 import BeautifulSoup

URL = "https://comic.naver.com/webtoon/weekday.nhn" #네이버웹툰 홈페이지

res = requests.get(URL) # 웹페이지 정보 가져오기
res.raise_for_status()  # 웹페이지 정보를 가져오지 못할 경우 프로그램 종료


soup = BeautifulSoup(res.text, "lxml")  # soup로 파싱

cartoons = soup.find_all("a", attrs={"class" : "title"})  # 'a'태그에 'title'클래스
# 경우 모두 가져오기

for cartoon in cartoons:
    title = cartoon.get_text()  # 태그의 텍스트 가져오기
    link = cartoon['href']  # 태그의 링크 정보 가져오기
    print(f'제목 : {title}, 링크 : https://comic.naver.com{link}', '\n')