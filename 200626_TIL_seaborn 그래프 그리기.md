# 200626_TIL_seaborn 그래프 그리기
#코딩/TIL #판다스/그래프
## 시본 바플롯 그리기
``` python
import seaborn as sns

plt.figure(figsize=(15, 4))
plt.xticks(rotation = 60)
sns.barplot(data=df, x="연도 (년)", y="추계인구(명)")

```

## 시본 포인트플롯 그리기
``` python
import seaborn as sns

plt.figure(figsize=(15, 4))
plt.xticks(rotation = 60)
sns.pointplot(data=df, x="연도 (년)", y="추계인구(명)")

```

## 시본 라인플롯 그리기
``` python
import seaborn as sns

plt.figure(figsize=(15, 4))
plt.xticks(rotation = 60)
sns.lineplot(data=df, x="연도 (년)", y="추계인구(명)")

```

##  특이사항.
	* 라인플롯의 경우 x축의 값이 모두 나타나지 않음.
	* 포인트 플롯 및 바플롯 같은경우 x축의 값이 모두 나타남