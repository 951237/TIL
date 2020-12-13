# 특기사항에 결측값 있는 행 삭제
df_etc = df.dropna(subset=['특기사항']).copy()    

# 특기사항에 '파견'포함 필터링
파견 = df_etc["특기사항"].str.contains('파견', regex=True)

# 원하는 데이터만으로 데이터 프레임 만들기
df_etc = df_etc.loc[파견, ['지역', '소속', '이름', '주민번호', '성별', '근무성적','특기사항']]

# 결과물 CSV파일로 만들기
df_etc.to_csv(RESULT_PATH)
