# 세션 19: 다이아몬드 회귀 완성

<!-- session-nav -->
**이동:** [← 세션 18](./session18.md) · [세션 20 →](./session20.md)

session18에서 Feature·이상치(IQR)를 봤습니다.  
이번 세션은 그 위에 **선형·규제 회귀**를 올리고, 점수·교차검증·가격 로그 변환까지 이어 갑니다.

실습 노트북: [`Jupyter/09_diamonds_regression.ipynb`](./Jupyter/09_diamonds_regression.ipynb)  
(전처리·EDA만 보려면 [`Jupyter/08_diamonds_eda.ipynb`](./Jupyter/08_diamonds_eda.ipynb), session18 참고)

> **이 세션이 하는 일 (쉬운 말)**  
> 다이아몬드 **가격(price)** 을 맞춥니다.  
> 전처리는 session18과 같고, 오늘은 **모델**이 중심입니다.  
> 기본 선형과 규제 모델(Ridge·Lasso·ElasticNet)을 같은 점수로 비교합니다.  
> **MSE·R²**, **교차검증**, **log1p(가격)** 까지 봅니다.

---

## 1. 전처리 요약 (session18 교차참조)

긴 설명은 session18에 있습니다. 여기선 **회귀에 들어가기 직전 체크리스트**만 적습니다.

1. diamonds 표 불러오기 (seaborn 내장 또는 CSV)
2. 숫자 칸(`carat`, `depth`, `table`, `x`, `y`, `z`) 히스토그램·박스플롯
3. **IQR 1.5**로 이상치 후보 행 제거
4. `cut` / `color` / `clarity` → **등급 순서대로** 숫자 인코딩
5. Feature / `price` 분리 → 학습·테스트 80:20
6. **StandardScaler**: 학습 표에만 `fit`, 테스트는 `transform`만

> **쉽게 이해하기**  
> session18은 데이터 정리, session19는 그 위에 가격을 맞추는 모델입니다.  
> 인코딩·표준화를 빼면 문자나 단위 차이에 모델이 흔들립니다.

---

## 2. 점수 함수 — MSE · R²

연습 표·시험 표에 대해 같은 방식으로 점수를 찍습니다.

| 지표 | 뜻 (한 줄) | 좋은 쪽 |
| ---- | ---------- | ------- |
| **MSE** | 틀린 정도를 제곱해 평균 | **작을수록** |
| **R²** | 모델이 변동을 얼마나 설명했는지 | **1에 가까울수록** |

```python
# 스케치: 연습·시험 MSE / R²를 한 번에 출력
from sklearn.metrics import mean_squared_error, r2_score

def eval_data(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    print("[Train]", mean_squared_error(y_train, model.predict(X_train)),
          r2_score(y_train, model.predict(X_train)))
    print("[Test]", mean_squared_error(y_test, model.predict(X_test)),
          r2_score(y_test, model.predict(X_test)))
```

> **쉽게 이해하기**  
> **MSE(평균 제곱 오차)** 는 작을수록 좋고, **R²(결정계수)** 는 1에 가까울수록 좋습니다.  
> 연습 점수만 좋고 시험 점수가 나쁘면 **과적합(외우기)** 신호입니다.

---

## 3. LinearRegression

- 규제 없이 직선(평면)으로 `price`를 맞춤
- 오차 제곱합을 줄이는 기본 선형 회귀
- **다중공선성** = 힌트 칸끼리 너무 비슷한 상태. 계수가 흔들릴 수 있어 → 아래 규제 모델로 이어짐

```python
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
eval_data(lr, X_train, X_test, y_train, y_test)
```

> **쉽게 이해하기**  
> **LinearRegression(선형 회귀)** 는 특징들의 가중합으로 가격을 맞추는 기본형입니다.  
> 규제가 없어 특징이 겹치면 계수가 들쭉날쭉해질 수 있습니다.

---

## 4. Ridge / Lasso / ElasticNet

**규제** = 가중치를 너무 키우지 못하게 눌러 **과적합**을 줄입니다.  
보통 **표준화한 X**에 맞춥니다. (`alpha`가 클수록 규제가 셉니다.)

| 모델 | 누르는 방식 | 느낌 (한 줄) |
| ---- | ----------- | ------------ |
| **Ridge** | 가중치 **제곱** | 전체를 고르게 작게 |
| **Lasso** | 가중치 **절대값** | 덜 중요한 칸을 0에 가깝게 |
| **ElasticNet** | Ridge + Lasso 섞음 | `l1_ratio`로 비중 조절 (0.5 ≈ 반반) |

```python
from sklearn.linear_model import Ridge, Lasso, ElasticNet

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=1.0)
el = ElasticNet(alpha=0.1, l1_ratio=0.5)

eval_data(ridge, sc_x_train, sc_x_test, y_train, y_test)
eval_data(lasso, sc_x_train, sc_x_test, y_train, y_test)
eval_data(el, sc_x_train, sc_x_test, y_train, y_test)
```

> **쉽게 이해하기**  
> **규제**는 계수가 커질수록 벌점을 주는 장치입니다.  
> **Ridge**는 계수를 고르게 줄이고, **Lasso**는 덜 중요한 계수를 0에 가깝게 만듭니다. **ElasticNet**은 둘을 섞습니다.

---

## 5. 교차검증 (Cross-Validation)

- 표를 여러 겹으로 나눠 **번갈아 시험** → 점수 평균
- 한 번만 나눈 시험 점수보다 **덜 들쭉날쭉**
- 노트북에서는 `KFold` + `cross_val_score`(scoring=`r2`)로 평균 R²를 봅니다

```python
from sklearn.model_selection import cross_val_score, KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, features, label, cv=kf, scoring="r2")
print(scores.mean())
```

> **쉽게 이해하기**  
> **교차검증(Cross-Validation)** 은 데이터를 여러 겹으로 나눠 번갈아 시험하고 **평균** 점수를 냅니다.  
> 한 번만 나누면 운이 섞일 수 있습니다.

---

## 6. 가격 log1p 변환

- `price` 히스토그램이 **싼 쪽에 몰리면**(왜도) 큰 값이 학습을 흔들 수 있습니다
- `np.log1p(price)` = `log(1 + price)` 로 눌러 분포를 고르게
- `log(0)` 문제를 피하려고 `log1p`를 씁니다 (`log1p(0) = 0`)

```python
import numpy as np
y_log = np.log1p(label)  # 이후 모델은 y_log로 학습·평가 가능
```

> **쉽게 이해하기**  
> 가격이 싼 쪽에 몰리면 비싼 몇 개가 학습을 끌어갑니다.  
> **log1p**(`log(1+가격)`)는 큰 값을 눌러 분포를 고르게 만듭니다.  
> 되돌릴 때는 `expm1`을 씁니다.

---

## 한눈에 정리

```text
전처리: session18 (IQR → 인코딩 → split → StandardScaler)
모델: LinearRegression / Ridge / Lasso / ElasticNet
점수: MSE↓ 좋음, R²→1 좋음 (연습 vs 시험 비교)
교차검증: K겹으로 번갈아 → 평균 R²
log1p(price): 치우친 가격 분포를 눌러 학습 안정
노트북: Jupyter/09_diamonds_regression.ipynb
```

---

## 복습 체크 (스스로)

1. session18과 session19의 역할 차이는?
2. MSE와 R² 중 “클수록 좋은” 것은?
3. Ridge와 Lasso의 가장 큰 차이는?
4. 교차검증을 쓰는 이유는?
5. 가격에 `log1p`를 쓰는 이유는?

<details>
<summary>답 보기</summary>

1. 18은 Feature·이상치 등 **전처리**, 19는 그 위 **회귀 모델·평가·로그 변환**.
2. **R²** (1에 가까울수록). MSE는 작을수록 좋음.
3. Ridge는 계수를 고르게 줄이고, Lasso는 덜 중요한 계수를 **0에 가깝게** 만들 수 있음.
4. 한 번 나눈 시험 점수만 보면 운이 큼 → 여러 겹 평균이 더 안정적.
5. 가격이 한쪽으로 치우치면 큰 값이 학습을 흔듦 → log1p로 눌러 안정.

</details>

<!-- session-nav -->
**이동:** [← 세션 18](./session18.md) · [세션 20 →](./session20.md)
