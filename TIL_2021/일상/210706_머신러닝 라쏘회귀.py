from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import numpy as np
import mglearn

# 데이터셋 불러오기
X, y = mglearn.datasets.load_extended_boston()

# 훈련데이터와 테스트 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 라소객체 생성후 훈련하기
lasso = Lasso().fit(X_train, y_train)

# 성능테스트 
print(f"훈련세트 점수 : {lasso.score(X_train, y_train)}")
print(f"테스트세트 점수 : {lasso.score(X_test, y_test)}")
print(f"사용한 특성 수 : {np.sum(lasso.coef_ != 0)}")

# 과소적합 줄이기 alpha = 0.01
lasso001 = Lasso(alpha = 0.01, max_iter = 100000).fit(X_train, y_train)

# 성능테스트 
print(f"훈련세트 점수 : {lasso001.score(X_train, y_train)}")
print(f"테스트세트 점수 : {lasso001.score(X_test, y_test)}")
print(f"사용한 특성 수 : {np.sum(lasso001.coef_ != 0)}")

