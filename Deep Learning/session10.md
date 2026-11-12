# 세션 10 — epoch·하이퍼파라미터 · 로지스틱 · Sequential · BCELoss

<!-- session-nav -->

**이동:** [← 세션 09](./session09.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md) · [세션 05](./session05.md) · [세션 06](./session06.md) · [세션 07](./session07.md) · [세션 08](./session08.md)

날짜: 2026.11.11

Notion(딥러닝 기초 6): https://app.notion.com/p/6-27f974c0f4ae80519613d5ebf2c94370

session09의 **보스턴 집값 · MLP · DataLoader**에 이어, 학습을 나누는 단위(**epoch · batch · iteration**)와 **하이퍼파라미터**, 이진 분류의 **로지스틱 · Sequential · BCELoss · Adam**을 쉬운 말로 정리합니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 문제를 몇 번 다 보는지(epoch), 한 번에 몇 개씩 보는지(batch), 한 epoch에 몇 번 갱신하는지(iteration)를 잡습니다.  
> 학습이 고치는 숫자(파라미터)와 사람이 미리 정하는 숫자(하이퍼파라미터)를 구분합니다.  
> **고객 이탈(churn)** 처럼 예/아니오를 맞출 때 쓰는 StandardScaler · 시그모이드 · BCELoss · Adam을 실습과 함께 봅니다.

실습: [`PyTorch/11_churn_logistic.ipynb`](./PyTorch/11_churn_logistic.ipynb)  
데이터: [`PyTorch/data/ChurnData.csv`](./PyTorch/data/ChurnData.csv)

(`torch-env` 커널 권장. `pandas` · `scikit-learn`이 필요합니다.)

---

## 0. session09 복습 — MLP · 배치 한 줄

집값 회귀는 `13→64→32→1` MLP와 `DataLoader(batch=32)`로 학습하고, MSE·R²·산점도로 점수를 봤습니다.  
자세한 본편은 [`session09.md`](./session09.md) · [`10_boston_mlp.ipynb`](./PyTorch/10_boston_mlp.ipynb)를 보세요.

---

## 1. epoch · batch size · iteration

쉬운 비유: 문제지가 **1000문제**이고, 한 번에 **10문제**씩 본다고 합시다.

| 말 | 쉬운 뜻 | 이 비유 |
| --- | --- | --- |
| epoch | 학습 데이터를 **처음부터 끝까지 한 바퀴** 본 횟수 | 1000문제를 다 보면 1 epoch |
| batch size | 한 번에 묶어서 넣는 샘플 수 | 10개씩 |
| iteration | 한 epoch 안에서 **배치를 넣는 횟수**(갱신 횟수) | 1000 ÷ 10 = **100번** |

```text
iteration ≈ 샘플 수 / batch size
예: 1000문제 · batch 10 → iteration 100 / epoch
```

한 epoch = “전 문제지를 한 번 다 봄”.  
한 iteration = “한 묶음(batch)을 보고 weight·bias를 한 번 고침”.

---

## 2. 파라미터 vs 하이퍼파라미터

| 구분 | 무엇이냐 | 예 |
| --- | --- | --- |
| 파라미터 | 학습이 **스스로 고치는** 숫자 | weight `w`, bias `b` |
| 하이퍼파라미터 | 사람이 **미리 정하는** 설정 | `lr`, 은닉층 수, dropout, epochs, batch size |

파라미터는 학습 루프가 바꿉니다.  
하이퍼파라미터는 실험 전에 고르고, 결과에 맞춰 다시 골라 봅니다.

---

## 3. 로지스틱 — 머신러닝 vs 딥러닝

**로지스틱**은 출력을 0~1 사이 확률처럼 보이게 만들어, **예/아니오(이진)** 를 맞출 때 씁니다.

| 곳 | 쉬운 역할 |
| --- | --- |
| 머신러닝 로지스틱 | 모델 **자체**가 로지스틱 회귀인 경우가 많음 |
| 딥러닝 | **마지막 출력층**에 시그모이드를 두고, 앞 층은 특징을 뽑음 |
| 다중 분류 | 출력이 여러 클래스면 **소프트맥스**를 씀(이번 세션 초점 밖) |

이진: 시그모이드 → 확률 하나(예: 이탈 확률).  
다중: 소프트맥스 → 클래스마다 확률 합이 1.

---

## 4. 이탈(churn) 예측 실습

**churn(이탈)** 은 고객이 서비스를 **그만두는 것**입니다. 정답은 예(1)·아니오(0)입니다.

실습 노트북: [`11_churn_logistic.ipynb`](./PyTorch/11_churn_logistic.ipynb)  
데이터: [`data/ChurnData.csv`](./PyTorch/data/ChurnData.csv) (노트북에서는 `data/ChurnData.csv` 상대경로)

| 단계 | 쉬운 뜻 |
| --- | --- |
| feature / `churn` | 입력 열들과 이탈 여부(정답) |
| `StandardScaler` | 각 열을 **평균 0 · 표준편차 1**로 맞춤. `fit`은 train만 |
| MinMax와 비교 | MinMax는 0~1 압축. 표 숫자엔 Standard를 자주 씀 |
| 모델 | `in_dim→32→1` + ReLU + **Sigmoid**(확률 0~1). 은닉 32는 2의 거듭제곱 효율 |
| 손실 · Optimizer | `BCELoss` · `Adam(lr=0.001)` |
| 배치 | `TensorDataset` · `DataLoader(batch=16)` |
| 평가 | 확률 ≥ 0.5면 이탈(1)로 보고 정확도 |

```text
입력 → Linear(in, 32) + ReLU → Linear(32, 1) + Sigmoid → 확률(0~1)
학습: zero_grad → backward → step
테스트: 임계값 0.5 → 정확도
```

이론 흐름(흡연 예시의 층 줄이기)도 같은 아이디어입니다. 숫자를 줄이며 핵심만 남깁니다.

```text
입력 → 200 → 100 → 20 → 5 → output(시그모이드)
```

흡연 실습: [`PyTorch/12_insurance_smoke.ipynb`](./PyTorch/12_insurance_smoke.ipynb)  
데이터: [`PyTorch/data/insurance.csv`](./PyTorch/data/insurance.csv)

---

## 5. `nn.Sequential` — 층을 한 줄로 나열

`Sequential`은 층을 **위에서 아래 순서대로** 쌓아 둡니다.  
`forward`를 따로 안 써도, 넣은 순서대로 자동으로 통과합니다.

```python
import torch.nn as nn

model = nn.Sequential(
    nn.Linear(5, 1),
    nn.Sigmoid(),
)

# model[0] → 첫 번째 층(Linear)
# model(x) → Linear 통과 후 Sigmoid
```

| 말 | 쉬운 뜻 |
| --- | --- |
| `nn.Sequential(...)` | 층을 순서대로 나열한 모델 |
| `model[0]` | 0번 층에 바로 접근 |
| `forward` 생략 | Sequential이 순서를 대신 처리 |

실습 노트북은 `nn.Module`을 상속한 `LinearReg`(이탈)와 `SmokeModel`+`Sequential`(흡연)로 같은 시그모이드 출력을 만듭니다. Sequential과 Module 둘 다 쓸 수 있습니다.  
흡연 Sequential 실습: [`12_insurance_smoke.ipynb`](./PyTorch/12_insurance_smoke.ipynb)

---

## 6. `BCELoss` — 이진 분류 손실

**BCELoss**(Binary Cross Entropy Loss)는 정답이 0 또는 1일 때, 예측 확률이 얼마나 빗나갔는지 재는 손실입니다.  
정답이 1인데 예측이 1에 가까우면 손실이 작고, 멀리 떨어지면 손실이 큽니다.

| 정답 | 예측 | 손실(대략) | 쉬운 느낌 |
| --- | --- | --- | --- |
| 1 | 0.9 | 0.105 | 거의 맞춤 → 손실 작음 |
| 1 | 0.1 | 2.303 | 크게 틀림 → 손실 큼 |
| 0 | 0.1 | 0.105 | 거의 맞춤 → 손실 작음 |
| 0 | 0.9 | 2.303 | 크게 틀림 → 손실 큼 |

학습은 이 손실을 **작게** 만들도록 weight·bias를 고칩니다.  
실습 [`11_churn_logistic.ipynb`](./PyTorch/11_churn_logistic.ipynb)의 `criterion = nn.BCELoss()`가 이 역할입니다.

---

## 7. 학습 흐름 한 바퀴

```text
forward → BCELoss → backward → step → (다음 배치 / 다음 epoch)
```

| 단계 | 쉬운 뜻 |
| --- | --- |
| forward | 입력으로 예측(확률)을 냄 |
| BCELoss | 예측과 정답(0/1)의 차이를 숫자로 |
| backward | 어디를 얼마나 고칠지 기울기 계산 |
| step | Optimizer가 weight·bias를 실제로 고침 |
| epoch | 위 과정을 데이터 한 바퀴만큼 반복 |

회귀(session09)는 MSE, 이진 분류는 BCELoss를 쓰는 점이 다릅니다.  
3연타(`zero_grad` → `backward` → `step`) 순서는 같습니다.

---

## 8. `nn.Linear` 내부 모양

`nn.Linear(in_features, out_features)`의 내부 텐서 모양입니다.

| 이름 | 모양 | 쉬운 뜻 |
| --- | --- | --- |
| weight | `(out, in)` | 출력 칸 × 입력 칸 |
| bias | `(out,)` | 출력 칸마다 더하는 숫자 |

예: `nn.Linear(5, 1)` → weight `(1, 5)`, bias `(1,)`.

---

## 9. 손실 · 역전파 · Adam · RMSprop

| 말 | 쉬운 한 줄 |
| --- | --- |
| 손실 | 예측이 정답과 **얼마나 다른지**를 숫자로 만든 것 |
| 역전파(`backward`) | 그 차이를 줄이려면 **어느 방향을 얼마나** 고칠지 계산 |
| RMSprop | 최근 기울기 크기를 **지수 가중 이동 평균**으로 기억해, 칸마다 보폭을 조절 |
| Adam | **모멘텀**(방향 기억) + **RMSprop**(보폭 조절)을 합친 Optimizer |

**지수 가중 이동 평균:** 옛날 값보다 **최근 값**에 더 무게를 두는 평균입니다.  
Adam은 “어느 쪽으로 갈지”와 “얼마나 성큼 갈지”를 같이 봅니다.  
실습은 `optim.Adam(..., lr=0.001)`을 씁니다.

---

## 복습 체크 (스스로)

1. 문제 1000개 · batch 10이면 한 epoch의 iteration은?
2. `w`, `b`는 파라미터일까요, 하이퍼파라미터일까요?
3. 딥러닝에서 이진 분류의 시그모이드는 보통 어디에 두나요?
4. `nn.Sequential`에서 `forward`를 안 써도 되는 이유는?
5. 정답 1 · 예측 0.9일 때 BCELoss는 대략 큰가요, 작은가요?
6. Adam은 무엇을 합친 Optimizer인가요?
7. `churn`이 1이면 무엇을 뜻하나요?
8. `StandardScaler`의 `fit`은 어디에만 하나요?

<details>
<summary>답 보기</summary>

1. **100번** (1000 ÷ 10)
2. **파라미터** — 학습이 고침. `lr`·epochs·batch는 하이퍼파라미터
3. **마지막 출력층**
4. **층을 넣은 순서대로 자동 통과**하기 때문
5. **작음**(대략 0.105)
6. **모멘텀(방향) + RMSprop(보폭)**
7. **이탈(서비스를 그만둠)**
8. **학습 데이터에만**

</details>

---

## 한눈에

```text
단위       : epoch(한 바퀴) · batch(한 묶음) · iteration(샘플/batch)
파라미터   : w, b (학습이 고침)
하이퍼     : lr, 은닉층 수, dropout, epochs, batch size
로지스틱   : ML=모델 자체 / DL=출력층 시그모이드 · 다중은 소프트맥스
이탈 실습  : ChurnData.csv · StandardScaler · in→32→1 · Sigmoid
           : BCELoss · Adam(lr=0.001) · DataLoader(batch=16) · 임계값 0.5
Sequential : Linear + Sigmoid · forward 생략 · model[0] 접근
BCELoss    : 정답1·예측0.9→~0.105 / 정답1·예측0.1→~2.303
학습       : forward → BCELoss → backward → step → epoch
Linear     : weight (out, in) · bias (out,)
Optimizer  : Adam = 모멘텀 + RMSprop

실습: 11_churn_logistic.ipynb · 12_insurance_smoke.ipynb
이전: session09.md · 10_boston_mlp.ipynb
```

<!-- session-nav -->

**이동:** [← 세션 09](./session09.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md) · [세션 05](./session05.md) · [세션 06](./session06.md) · [세션 07](./session07.md) · [세션 08](./session08.md)
