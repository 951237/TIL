import requests
from bs4 import BeautifulSoup

# 유저에이전트 설정 - what is my user-agent 검색
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

# 다음영화 순위 링크
URL = "https://search.daum.net/search?w=tot&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

#링크 정보 받아오기
res = requests.get(URL, headers=headers)
res.raise_for_status()  #정보가 없으면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")

#다음영화 순위 정보 모두 찾기
movies = soup.find_all("div", attrs={"class" : "wrap_cont cont_type2"})

for movie in movies:
    title = movie.find("a", attrs={"class":"tit_main"}).get_text() #영화제목
    rate = movie.find("em", attrs={"class":"rate"}) #평점
    if rate:
        rate = rate.get_text()
    else:
        # rate = "No data"
        continue

    base = movie.find_all('dd', attrs={"class":"cont"}) #0-예매 / 1-개봉일 / 2-누적관객수
    rev = base[0].get_text() #예매율
    open_day = base[1].get_text()   #개봉일
    if len(base) < 3:   #개봉을 안 한 경우 예외처리
        # seen_people = "No data"
        continue
    else:
        seen_people = base[2].get_text()

    if int(seen_people[0:-1].replace(',','')) > 1000000:
        print(f"영화제목 : {title}")
        print(f"개봉일 : {open_day}")
        print(f"평점 : {rate}")
        print(f"누적관객수 : {seen_people}")
        print("*" * 100)



