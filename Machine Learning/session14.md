# 세션 14: 문제 2 — California Housing (선형·다중 회귀)

## 데이터

| 구분 | 내용 |
| ---- | ---- |
| 첨부 파일 | `fetch_california_housing.csv` |
| 권장 경로 | `Machine Learning/data/fetch_california_housing.csv` |
| Kaggle | https://www.kaggle.com/datasets/sooyoungher/california-housing?resource=download |

- 대안: `sklearn.datasets.fetch_california_housing(as_frame=True)`
- sklearn 다운로드가 403 등이면 CSV/Kaggle 사용
- Jupyter 실행 시 데이터는 `../data/fetch_california_housing.csv`로 읽음

---

## 요구사항 체크리스트

1. 데이터 불러오기
2. 결측치 확인 + 데이터 내용 확인
3. 훈련/테스트 분할
4. 선형 회귀 학습
5. 평가 (결정계수 R²)
6. 시각화
7. 다중선형회귀도 평가

---

## 핵심 코드 스케치

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
# 대안: from sklearn.datasets import fetch_california_housing

df = pd.read_csv("../data/fetch_california_housing.csv")
df.info()
df.isnull().sum()

# 단변수 예시 (피처 1개) / 다중은 X에 여러 컬럼
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=..., random_state=...
)

regr = LinearRegression()
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)
print(r2_score(y_test, y_pred))

# 시각화 힌트: scatter(실제) + 회귀선
plt.scatter(X_test, y_test)          # 단변수일 때
plt.plot(X_test, y_pred)             # 회귀선
plt.show()
```

- session10·11(회귀·R²)과 연결 — 단변수 선형 후 다중선형으로 R² 비교
