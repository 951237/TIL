from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify = cancer.target, random_state = 1 )


logreg = LogisticRegression().fit(X_train, y_train)
print(f"훈련세트 점수 : {logreg.score(X_train, y_train)}")
print(f"테스트세트 점수 : {logreg.score(X_test, y_test)}")

# 제약 풀기 C 값이 높을경우, 제약강화 :  C 값이 낮을 경우
logreg100 = LogisticRegression(C=100).fit(X_train, y_train)
print(f"훈련세트 점수 : {logreg100.score(X_train, y_train)}")
print(f"테스트 점수 : {logreg100.score(X_test, y_test)}")

