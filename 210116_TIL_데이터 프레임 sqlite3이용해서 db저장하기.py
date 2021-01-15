import sqlite3

# csv 파일 불러오기
df_bigdata = pd.read_csv(big_data)

# 인덱스 행 삭제
del df_bigdata['Unnamed: 0']

# 데이터 베이스 접속
con = sqlite3.connect("/Users/mac/Documents/문서 - 951237's 2017 Macbook Pro/coding_insa2020/db_insa.db")

# DB의 스키마에 맞게 칼럼 이름 바꾸기
df_bigdata.columns = ['city', 'school', '_name', 'age', 'sex', 'grade', 'prize', 'chridren', 'charge', 'etc', 'total', 'total_score', 'pre', 'new_reg', 'fir_hope', 'sec_hope', 'third_hope', 'forth_hope', 'code_year', 'code_type']

# DB에 붙여넣기(기존에 DB가 있을경우에)
df_bigdata.to_sql('db_2013_2019', con, index=False, index_label=False,if_exists='append')
