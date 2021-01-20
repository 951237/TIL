import pandas as pd

PATH_FILE = "/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_TIL/data/데이터_발열근무자명단.csv"
PATH_SAVE = "/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_TIL/result/200915_TIL_발열근무조 횟수 카운트.csv"

df = pd.read_csv(PATH_FILE) #근무자 명단 가져오기
df.columns = ['team', 'date', 'name1', 'name2', 'name3'] # 명단 칼럼 만들기
concat_name = pd.concat([df['name1'], df['name2'], df['name3'].dropna()]) # 이름칼럼 하나의 칼럼으로 합치기 / 빈값이 있는
list_name = concat_name.unique() # 합친 명단에서 요소 추출하여 리스트로 저장
list_team = concat_name.tolist() # 전체 명단 시리즈를 리스트로 변환
# 리스트의 요소를 카운트
for name in list_name:
    count = list_team.count(name)
    print(f'{name} : {count}')

# 데이터 프레임 생성 / 헤더[이름, 카운트]
df_result = pd.DataFrame()
df_result['name'] = 1   # name 칼럼 생성
df_result['count'] = 1  # count 칼럼 생성
df_result['name'] = df_result['name'].astype(str) # name칼럼 str타입으로 변경

# 이름과 카운트를 기록하기
for i, name in enumerate(list_name):
    count = list_team.count(name)
    df_result.at[i, 'name'] = name  # name는 칼럼 이름
    df_result.at[i, 'count'] = count    # 'count'는 칼럼 이름

# 결과 csv파일로 저장하기
df_result.to_csv(PATH_SAVE)