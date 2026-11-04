# 세션 14: 문제 2 — California Housing (선형·다중 회귀)

<!-- session-nav -->
**이동:** [← 세션 13](./session13.md) · [세션 15 →](./session15.md)

> **이 세션이 하는 일 (쉬운 말)**  
> 캘리포니아 주택 데이터로 **집값(숫자)** 을 맞추는 **회귀** 과제를 합니다.  
> 먼저 **원인 하나**(단변수 선형)로 연습한 뒤, **원인 여러 개**(다중선형)로 넓히고  
> **R²**로 얼마나 잘 맞는지 비교·시각화합니다.

## 데이터

| 구분 | 내용 |
| ---- | ---- |
| 첨부 파일 | `fetch_california_housing.csv` |
| 권장 경로 | `Machine Learning/data/fetch_california_housing.csv` |
| Kaggle | https://www.kaggle.com/datasets/sooyoungher/california-housing?resource=download |

- 대안: `sklearn.datasets.fetch_california_housing(as_frame=True)`
- sklearn 다운로드가 403 등이면 CSV/Kaggle 사용
- Jupyter 실행 시 데이터는 `../data/fetch_california_housing.csv`로 읽음

> **쉽게 이해하기**  
> 한 줄은 캘리포니아 한 구역의 주택·인구 정보입니다.  
> 소득 중앙값, 방 수 같은 **특징(입력)** 과 맞출 **집값(목표)** 이 함께 있습니다.  
> 인터넷 다운로드가 막히면 파일을 받아 `data/`에 두시면 됩니다.  
> 노트북에서는 `../data/fetch_california_housing.csv`로 읽습니다.

---

## 요구사항 체크리스트

1. 데이터 불러오기
2. 결측치 확인 + 데이터 내용 확인
3. 훈련/테스트 분할
4. 선형 회귀 학습
5. 평가 (결정계수 R²)
6. 시각화
7. 다중선형회귀도 평가

> **쉽게 이해하기**  
> 아래 순서대로 진행하시면 됩니다.  
> 1. **불러오기**: 표로 올려야 열을 고르고 모델에 넣을 수 있습니다.  
> 2. **확인**: `info`와 결측 합으로 빈칸·열 종류를 먼저 봅니다.  
> 3. **분할**: 학습용과 아직 보지 않은 테스트용으로 나눕니다.  
> 4. **선형 회귀**: 원인 하나일 때 집값과 **직선** \( y = wx + b \)으로 맞춥니다.  
> 5. **R²(결정계수)**: 집값 변동을 모델이 얼마나 설명하는지 봅니다. 1에 가까우면 잘 맞춘 편이고, 0 근처면 평균만 찍은 수준입니다.  
> 6. **시각화**: 실제 점과 예측 직선을 겹쳐 기울기·흩어짐을 눈으로 확인합니다.  
> 7. **다중선형**: 원인을 여러 개 넣고, 단변수 R²와 비교해 설명력이 나아졌는지 봅니다.

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

> **쉽게 이해하기**  
> 코드 순서는 표 읽기 → `info`·결측 확인 → X에 열 하나(단변수) 또는 여러 개(다중) → 분할·학습·예측 → `r2_score` 출력 → 단변수면 산점도와 직선을 그립니다.  
> 다중일 때는 원인 하나 대 집값 그림이 어려우니 **R² 비교**가 핵심이고, 예측값 대 실제값 산점도로 그릴 수 있습니다.  
> **단변수**는 원인 하나로 직선, **다중**은 원인 여러 개를 한꺼번에 맞추며, 클래스는 같고 X 열 개수만 달라집니다.

---

## 복습 체크 (스스로)

1. 이 세션의 목표는 분류인가요, 회귀인가요? 무엇을 맞추나요?
2. 결측·`info`를 먼저 보는 이유는 무엇인가요?
3. R²가 “대략” 의미하는 바는 무엇인가요?
4. 단변수 선형과 다중선형의 차이는 무엇인가요? 왜 R²를 비교하나요?

<details>
<summary>답 보기</summary>

1. **회귀**입니다. 집값(연속 숫자)을 맞춥니다. (예/아니오 분류가 아닙니다.)
2. 빈칸·열 타입·데이터 모양을 모르고 학습하면, 이상한 결과의 원인을 찾기 어렵기 때문입니다.
3. 모델이 목표값의 변동을 얼마나 설명하는지에 가까운 점수. 1에 가까울수록 잘 맞는 편입니다.
4. 단변수 = 원인 1개(직선). 다중 = 원인 여러 개. 정보가 늘었을 때 설명이 나아지는지 R²로 비교합니다.

</details>

<!-- session-nav -->
**이동:** [← 세션 13](./session13.md) · [세션 15 →](./session15.md)
