# 200704_TIL_데이터 시각화 seaborn

```python

import seaborn as sns

# lineplot 그리기
plt.figure(figsize=(15, 4))
sns.lineplot(data = df_all, x=“월”, y=“출생아수”, ci = None)	# ci는 시본에서 년도별 1월에서 12월까지의 평균을 구해서 자체적으로 통계처리를 하는데, none처리를 하면 달리 하지 않음.

# barplot 그리기
plt.figure(figsize=(15, 4))
sns.barplot(data=df_all, x=“월”, y=“출생아수”, ci=None)

```
