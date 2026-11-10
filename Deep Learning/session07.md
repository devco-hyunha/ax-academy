# 세션 07: 딥러닝 기초 5 — 학습 루프 · state_dict · Optimizer

<!-- session-nav -->

**이동:** [← 세션 06](./session06.md) · [세션 08 →](./session08.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md) · [세션 05](./session05.md)

날짜: 2026.11.10  
Notion: [딥러닝 기초 5](https://app.notion.com/p/5-27e974c0f4ae80ca818af122152ae090)

session06의 **ANN · nn.Module · 순/역전파**에 이어, 머신러닝과 딥러닝의 **선형회귀** 차이를 잡고, `state_dict` · `Module.__call__` · **GD/SGD** · Optimizer **3연타** · **autograd**까지 연결합니다.  
session01의 \( y=wx+b \) 감각은 같고, 이번엔 **모듈 + Optimizer 학습 루프**에 초점을 둡니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 직선 하나를 `nn.Linear`로 두고, 손실을 줄이는 **학습 루프**를 배웁니다.  
> `zero_grad` → `backward` → `step` 세 줄이 한 박자임을 잡고,  
> 학습 전후 `state_dict`로 가중치가 바뀌는지 확인합니다.

실습: [`PyTorch/07_linear_train_loop.ipynb`](./PyTorch/07_linear_train_loop.ipynb)

(`torch-env` 커널 권장)

---

## 0. session06 복습 — 순전파 · 역전파 · Optimizer 한 줄

순전파로 예측을 내고, 손실에서 역전파로 기울기를 구한 뒤, Optimizer가 가중치를 고칩니다.  
이번 세션은 그 흐름을 **짧은 epoch 루프**로 실제로 돌립니다.  
자세한 본편은 [`session06.md`](./session06.md) · [`06_tensor_dataset.ipynb`](./PyTorch/06_tensor_dataset.ipynb)를 보세요.

---

## 파트 A — 선형회귀 · 학습 루프 (Notion)

### 1. 머신러닝 vs 딥러닝 선형회귀

| 쪽                    | 쉬운 뜻                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **머신러닝** 선형회귀 | 전통 기법. 파라미터 \( (w, b) \) 를 **닫힌 해**(공식, 예: 최소제곱법 OLS)나 경사하강으로 구함. 보통 `LinearRegression()` 한 줄 |
| **딥러닝** 선형회귀   | 신경망의 **가장 기본 형태**. 프레임워크 안에서 **자동미분 + 옵티마이저**로 학습. 닫힌 해는 거의 안 씀                          |

딥러닝에서도 선형회귀는 **한 층짜리 모델**입니다.  
**단층 퍼셉트론**(은닉층 없음 · 활성화 없음) = 선형회귀와 같습니다.

> **어떻게 쓰지**  
> 단순 직선 문제면 사이킷런 같은 머신러닝 라이브러리로도 충분합니다.  
> 딥러닝에서는 이 직선 층이 **큰 망을 쌓는 기본 벽돌**이라서 배웁니다.

---

### 2. `model.state_dict()` — 지금 가중치 사전

`nn.Module`은 학습 가능한 **가중치(weight)** · **편향(bias)** 를 안에 둡니다.  
`state_dict()`를 호출하면 그 값들을 **딕셔너리**(키-값 묶음)로 돌려줍니다.

| 시점           | `state_dict()` 값                |
| -------------- | -------------------------------- |
| 모델 생성 직후 | 초기 weight · bias (**랜덤**)    |
| 학습 후        | 손실을 줄이며 맞춘 weight · bias |

최적값을 보려면 **학습(손실 최소화)** 을 거친 뒤에 다시 보면 됩니다.

---

### 3. 딥러닝에서 경사하강법을 쓰는 이유

딥러닝 프레임워크는 **경사하강법**(gradient descent, 기울기를 따라 내려가 손실을 줄이는 방법) 기반 최적화가 기본입니다.

- 데이터가 많거나 특징 차원이 커도 계산 가능
- 다층 망처럼 **닫힌 해가 없는** 모델에도 그대로 씀
- GPU · 자동 미분과 잘 맞음

---

### 4. `nn.Module.__call__()` — 객체를 함수처럼

`nn.Linear` 같은 `nn.Module`에는 내부적으로 `__call__`이 있습니다.  
`model(x)` 또는 `self.linear(x)` 라고 쓰면:

1. 부가 처리(훅) 실행
2. 기울기 추적 설정
3. **`forward(x)` 호출**

| 개념             | 쉬운 뜻                                     |
| ---------------- | ------------------------------------------- |
| `nn.Module` 객체 | weight · bias 를 가진 층                    |
| `__call__`       | 객체를 **함수처럼** 부르게 하는 파이썬 기능 |
| `forward(x)`     | 실제 계산. `__call__`이 호출할 때 실행      |

session05의 `__call__`과 같은 감각입니다. 층도 “함수처럼” 부릅니다.

---

### 5. GD vs SGD

| 말                                                       | 쉬운 뜻                                                    |
| -------------------------------------------------------- | ---------------------------------------------------------- |
| **GD**(Gradient Descent)                                 | 한 번 갱신할 때 **데이터 전부**로 기울기 계산              |
| **SGD**(Stochastic Gradient Descent, 확률적 경사 하강법) | **작은 묶음(batch)** 만 뽑아 갱신. 빠르고 큰 데이터에 유리 |

둘 다 “기울기를 따라 내려가며” 손실이 작은 지점을 찾습니다.  
파라미터가 **가짜 골짜기(local minima)** 에 갇히기 쉬운데, SGD는 갱신이 흔들려 **진짜 최저**에 가까워질 여지가 큽니다.

---

### 6. Optimizer 3연타 — `zero_grad` · `backward` · `step`

Optimizer는 파라미터 갱신을 **대신** 해 줍니다.  
학습 루프에서 거의 항상 이 **세 줄**이 한 세트입니다.

| 순서 | 코드                    | 쉬운 뜻                                                                              |
| ---- | ----------------------- | ------------------------------------------------------------------------------------ |
| 1    | `optimizer.zero_grad()` | 이전에 쌓인 기울기를 **0으로 지움**. 안 지우면 기울기가 누적되어 틀어짐              |
| 2    | `loss.backward()`       | 손실 기준으로 각 파라미터 기울기를 구해 `.grad`에 저장. **여기선 값이 아직 안 바뀜** |
| 3    | `optimizer.step()`      | 기울기 · 학습률(lr)로 weight · bias 를 **실제로 고침**                               |

선형 모델 흐름 한 줄:

```text
입력 → 모델 → 예측
예측 · 정답 → 손실
zero_grad → backward → step
```

예전에 손으로 `W = W - lr * W.grad` 하던 일을 `step()`이 대신합니다.

---

### 7. `torch.autograd` — 자동 미분

**autograd**는 텐서 연산에 대해 **자동으로 미분**해 주는 엔진입니다.  
역전파에서 가중치는 “손실에 대한 기울기”만큼 조정됩니다.

| 말                   | 쉬운 뜻                                 |
| -------------------- | --------------------------------------- |
| `requires_grad=True` | 이 텐서 연산을 **추적** 시작            |
| `.backward()`        | 추적한 연산으로 **모든 기울기**를 계산  |
| `.grad`              | 계산된 기울기가 **누적**되는 자리       |
| `.detach()`          | 연산 기록에서 **떼어** 이후 추적을 막음 |

---

### 8. 면접 비유 — \( y = wx + b \) 한 장

합격을 예측하는 면접으로 비유하면 이해가 쉽습니다.

| 신경망 말 | 면접 비유                                      |
| --------- | ---------------------------------------------- |
| 입력층    | 스펙(학점 · 토익 · 프로젝트 · 경력 …)          |
| 가중치    | 무엇을 **중요**하게 볼지 (큰 신호 / 작은 신호) |
| 편향      | 면접관 성격(깐깐 · 널널)                       |
| 은닉층    | 입력을 조합해 **숨은 특징** 찾기               |
| 활성화    | 점수가 **임계값**을 넘었는지                   |
| 출력층    | 합격 확률 예: 95%                              |

학습 순서(코드와 맞추기):

```text
1. 순전파 — forward로 예측
2. 손실 — 실제값과 예측값 차이
3. zero_grad() — 이전 기울기 지우기
4. loss.backward() — 기울기만 계산 (아직 갱신 없음)
5. optimizer.step() — w, b 업데이트
```

역전파는 대략 `loss → MSE → 덧셈 · 행렬곱`처럼 **역순**으로 미분 대상을 추적합니다.

---

## 파트 B — 실습 안내 (`nn.Linear` 학습 루프)

짧은 데이터로 `nn.Linear(1, 1)` · `MSELoss` · `SGD` 를 돌립니다.  
학습 **전후** `state_dict()`를 비교해 가중치가 바뀌었는지 확인합니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(0)

x = torch.linspace(-1.0, 1.0, 20).unsqueeze(1)
y = 2.0 * x + 1.0

model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

print("학습 전:", model.state_dict())

for epoch in range(50):
    y_pred = model(x)
    loss = criterion(y_pred, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("학습 후:", model.state_dict())
```

실습 본편: [`PyTorch/07_linear_train_loop.ipynb`](./PyTorch/07_linear_train_loop.ipynb)

---

## 9. 앞 세션과의 연결

| 곳               | 연결                                                                  |
| ---------------- | --------------------------------------------------------------------- |
| session01        | \( y=wx+b \) · 손수 경사하강 · (선택) `nn.Linear`                     |
| session05~06     | `__call__` · `nn.Module` · 순/역전파 · Optimizer 뼈대                 |
| session07 (이번) | ML/DL 선형회귀 · state_dict · SGD · 3연타 · autograd · 짧은 학습 루프 |
| 실습 07          | [`07_linear_train_loop.ipynb`](./PyTorch/07_linear_train_loop.ipynb)  |

---

## 복습 체크 (스스로)

1. 딥러닝 선형회귀는 보통 닫힌 해 대신 무엇을 쓰나요?
2. 학습 직후가 아니라 생성 직후 `state_dict`를 보면 무엇이 보이나요?
3. `model(x)`를 쓰면 실제로 실행되는 메서드 이름은?
4. Optimizer 3연타 순서는?
5. `loss.backward()`만 호출하면 가중치가 바로 바뀌나요?

<details>
<summary>답 보기</summary>

1. **옵티마이저**(SGD · Adam 등) + 자동미분
2. **랜덤** 초기 weight · bias
3. **`forward`**
4. **`zero_grad` → `backward` → `step`**
5. **아니요.** 기울기만 계산하고, `step()`이 값을 고칩니다.

</details>

---

## 한눈에

```text
ML 선형회귀 : 공식(OLS) 또는 라이브러리 한 줄
DL 선형회귀 : nn.Linear 한 층 + Optimizer 학습
state_dict  : 지금 weight·bias 사전 (학습 전=랜덤, 후=맞춤값)
__call__    : model(x) → forward(x)
GD / SGD    : 전체 vs 작은 batch로 기울기
3연타       : zero_grad → backward → step
autograd    : requires_grad · backward · .grad · detach

실습: 07_linear_train_loop.ipynb
복습: session06 순/역전파 · Notion 딥러닝 기초 5
```

<!-- session-nav -->

**이동:** [← 세션 06](./session06.md) · [세션 08 →](./session08.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md) · [세션 05](./session05.md)
