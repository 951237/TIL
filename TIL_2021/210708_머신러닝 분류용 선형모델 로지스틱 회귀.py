from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify = cancer.target, random_state = 1 )


logreg = LogisticRegression().fit(X_train, y_train)
print(f"훈련세트 점수 : {logreg.score(X_train, y_train)}")
print(f"테스트세트 점수 : {logreg.score(X_test, y_test)}")

# 제약 풀기 C 값이 높을경우, 제약강화 :  C 값이 낮을 경우
print(f"훈련세트 점수 : {logreg100.score(X_train, y_train)}")
print(f"테스트 점수 : {logreg100.score(X_test, y_test)}")

# L1 규제 사용
for c, marker in zip([0.01, 1, 100], ['o', '^', 'v']):

	lr_l1 = LogisticRegression(C=c, penalty='l2').fit(X_train, y_train)
	print(f"c= {c}인 l1 로지스틱 회귀훈련 정확도 : {lr_l1.score(X_train, y_train)}")
	print(f"c= {c}인 l1 로지스틱 회귀테스트 정확트 : {lr_l1.score(X_test, y_test)}", "\n")

	plt.plot(lr_l1.coef_.T, marker, label=c)

plt.xticks(range(cancer.data.shape[1]), cancer.feature_names, rotation=90)
plt.hlines(0, 0, cancer.data.shape[1])
plt.xlabel("특성")
plt.ylabel("계수크기")
plt.ylim(-5, 5)
plt.legend(loc=3)
