import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
!pip install mglearn

X, y = mglearn.datasets.make_wave(n_samples=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

lr = LinearRegression().fit(X_train, y_train)

# 가중치와 편향 구하기
print(f"lr.coef_ : {lr.coef_}")
print(f"lr.intercept_ : {lr.intercept_}")

# 테스트, 훈련세트 성틍
print(f"train score : {lr.score(X_train, y_train)}")
print(f"train score : {lr.score(X_test, y_test)}")
print()
련
# 데이터를 바꾸어서 훈련
X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

lr = LinearRegression().fit(X_train, y_train)

print(f"LR train score : {lr.score(X_train, y_train)}")
print(f"LR test score : {lr.score(X_test, y_test)}")
