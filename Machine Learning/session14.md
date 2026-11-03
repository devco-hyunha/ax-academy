# 세션 14: 문제 2 — California Housing (선형·다중 회귀)

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
> 각 줄 ≈ 한 구역(블록)의 주택·인구 통계.  
> 여러 특징(소득 중앙값, 방 수 등)과 **맞추고 싶은 집값(또는 관련 목표 열)** 이 있습니다.  
> 온라인 다운로드가 막히면(403 등) CSV/Kaggle로 받아 `data/`에 두면 됩니다.  
> Jupyter에서는 보통 `../data/fetch_california_housing.csv` 경로를 씁니다.

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
> 단계별 “왜”만 짚어 보면 다음과 같습니다.
>
> 1. **불러오기**: 표로 올려야 열을 고르고 모델에 넣을 수 있습니다.  
> 2. **확인**: `info`·결측 합계로 “빈칸 있나?”, “열 타입이 뭔가?”를 먼저 봅니다.  
>    모르는 표를 바로 학습에 넣으면, 나중에 이상한 점수만 보고 헤매기 쉽습니다.  
> 3. **분할**: 학습용과 **안 본** 테스트용을 나눕니다. (회귀도 분류와 같습니다.)  
> 4. **선형 회귀**: 단변수라면 “한 원인 → 집값”을 **직선**으로 맞춥니다.  
>    식의 느낌: \( y = wx + b \)  
> 5. **R²(결정계수)**: “이 모델이 집값 변동을 얼마나 설명하나”에 가까운 점수.  
>    1에 가까울수록 잘 맞춘 편, 0 근처면 “평균만 찍은 것”과 비슷한 수준으로 보면 됩니다.  
>    (음수도 나올 수 있음 = 평균보다도 못한 경우)  
> 6. **시각화**: 점(실제)과 직선(예측)을 겹쳐 보면, 숫자만 볼 때보다 **기울기·흩어짐**이 눈에 들어옵니다.  
> 7. **다중선형**: 원인을 여러 개 넣습니다.  
>    예측 ≈ (원인1 영향) + (원인2 영향) + … + 기본값  
>    단변수 R²와 **비교**해, 정보가 늘면 설명이 나아지는지 확인합니다.

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
> 스케치가 말하는 순서는 이렇습니다.
>
> 1. CSV(또는 sklearn fetch)로 표를 읽는다  
> 2. `info` / `isnull().sum()`으로 구조와 결측을 본다  
> 3. **단변수**: X에 열 하나 / **다중**: X에 열 여러 개  
> 4. 분할 → `LinearRegression().fit` → `predict`  
> 5. `r2_score`로 점수를 출력한다  
> 6. 단변수일 때: 산점도(실제) + 직선(예측)으로 그림을 그린다  
>
> 다중일 때는 X가 여러 차원이라, 위 스케치의 `scatter(X_test, y_test)` 한 줄만으로는  
> “원인 하나 vs 집값” 그림이 잘 안 맞을 수 있습니다.  
> 그때는 **R² 비교**가 핵심이고, 그림은 예측값 vs 실제값 산점도처럼 바꾸는 식으로 확장하면 됩니다.
>
> **단변수 vs 다중 (한 줄)**  
> 단변수 = 원인 하나로 직선.  
> 다중 = 원인 여러 개를 한꺼번에 합쳐 맞춤.  
> 같은 `LinearRegression` 클래스지만, **넣는 X의 열 개수**가 달라집니다.

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
