# 갑만기 명부에서 부부 가산 이상 찾기
df = pd.read_excel(PATH_LOAD, sheet_name='갑만기_명부')
df_bubu = df.loc[(df['현임교발령일'].str[-2:] != '01') & (df['가점_부부'] != 0)]    # 현임교 발령일이 '01'이 아니고 부부가점이 0점이아닌 것 필터
df_child.to_excel('부부_갑만기.xlsx')
