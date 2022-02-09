import pandas as pd
import numpy as np
import os
import time

# 데이터 프레임 칼럼을 넓혀서 글자 모두 보기 설정하기
# pd.set_option('display.max_columns', None)
# pd.set_option('display.expand_frame_repr', False)
# pd.set_option('max_colwidth', -1)

# 안산교육지원청 웹페이지 딕셔너리
dic_ansan_eduSupportOffice = {
    'A': '초등교육지원과',
    'B': '중등교육지원과',
    'C': '평생교육건강과',
    'D': '경영지원과',
    'E': '학교현장지원과',
    'F': '교육시설과',
    'G': '교육시설관리센터'
}
# 기초코드
'''
URL = "http://www.goeas.kr/USR/ORG/MNU6/OrgDetail.do?orgType=A"
html_src = pd.read_html(URL)    
df_all = pd.concat(html_src)

'''

# 오늘 날짜 구하기
timestr = time.strftime("%Y%m%d-%H%M%S")

# 경로설정하기
base_dir = "/Users/mac/Documents/coding_result"
file_name = f"안산교육지원청 업무분장_{timestr}.xlsx"
xlsx_dir = os.path.join(base_dir, file_name)


# 여러개의 시트에 엑셀파일로 저장하기
with pd.ExcelWriter(xlsx_dir) as writer:
    for k, v in dic_ansan_eduSupportOffice.items():
        URL = f"http://www.goeas.kr/USR/ORG/MNU6/OrgDetail.do?orgType={k}"
        print(f"{v} 페이지 크롤링 시작!")
        html_src = pd.read_html(URL)
        df_temp = pd.concat(html_src)
        df_temp.to_excel(writer, sheet_name=f'{v}')
        print(f'{v}엑셀시트 생성 완료!', '\n')
