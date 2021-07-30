# 2가지 이상의 조건 적용하여 필터링 하기
df.loc[(df['con1'] == 'con1') & (df['con2'] == 'con2') & (df['con3'] > 70)]

# 문자열 포함된 값 필터링
df.loc[df['Name'].str.contains('Mega')]

# regex 이용하여 필터링 하기
df.loc[df['Name'].str.contains('fire|glass', regex = True)]  # 불린연산자 '|'를 사용함.

# regex 이용하여 필터링 하기 2
df.loc[df['Name'].str.contains('pi[a-z]', flags=re.I, regex = True)] # pi로 시작하는 문자열이 포함된 것을 찾기

# 조건에 맞는 것을 칼럼에 결과를 표시
df.loc[df['type 1'] == 'Fire', 'Legendary'] = True  # type1이 fire면 legendary 칼럼에 true 값을 표시
