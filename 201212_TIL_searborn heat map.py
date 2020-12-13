f, ax = plt.subplots(figsize = (7,7)) 	# 그래프의 크기
c = pd.crosstab(df_cho['지역'], df_cho['초빙_시군'])	# 상관관계를 알고싶은 칼럼을 표로 만들기
sns.heatmap(c, annot=True, cmap='Blues', fmt = 'g') 	# 히트맵 그래프 그리기
