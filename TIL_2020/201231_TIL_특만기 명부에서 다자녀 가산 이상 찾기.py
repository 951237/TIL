# 특만기 명부에서 다자녀 가산 이상 찾기
df = pd.read_excel(PATH_LOAD, sheet_name='특만기_명부')
df_child = df.loc[(df['현임교_근무년수'] == 5) & (df['가점_세자녀'] >= 1.9)]
df_child.to_excel('다자녀_특만기.xlsx')
