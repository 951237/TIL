import requests
from bs4 import BeautifulSoup


def create_soup(p_url):
    # 유저에이전트 설정 - what is my user-agent 검색
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        }

    # 링크 정보 받아오기
    res = requests.get(p_url, headers=headers)
    res.raise_for_status()  # 정보가 없으면 프로그램 종료

    soup = BeautifulSoup(res.text, "lxml")
    return soup

def today_news():
    print("오늘의 헤드라인 뉴스")
    URL = "https://news.daum.net"
    soup = create_soup(URL)
    news = soup.find("ol", attrs={"class" : "list_popcmt"}).find_all("li")
    for i, item in enumerate(news[:3]):
        title = item.find('a', attrs={"class": "link_txt"}).get_text().replace("                            ",
                                        "")[4:].strip()
        link = item.find('a', attrs={"class": "link_txt"})['href']
        from_news = item.find('span', attrs={"class":"info_news"}).get_text()
        print(f'{i+1}위: {title}({from_news}) / {link}')
    print()

def today_weather():
    print("오늘의 날씨")
    URL = "https://n.weather.naver.com/today/02590140"
    soup = create_soup(URL)
    div = soup.find("div", attrs={"class" : "today_weather"})
    weather_area = div.find("div", attrs={"class" : "weather_area"})
    current_degree = weather_area.find("strong", attrs={
        "class":"current"}).get_text() # 현재온도
    degree_height = weather_area.find("strong", attrs={
        "class":"degree_height"}).get_text() # 최고온도
    degree_low = weather_area.find("strong", attrs={
        "class":"degree_low"}).get_text() #최저온도
    degree_feel = weather_area.find("strong", attrs={
        "class":"degree_feel"}).get_text() #체감온도
    print(current_degree, degree_height, degree_low, degree_feel)

    ttl_areas = div.find_all('div', attrs={"class":"ttl_area"})
    charts = div.find_all('div', attrs = {"class" : "chart"})

    #미세먼지
    dust = ttl_areas[1].find("em", {"class" : "level_text"}).get_text()
    value = charts[0].find("strong", {"class":"value"}).get_text()
    #초미세먼지
    cho_dust = ttl_areas[2].find("em", {"class" : "level_text"}).get_text()
    cho_value = charts[1].find("strong", {"class":"value"}).get_text()
    #자외선
    sun = ttl_areas[3].find("em", {"class" : "level_text"}).get_text()
    sun_value = charts[2].find("strong", {"class":"value"}).get_text()

    print(f'미세먼지 : {dust}({value}) / 초미세먼지 : {cho_dust}({cho_value}) / 자외선 : '
          f'{sun}({sun_value}) ', '\n')

def today_english():
    pass

if __name__ == "__main__":
    today_news()
    today_weather()
    # today_english()