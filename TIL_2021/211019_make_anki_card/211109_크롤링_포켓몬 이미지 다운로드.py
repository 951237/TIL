from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
from tqdm import tqdm
import time

# 기본 카테고리 다운로드
lst_names = []
def get_keyword(keyword):
    global lst_names
    URL = 'https://pokemon.fandom.com/wiki/' + parse.quote(keyword) # url에서 공백문자 포함하기
    
    try:
        html = urlopen(URL)
        soup = BeautifulSoup(html, 'html.parser')

        names = soup.find_all('a', {'class':'category-page__member-link'})
#         lst_names = []
        for name in names:
            temp = name.text
            if 'Category' in temp:
                lst_names.append(temp)
    except:
        print(f'{keyword} 오류발생!')

get_keyword('Category:Pokémon')
print(f'카테고리 갯수 : {len(lst_names)}개')  # 리스트 갯수 확인

# 하위 카테고리 다운로드 
lst_result=[]
def get_keyword_all(keyword):
    global lst_result
    URL = 'https://pokemon.fandom.com/wiki/' + parse.quote(keyword) # url에서 공백문자 포함하기
    
    try:
        html = urlopen(URL)
        soup = BeautifulSoup(html, 'html.parser')

        names = soup.find_all('a', {'class':'category-page__member-link'})
#         lst_names = []
        for name in names:
            temp = name.text
            if 'Category' in temp:
                lst_result.append(temp)
    except:
        print(f'{keyword} 오류발생!')

for idx, name in enumerate(tqdm(lst_names)):
    get_keyword_all(name)
print(f'모든 카테고리 갯수 : {len(lst_result)}개')

# 모든 포켓몬 이름 수집
lst_result_names=[]
def get_pocketmon_name(keyword):
    print(f'{keyword} 카테고리에서 포켓몬 이름 수집시작!')
    global lst_result_names
    URL = 'https://pokemon.fandom.com/wiki/' + parse.quote(keyword) # url에서 공백문자 포함하기
    
    try:
        html = urlopen(URL)
        soup = BeautifulSoup(html, 'html.parser')

        names = soup.find_all('a', {'class':'category-page__member-link'})
        for name in names:
            temp = name.text
            if 'Category' in temp:
                continue
            lst_result_names.append(temp)
    except:
        print(f'{keyword} 오류발생!')

for idx, name in enumerate(tqdm(lst_result)):
    get_pocketmon_name(name)
# lst_result_names
print(f'{len(lst_result_names)}개의 이름 수집 완료!')

# 포켓몬 이미지 다운로드
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup

path_target_dir = ''

def download_img(name):
    global path_target_dir
    try:
        URL = 'https://pokemon.fandom.com/wiki/' + parse.quote(name)

        html = urlopen(URL)
        soup = BeautifulSoup(html, 'html.parser')

        # 본문 찾기
        aside = soup.find('figure', {'class':'pi-item'})
        link = aside.find_all('img')[0].get('src')
        savename = f'{path_target_dir}/{name}.png'
        request.urlretrieve(link, savename)
#         print(f'{name} 다운로드 완료!')
    except:
        print(f'{name} 다운로드 실패!')

names = lst_result_names
for i, name in enumerate(names):
    download_img(name)
    print(f'{i+1}/{len(names)} : {name} 포켓몬 이미지 수집 완료!')
    time.sleep(0.5)
print(f'{len(names)}개 작업 완료!')

