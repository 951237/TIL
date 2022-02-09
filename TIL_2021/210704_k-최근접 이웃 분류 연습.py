import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# pip install mglearn
import mglearn

# 그래프 표혀ㄴ
mglearn.plots.plot_knn_classification(n_neighbors=1)

# 테스트 세트 후ㄴ려ㄴ세트 나누기
from sklearn.model_selection import train_test_split

X, y = mglearn.datasets.make_forge()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

# k-초ㅣ그ㄴ저ㅂ 개ㄱ체새ㅇ서ㅇ
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=3)

# 부ㄴ류모데ㄹ 하ㄱ스ㅂ
clf.fit(X_train, y_train)

# 예ㅊㅡㄱ하기
print(f"테스트 세트 예츠ㄱ : {clf.predict(X_test)}")

# 서ㅇ느ㅇ펴ㅇ가
print(f"테스ㅌ 세트 저ㅇ호ㅏㄱ도 : {clf.score(X_test, y_test)}")
