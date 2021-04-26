import pandas as pd
import tqdm

# 데이터 찾기
    # 기상청 기상자료 개방포털에서 수집
    # https://data.kma.go.kr/data/grnd/selectAwosRltmList.do?pgmNo=638
    # 파일 경로
PATH_SRC = 'coding_TIL/TIL_2021/210426_데이터셋_2020년 기온 데이터_강수량 프로젝트.csv'

df = pd.read_csv(PATH_SRC, encoding='cp949')
print(df)
# 강수량으로 비가온 날짜 추출
# 카운트 하기
# 월별 강수량 그래프 출력

