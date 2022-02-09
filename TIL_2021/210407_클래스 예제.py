import requests
from bs4 import BeautifulSoup

class ConverSation:
    # 질문, 응답 두변수로 구분
    def __init__(self, qustion, answer):
        self.question = question
        self.answer = answer
    
    def __str__(self):
        return "질문: " + self.question + "\n답변: " + self.answer + "\n"

def get_subjects():
    subjects = []

    # 전체 주제 목록을 보여주는 페이지로의 요청 객체를 생성
    req = requests.get(url)
    html = req.text
    soup = BeautifulSou(html, 'html.parser')

    divs = soup.findAll('div', {'class' : 'example'})
    for div in divs:
        # 내부의 a태그를 추출
        links = div.findAll('a')

        # a태그 내부의 텍스트를 리스트에 삽입
        for link in links:
            subject = link.text
            subjects.append(subject)
    return subjects

