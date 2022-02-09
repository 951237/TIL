# 갑만기 명부에서 다자녀 가산 이상 찾기
df = pd.read_excel(PATH_LOAD, sheet_name='갑만기_명부')
df_test = df.loc[df['가점_기타'].str[:1] != '-']    # 가점_기타에 '-'가 포함하지 않은 명단을 저장
df_test['가점_기타'] = df_test['가점_기타'].astype(float)   # '-'문자 포함으로 오브젝트 형식이었음.
df_child = df_test.loc[(df_test['현임교발령일'].str[-2:] != '01') & (df_test['가점_기타'] > 1.01)]
df_child.to_excel('다자녀_갑만기.xlsx')
