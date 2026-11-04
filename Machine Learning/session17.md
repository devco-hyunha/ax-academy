# 세션 17: 하이퍼파라미터 튜닝 — GridSearchCV & RandomizedSearchCV

<!-- session-nav -->
**이동:** [← 세션 16](./session16.md) · [세션 18 →](./session18.md)

session16에서 DecisionTree·RandomForest·GradientBoosting·XGBoost 같은 **트리 회귀기**를 배웠습니다.  
오늘은 그 모델들(과 Ridge·Lasso)의 **손잡이(하이퍼파라미터)** 를 어떻게 고를지 —  
**GridSearchCV**와 **RandomizedSearchCV**로 탐색하는 방법을 봅니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 오늘은 모델의 **설정값(하이퍼파라미터)** 을 고르는 법을 배웁니다.  
> **하이퍼파라미터** = 학습 전에 사람이 정하는 숫자입니다. (예: 나무 깊이, 나무 개수)  
> 집값 데이터로 **전부 다 해보기(Grid)** 와 **몇 개만 뽑아 보기(Random)** 를 비교합니다.  
> 기억할 한 줄: **먼저 Random으로 넓게 → 그다음 Grid로 좁게**.

---

## 1. 하이퍼파라미터란 / 왜 튜닝하는지

- **파라미터(Parameter)**: 학습 중에 데이터가 정해 주는 값 (예: 회귀의 기울기·절편)
- **하이퍼파라미터(Hyperparameter)**: 학습 **전에** 사람이 정해 두는 손잡이  
  (예: `max_depth`, `n_estimators`, `alpha`)
- 손잡이를 잘못 잡으면 과적합·과소적합·느린 학습이 납니다.  
  그래서 **검증(CV)** 점수로 여러 조합을 비교해 고릅니다.

> **쉽게 이해하기**  
> **하이퍼파라미터**는 학습 **전**에 사람이 정하는 설정(나무 깊이 등)입니다.  
> 잘못 잡으면 과하게 외우거나 너무 단순해집니다.  
> 교차검증 점수로 여러 조합을 비교해 고르시면 됩니다.

---

## 2. GridSearchCV: 격자 전수 탐색

- 지정한 후보값을 **격자(grid)** 로 만들고, **모든 조합**을 교차검증합니다.
- `best_params_`, `best_estimator_`로 최고 조합·모델을 꺼냅니다.
- 후보가 많으면 조합 수가 급증해 **시간이 오래** 걸립니다.

```python
# 스케치: 격자 전수 탐색
from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(
    estimator=model,
    param_grid={"max_depth": [3, 5, 7], "n_estimators": [100, 200]},
    scoring="neg_mean_squared_error",
    cv=5,
    n_jobs=-1,
)
grid.fit(X_train_scaled, y_train)
print(grid.best_params_)
```

> **쉽게 이해하기**  
> **GridSearchCV(격자 탐색 교차검증)** 는 정해 둔 설정 조합을 **전부** 교차검증하는 도구입니다.  
> 정확하지만 조합이 많으면 시간이 오래 걸립니다.

---

## 3. RandomizedSearchCV: 무작위 n_iter번

- 후보 분포·목록에서 **무작위**로 `n_iter`번만 뽑아 교차검증합니다.
- 넓은 범위를 **빠르게 훑을** 때 유리합니다.
- 운이 나쁘면 최적 근처를 못 건드릴 수 있어,  
  보통 이후에 Grid로 **주변을 촘촘히** 다시 봅니다.

```python
# 스케치: 무작위 n_iter번
from sklearn.model_selection import RandomizedSearchCV

rand = RandomizedSearchCV(
    estimator=model,
    param_distributions={"max_depth": [3, 5, 7, 9], "n_estimators": [50, 100, 200, 300]},
    n_iter=10,
    scoring="neg_mean_squared_error",
    cv=5,
    n_jobs=-1,
    random_state=42,
)
rand.fit(X_train_scaled, y_train)
print(rand.best_params_)
```

> **쉽게 이해하기**  
> **RandomizedSearchCV(무작위 탐색 교차검증)** 는 후보 중 **n_iter번만** 뽑아 시험합니다.  
> 넓은 범위를 빨리 훑어 유망 구간을 찾을 때 씁니다.

---

## 4. 실무 흐름: 넓게 Randomized → 좁혀 Grid

1. **RandomizedSearchCV**로 넓은 범위를 `n_iter`번 훑어 유망 구간을 찾습니다.
2. 그 근처만 후보로 줄여 **GridSearchCV**로 촘촘히 전수 탐색합니다.
3. 최종 모델로 **테스트셋** 점수(예: R²)를 한 번만 확인합니다.

> **쉽게 이해하기**  
> 먼저 **RandomizedSearchCV**로 넓게 훑고, 좋은 구간만 **GridSearchCV**로 촘촘히 찾습니다.  
> 처음부터 모든 조합을 다 보면 시간이 너무 오래 걸립니다.

---

## 5. scoring=`neg_mean_squared_error`인 이유

- **MSE(Mean Squared Error)** 는 오차 제곱 평균이라 **작을수록** 좋습니다.
- 그런데 sklearn의 `scoring` 규칙은 “**클수록** 좋다”입니다.
- 그래서 MSE에 **마이너스**를 붙인 `neg_mean_squared_error`를 씁니다.  
  (점수가 −4보다 −1이 “더 크다” → 실제로 MSE가 더 작은 쪽)

> **쉽게 이해하기**  
> **MSE(평균 제곱 오차)** 는 작을수록 좋습니다.  
> 사이킷런 `scoring`은 클수록 좋게 되어 있어 **`neg_mean_squared_error`**(음수 MSE)를 씁니다.  
> 실제 오차가 작을수록 점수가 0에 가까워집니다.

---

## 6. StandardScaler는 train에만 fit (누수 방지)

- 스케일링의 평균·표준편차는 **학습 데이터만**으로 `fit`합니다.
- 테스트(또는 검증 폴드 밖) 정보를 미리 쓰면 **데이터 누수(Data Leakage)** 가 됩니다.
- 이후 `transform`만 train/test에 적용합니다.

```python
# 스케치: train에만 fit
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit은 train만
X_test_scaled = scaler.transform(X_test)        # test는 transform만
```

> **쉽게 이해하기**  
> **StandardScaler(표준 스케일러)** 의 평균·편차는 **학습(train) 데이터만**으로 잡습니다.  
> **테스트(test)** 로 미리 맞추면 **데이터 누수(Data Leakage, 점수 부풀림)** 가 됩니다.

---

## 7. California housing + 다모델 튜닝

- 데이터: California housing (집값 회귀)
- 모델: Ridge, Lasso, DecisionTree, RandomForest, XGB, GradientBoosting  
  → 트리 회귀기는 [session16](./session16.md)에서 배웠고, **오늘은 탐색(튜닝)** 이 주제입니다.
- `GridSearchCV` / `RandomizedSearchCV`, `cv=5`, `scoring="neg_mean_squared_error"`
- 실습 노트북: [`Jupyter/07_california_housing_tuning.ipynb`](./Jupyter/07_california_housing_tuning.ipynb)

### GridSearchCV test_r2 (대략)

| 모델 | test_r2 (대략) |
| ---- | -------------- |
| XGB | 0.8427 |
| GradientBoosting | 0.8405 |
| RandomForest | 0.8074 |
| DecisionTree | 0.6725 |
| Lasso | 0.5769 |
| Ridge | 0.5758 |

> 수치는 실행 환경·시드·탐색 격자에 따라 조금 달라질 수 있어 **대략**으로 적습니다.  
> 대체로 트리·부스팅 계열이 선형(규제)보다 높은 편입니다.

---

## 한눈에 정리

```text
하이퍼파라미터 = 학습 전 손잡이 (깊이, 트리 수, alpha …)
GridSearchCV     = 격자 전수 탐색 (정확·느림)
RandomizedSearchCV = 무작위 n_iter번 (넓게·빠름)
실무: Random 넓게 → Grid 좁히기
scoring: neg_mean_squared_error (MSE↓인데 “클수록 좋음” 규칙에 맞추기)
StandardScaler: train에만 fit (누수 방지)
모델은 session16에서 배웠고, 오늘은 탐색
```

---

## 복습 체크 (스스로)

1. 하이퍼파라미터와 (학습) 파라미터의 차이는 무엇인가요?
2. GridSearchCV와 RandomizedSearchCV의 차이는?
3. 왜 `neg_mean_squared_error`를 쓰나요?
4. StandardScaler를 train에만 `fit`하는 이유는?
5. 실무에서 Random 다음에 Grid를 쓰는 이유는?

<details>
<summary>답 보기</summary>

1. 하이퍼파라미터는 학습 **전**에 정하는 손잡이, 파라미터는 학습 **중**에 데이터가 정하는 값.
2. Grid는 모든 조합 전수, Random은 `n_iter`번만 무작위 탐색.
3. MSE는 작을수록 좋은데 sklearn scoring은 클수록 좋아서, 부호를 뒤집은 지표를 씀.
4. 테스트 분포를 미리 보면 누수가 되어 점수가 과장됨.
5. 넓은 범위를 빨리 좁힌 뒤, 유망 구간만 촘촘히 전수 탐색하기 위함.

</details>

<!-- session-nav -->
**이동:** [← 세션 16](./session16.md) · [세션 18 →](./session18.md)
