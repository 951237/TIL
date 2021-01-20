import matplotlib.pyplot as plt
import pandas as pd

df_all = df[(df["시군구별"] == "전국") & (df["성별"] == "전체")] 	# 데이터 프레임 필터링

# 원하는 칼럼만 추출하여 데이터 프레임을 만듦. 다만 카피해서 만들기
df_all = df_all[["연도", "월", "출생아수"]].copy


plt.rc("font", family="AppleGothic") 	# 맥 쥬피터에서 글꼴 잡아 설정하기
plt.rc("font", family="Malgun Gothic") 	# 윈도우 쥬피터에서 글꼴 잡아 설정하기

df_all.set_index(["연도", "월"]).plot(figsize=(15, 4))
# 인덱스를 2개 칼럼으로 설정하고 그래프 그리기 / 크기도 정해줌.
# 인덱스를 2개를 설정할 경우 "연도"칼럼이 겹치는 반복되고 겹치는 경우 예를 들면 연도

df_all[-24:].set_index(["연도", "월"]).plot.bar(figsize=(15, 4))		#최근 24개의 데이터만을 가지고 그래프 그리기
