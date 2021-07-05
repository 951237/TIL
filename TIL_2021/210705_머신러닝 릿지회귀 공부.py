# 릿지 회귀
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import mglearn

X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

ridge = Ridge().fit(X_train, y_train)
print(f"Ridge train score : {ridge.score(X_train, y_train)}")
print(f"Ridge test score : {ridge.score(X_test, y_test)}")

# 알파값을 10으로 설정 - 규제를 강화
ridge10 = Ridge(alpha=10).fit(X_train, y_train)
print(f"Ridge10 train score : {ridge10.score(X_train, y_train)}")
print(f"Ridge10 test score : {ridge10.score(X_test, y_test)}")
