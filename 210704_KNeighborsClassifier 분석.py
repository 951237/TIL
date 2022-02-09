import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# pip install mglearn
import mglearn

# 그래프 표혀ㄴ
 # mglearn.plots.plot_knn_classification(n_neighbors=1)

# 테스트 세트 후ㄴ려ㄴ세트 나누기
from sklearn.model_selection import train_test_split

X, y = mglearn.datasets.make_forge()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

# k-초ㅣ그ㄴ저ㅂ 개ㄱ체새ㅇ서ㅇ
from sklearn.neighbors import KNeighborsClassifier

# 매개벼ㄴ수 이우ㅅ 수ㅅ자에 따르ㄴ 부ㄴ서ㄱ하기
fig, axes = plt.subplots(1, 3, figsize=(10,3))

for n_neighbors, ax in zip([1, 3, 9], axes):
	# fit 메서드느ㄴ self개ㄱ체르ㄹ 바ㄴ호ㅏㄴ
	# 그래서 개ㄱ체 새ㅇ서ㅇ고ㅏ fit메ㅅㅓ드르ㄹ 하ㄴ주ㄹ에 사요ㅇ가느ㅇ
	
	clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X,y)
	mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax = ax, alpha=.4)
	mglearn.discrete_scatter(X[:,0], X[:,1], y, ax=ax)
	ax.set_title(f"{n_neighbors} neighbor")
	ax.set_xlabel("feacher0")
	ax.set_ylabel('feacher1')
axes[0].legend(loc=3) 	# display legend at first graph
