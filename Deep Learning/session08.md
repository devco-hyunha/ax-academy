# 세션 08: 딥러닝 기초 6 — 커스텀 Module · 다출력 선형

<!-- session-nav -->

**이동:** [← 세션 07](./session07.md) · [세션 09 →](./session09.md) · [세션 10](./session10.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md) · [세션 05](./session05.md) · [세션 06](./session06.md)

날짜: 2026.11.10

session07의 **학습 루프 · state_dict · Optimizer**에 이어, 손으로 `forward`를 만들고, `nn.Linear`와 **커스텀 Module**(`LinearReg`)을 비교한 뒤, **출력이 여러 개**일 때 가중치 모양과 `Linear(4, 2)` 학습을 잡습니다.

> **이 세션이 하는 일 (쉬운 말)**  
> `y = wx + b`를 손으로 쓰는 법부터, 같은 식을 `nn.Linear`와 나만의 클래스에 넣는 법을 배웁니다.  
> `model(x)`가 왜 `forward`를 부르는지 잡고,  
> 입력이 여러 개·출력이 여러 개일 때 가중치 모양과 짧은 학습 루프를 실습합니다.

실습:

- [`PyTorch/08_custom_linear_module.ipynb`](./PyTorch/08_custom_linear_module.ipynb) — 수동 forward · LinearReg · `__call__`
- [`PyTorch/09_multi_output_linear.ipynb`](./PyTorch/09_multi_output_linear.ipynb) — `Linear(4, 2)` · MSE · SGD

(`torch-env` 커널 권장)

---

## 0. session07 복습 — 3연타 · state_dict 한 줄

학습 한 박자는 `zero_grad` → `backward` → `step` 입니다.  
`state_dict()`는 지금 weight · bias를 사전으로 보여 줍니다.  
자세한 본편은 [`session07.md`](./session07.md) · [`07_linear_train_loop.ipynb`](./PyTorch/07_linear_train_loop.ipynb)를 보세요.

---

## 파트 A — 수동 forward → nn.Linear → 커스텀 Module

### 1. 손으로 쓰는 forward

스칼라 가중치 `w`, 편향 `b`를 두고 `yhat = w * x + b`를 함수로 씁니다.

```python
w = torch.tensor(3.0)
b = torch.tensor(-1.0)

def forward(x):
    yhat = w * x + b
    return yhat
```

입력 하나가 아니라 여러 값이어도, 각 칸에 같은 식을 적용하면 출력 모양이 입력과 같습니다.

---

### 2. `nn.Linear` · `state_dict`

`nn.Linear(in_features, out_features)`는 같은 `y = wx + b`를 층으로 만듭니다.  
생성 직후 `state_dict()`는 **랜덤** 초기값입니다.

| 키              | 쉬운 뜻                                     |
| --------------- | ------------------------------------------- |
| `weight`        | 학습되는 기울기(가중치)                     |
| `bias`          | 학습되는 편향                               |
| `requires_grad` | 이 값의 연산을 추적해 기울기를 구할 수 있음 |

---

### 3. 커스텀 Module — `LinearReg`

`nn.Module`을 상속해 **나만의 모델 클래스**를 만듭니다.  
`__init__`에서 `nn.Linear`를 등록하고, `forward`에서 그 층을 호출합니다.

```python
from torch import nn

class LinearReg(nn.Module):
    def __init__(self, in_size, out_size):
        super().__init__()
        self.linear = nn.Linear(in_size, out_size)

    def forward(self, x):
        out = self.linear(x)
        return out
```

`super().__init__()`는 부모(`nn.Module`) 초기화를 불러 **가중치 등록·추적**을 켜는 단계입니다.

---

### 4. `model(x)` → `__call__` → `forward`

`model(x)`처럼 객체를 함수처럼 부르면, 파이썬 `__call__`이 먼저 돌고 그 안에서 `forward(x)`가 실행됩니다.  
직접 `forward`만 부르는 것보다 `model(x)`를 쓰는 편이 부가 처리·기울기 추적 설정과 맞습니다.

| 말           | 쉬운 뜻                         |
| ------------ | ------------------------------- |
| `model(x)`   | 객체를 함수처럼 호출            |
| `__call__`   | 그 호출을 받아 주는 파이썬 기능 |
| `forward(x)` | 실제 계산. `__call__`이 불러 줌 |

session05·07에서 본 `__call__`과 같은 감각입니다.

---

## 파트 B — 다출력 · `Linear(4, 2)` 학습

### 5. 출력이 여러 개일 때 가중치 모양

입력 특징이 4개, 출력이 3개라면 대략 이런 식입니다.

```text
y0 = x0*w00 + x1*w10 + x2*w20 + x3*w30 + b0
y1 = x0*w01 + x1*w11 + x2*w21 + x3*w31 + b1
y2 = x0*w02 + x1*w12 + x2*w22 + x3*w32 + b2
```

행렬로 보면 `w` 모양은 `(입력 수, 출력 수)`, `b` 모양은 `(출력 수,)` 입니다.  
`torch.matmul(x, w) + b`로 한 번에 계산할 수 있습니다.

---

### 6. `nn.Linear(4, 2)` · MSE · SGD

샘플 5개 · 특징 4개 → 출력 2개인 짧은 표를 텐서로 바꿉니다.  
모델은 `nn.Linear(4, 2)`, 손실은 `MSELoss`, Optimizer는 `SGD(lr=1e-4)`입니다.

학습 루프는 session07과 같습니다.

```text
예측 = model(입력)
손실 = MSE(예측, 정답)
zero_grad → backward → step
```

실습 본편: [`09_multi_output_linear.ipynb`](./PyTorch/09_multi_output_linear.ipynb)

---

## 7. 앞 세션과의 연결

| 곳               | 연결                                                                       |
| ---------------- | -------------------------------------------------------------------------- |
| session05~07     | `__call__` · `nn.Module` · state_dict · Optimizer 3연타                    |
| session08 (이번) | 수동 forward · LinearReg · 다출력 shape · `Linear(4, 2)` 학습              |
| 실습 08          | [`08_custom_linear_module.ipynb`](./PyTorch/08_custom_linear_module.ipynb) |
| 실습 09          | [`09_multi_output_linear.ipynb`](./PyTorch/09_multi_output_linear.ipynb)   |

---

## 복습 체크 (스스로)

1. 손으로 쓴 `forward`는 어떤 식을 계산하나요?
2. `LinearReg`에서 `super().__init__()`를 쓰는 이유는?
3. `model(x)`를 쓰면 실제로 실행되는 계산 메서드 이름은?
4. 입력 4 · 출력 2일 때 `nn.Linear`의 `in_features` · `out_features`는?
5. 다출력 학습에서도 Optimizer 3연타 순서는 같나요?

<details>
<summary>답 보기</summary>

1. **`yhat = w * x + b`**
2. **부모 `nn.Module` 초기화로 가중치 등록·추적을 켜려고**
3. **`forward`**
4. **`in_features=4`, `out_features=2`**
5. **같습니다.** `zero_grad` → `backward` → `step`

</details>

---

## 한눈에

```text
수동 forward : y = wx + b 를 함수로 직접 계산
nn.Linear    : 같은 식을 층으로 제공 · state_dict로 가중치 확인
LinearReg    : nn.Module 상속 · __init__에 Linear · forward에서 호출
model(x)     : __call__ → forward(x)
다출력       : w shape ≈ (입력 수, 출력 수), b ≈ (출력 수,)
실습 09      : Linear(4,2) + MSE + SGD(lr=1e-4) + epoch 루프

실습: 08_custom_linear_module.ipynb · 09_multi_output_linear.ipynb
복습: session07 3연타 · state_dict
```

<!-- session-nav -->

**이동:** [← 세션 07](./session07.md) · [세션 09 →](./session09.md) · [세션 10](./session10.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md) · [세션 05](./session05.md) · [세션 06](./session06.md)
