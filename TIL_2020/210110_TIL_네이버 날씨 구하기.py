import urllib
from urllib import parse
import json 
import requests
import time
import requests
from bs4 import BeautifulSoup
import lxml

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content
    
def create_soup(p_url):
    # 유저에이전트 설정 - what is my user-agent 검색
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    #                   "Chrome/87.0.4280.88 Safari/537.36"
    #     }

    # 링크 정보 받아오기
    res = requests.get(p_url)   # header = headers → 크롤링이 안될때 헤더 넣기
    res = requests.get(p_url)
    res.raise_for_status()  # 정보가 없으면 프로그램 종료

    soup = BeautifulSoup(res.text, "lxml")
    return soup
    
def today_weather():
    result = []
    newline ='\n'
    result.append(f"===== 오늘의 안산 날씨 =====")
    URL = 'https://n.weather.naver.com/today/02271103'
    soup = create_soup(URL)
    div = soup.find("div", attrs={"class": "today_weather"})  # 날씨 전체 구쳑 선택
    weather_area = div.find("div", attrs={"class": "weather_area"})  # 오늘의 날씨 요약 선택
    
    try:
        summary = weather_area.find("p", {"class": "summary"}).get_text().strip().replace('\n', " / ")    # 날씨 한줄 정리
        current_degree = weather_area.find("strong", attrs={"class": "current"}).get_text().replace('현재 온도', '')  # 현재온도
        degree_feel = weather_area.find_all("dd", attrs={"class": "desc"})[3].get_text()  # 체감온도
        result.append(f'날씨 요약 : {summary}{newline}현재온도 : {current_degree} /  체감온도 : {degree_feel}')

    except Exception as e:
        print('예외가 발생했습니다.', e)

    try:
        ttl_areas = div.find_all('div', attrs={"class": "ttl_area"})  # 세부날씨 정보
        charts = div.find_all('div', attrs={"class": "level_text"})  # 세부날씨 수치
       
        dust = ttl_areas[0].find("em", {"class": "level_text"}).get_text()  # 미세먼지
        cho_dust = ttl_areas[1].find("em", {"class": "level_text"}).get_text()  # 초미세먼지
        sun = ttl_areas[2].find("em", {"class": "level_text"}).get_text()   # 자외선 값

        result.append(f'미세먼지 : {dust} / 초미세먼지 : {cho_dust} / 자외선 : {sun}{newline}')
        return result

    except:
        return ["오류 : 오늘의 날씨 세부정보"]

today_weather()
