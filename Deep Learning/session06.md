# 세션 06: 딥러닝 기초 4 — ANN · 퍼셉트론 · 활성화 · TensorDataset

<!-- session-nav -->

**이동:** [← 세션 05](./session05.md) · [세션 07 →](./session07.md) · [세션 08 →](./session08.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md)

날짜: 2026.11.10  
Notion: [딥러닝 기초 4](https://app.notion.com/p/4-27d974c0f4ae80d0a170fe0e4d0a47c3)

session05의 **MNIST · DataLoader**에 이어, 인공 신경망(**ANN**)이 무엇인지부터 **퍼셉트론**, **활성화 함수**, `torch.nn`까지 잡고, 텐서를 바로 Dataset으로 묶는 **TensorDataset**으로 연결합니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 뇌 뉴런을 흉내 낸 **인공 신경망**과, 그 최소 단위인 **퍼셉트론**을 배웁니다.  
> 층을 쌓는 이유, **Sigmoid·tanh·ReLU·Softmax**가 하는 일,  
> `nn.Module`·순전파·역전파·Optimizer 흐름을 잡고, 실습에서 **TensorDataset**을 만듭니다.

실습: [`PyTorch/06_tensor_dataset.ipynb`](./PyTorch/06_tensor_dataset.ipynb)

(`torch-env` 커널 권장)

---

## 0. session05 복습 — Dataset · DataLoader 한 줄

`Dataset`은 **뽑기 통**, `DataLoader`는 **한 번에 몇 개씩** 꺼내는 도구입니다.  
MNIST처럼 그림 셋도, 아래 **TensorDataset**처럼 이미 만든 텐서도 같은 규칙으로 묶을 수 있습니다.  
자세한 본편은 [`session05.md`](./session05.md) · [`05_mnist_transforms_dataloader.ipynb`](./PyTorch/05_mnist_transforms_dataloader.ipynb)를 보세요.

---

## 파트 A — 인공 신경망 이론 (Notion)

### 1. ANN — 뇌를 흉내 낸 수학 모델

**ANN**(Artificial Neural Network, 인공 신경망)은 사람 뇌 **뉴런**(신경세포) 구조에서 영감을 받은 수학 모델입니다.

| 쪽          | 쉬운 말                                                                             |
| ----------- | ----------------------------------------------------------------------------------- |
| 사람 뇌     | 뉴런이 전기 신호를 받아 다른 뉴런에 전달 → 복잡한 사고·인식                         |
| 인공 신경망 | **노드**(뉴런 역할)가 입력을 받아 **가중치(weight)**·**편향(bias)**으로 계산 → 출력 |

한 뉴런은 여러 입력 신호를 모아, 세포막이 **임계값**에 닿으면 다음 뉴런으로 일정한 출력을 보냅니다.  
인공 쪽에서도 “입력에 가중치를 곱하고 더한다 → 활성화로 통과할지 정한다”가 같은 뼈대입니다.

> **쉽게 이해하기**  
> 뇌는 **전선이 아주 많은 전화기 교환기**에 가깝습니다.  
> ANN은 그 교환기를 **숫자(가중치·편향)**로 흉내 냅니다.

---

### 2. 층 — 입력 · 은닉 · 출력

| 층                       | 쉬운 뜻                             | 예                         |
| ------------------------ | ----------------------------------- | -------------------------- |
| **입력층**(Input layer)  | 데이터가 들어오는 곳                | 그림 픽셀, 표의 특징       |
| **은닉층**(Hidden layer) | 안쪽에서 여러 번 가공해 패턴을 뽑음 | ReLU·sigmoid로 비선형 처리 |
| **출력층**(Output layer) | 최종 예측을 내는 곳                 | 숫자 0~9 확률              |

입력층에서 신호를 받으면, 미리 둔 가중치와 계산한 뒤 **활성화 함수**를 거쳐 은닉층으로 보냅니다.  
같은 방식으로 다음 층으로 이어집니다.

---

### 3. 퍼셉트론 — 가장 작은 인공 뉴런

**퍼셉트론**(Perceptron)은 인공 신경망의 **가장 기본 형태**입니다.  
여러 입력을 받아 계산한 뒤 **하나의 출력**을 냅니다.

1. 입력 \( x_1, x_2, \dots, x_n \) 이 들어옴
2. 각 입력에 가중치 \( w_1, w_2, \dots, w_n \) 을 곱함
3. 모두 더하고 편향 \( b \) 를 더함

\[
z = \sum\_{i=1}^{n} w_i x_i + b
\]

가중치가 클수록 그 입력이 **더 중요**하다고 봅니다.  
그다음 **활성 함수**(임계값 등)를 통과해 예측값(예: -1 또는 1)을 냅니다.  
실제값과 다르면 가중치를 고칩니다.

> **쉽게 이해하기**  
> 퍼셉트론은 **저울**입니다. 입력마다 다른 추(가중치)를 달고,  
> 합이 기준을 넘으면 “예”, 아니면 “아니오”를 말합니다.

---

### 4. 단층 · 다층(MLP)

| 말                         | 쉬운 뜻                                                           |
| -------------------------- | ----------------------------------------------------------------- |
| **단층 퍼셉트론**          | 입력 → (바로) 출력. 직선으로 가를 수 있는 문제(예: AND)에 잘 맞음 |
| **다층 퍼셉트론**(**MLP**) | 가운데 **은닉층**을 둠. XOR처럼 직선 하나로 안 되는 문제에 필요   |

AND는 좌표 평면에 직선 하나로 나눌 수 있습니다.  
더 꼬인 문제는 은닉층을 두고, NAND·OR·AND처럼 **중간 결과**를 거쳐 최종 답을 만듭니다.

많은 실전 문제는 **비선형**입니다.  
그래서 **활성화 함수**를 넣고, 필요하면 **은닉층을 더** 둡니다.

---

### 5. 활성화 함수 — Sigmoid · tanh · ReLU · Softmax

활성화 함수는 “합쳐진 숫자 \( z \)를 **어떻게 비틀어** 다음으로 넘길지” 정합니다.

| 이름        | 쉬운 동작                                 | 자주 쓰는 곳               |
| ----------- | ----------------------------------------- | -------------------------- |
| **Sigmoid** | 출력을 **0~1**로                          | 이진 분류 출력층           |
| **tanh**    | 출력을 **-1~1**로                         | Sigmoid보다 학습이 빠른 편 |
| **ReLU**    | \( x<0 \) → 0, \( x>0 \) → \( x \) 그대로 | 깊은망 **은닉층**          |
| **Softmax** | 여러 출력을 **확률**로(합=1)              | 다중 분류 출력층           |

> **쉽게 이해하기**  
> 활성화는 **문지기**입니다. 아무 숫자나 통과시키지 않고,  
> 0~1·양수만·확률처럼 **다음 층이 쓰기 좋은 형태**로 바꿉니다.

---

### 6. torch.nn · nn.Module · Parameter

`torch.nn`은 신경망을 만드는 **기본 공구함**입니다.  
층(레이어), 손실(예: MSE), 활성화 함수가 들어 있습니다.

**`nn.Module`**은 모든 신경망의 **부모 클래스**입니다.  
모델을 만들 때는 이 클래스를 상속합니다.

| 메서드     | 역할                                        |
| ---------- | ------------------------------------------- |
| `__init__` | 층(레이어)을 **선언**                       |
| `forward`  | 데이터가 층을 **어떤 순서로** 지나갈지 정의 |

**`nn.Parameter`**는 학습 가능한 텐서입니다.  
일반 텐서처럼 연산하고, **Autograd**(연산을 기억해 나중에 기울기를 자동으로 구하는 기능)가 연산을 기록하며, 역전파 때 기울기를 구하고 Optimizer가 갱신합니다.  
`nn.Module` 속성으로 등록하면 `model.parameters()`에 들어가 Optimizer가 학습 대상으로 봅니다.

---

### 7. 순전파 · 역전파 · Optimizer

| 말                          | 쉬운 뜻                                                               |
| --------------------------- | --------------------------------------------------------------------- |
| **순전파**(Forward)         | 입력 → 은닉 → 출력까지 계산이 **앞으로** 흘러 예측값을 냄             |
| **역전파**(backpropagation) | 손실(loss)을 **뒤로** 거슬러 각 가중치·편향의 기울기(gradient)를 계산 |
| **Optimizer**               | 그 기울기로 가중치를 **조금씩 고침**                                  |

흐름 한 줄:

```text
순전파: 입력 → 예측 → 손실
역전파: 손실 → 가중치 기울기
Optimizer: 기울기 바탕으로 가중치 업데이트
```

이 세션에서는 **전체 epoch**(데이터를 한 바퀴 도는 학습 단위) **학습 루프**까지는 가지 않습니다.  
뼈대만 잡고, 데이터는 파트 B의 TensorDataset으로 준비합니다.

---

## 파트 B — TensorDataset 안내

이미 **NumPy 배열**이나 **텐서**가 있을 때, 클래스 Dataset을 새로 안 짜고도 묶을 수 있습니다.

| 단계 | 도구                                          | 쉬운 뜻                             |
| ---- | --------------------------------------------- | ----------------------------------- |
| 1    | `numpy` 난수 등                               | 가짜 특징·정답 만들기               |
| 2    | `torch.from_numpy`                            | NumPy → 텐서                        |
| 3    | `TensorDataset(x, y)`                         | **같은 인덱스**끼리 (특징, 정답) 짝 |
| 4    | `DataLoader(..., batch_size=2, shuffle=True)` | 2개씩 섞어 꺼내기                   |

```python
from torch.utils.data import TensorDataset, DataLoader
import torch
import numpy as np

torch.manual_seed(0)
np.random.seed(0)

X = np.random.randn(5, 3)
Y = np.random.randint(0, 2, (5,))
x_torch = torch.from_numpy(X)
y_torch = torch.from_numpy(Y)

train_xy = TensorDataset(x_torch, y_torch)
loader = DataLoader(train_xy, batch_size=2, shuffle=True)
features, labels = next(iter(loader))
print(features.shape, labels.shape)
```

샘플 5개·`batch_size=2`면 대략 **2 + 2 + 1** 묶음이 됩니다.  
장문 텐서 전체보다 **shape**을 먼저 확인합니다.

실습 본편: [`PyTorch/06_tensor_dataset.ipynb`](./PyTorch/06_tensor_dataset.ipynb)

---

## 8. 앞 세션과의 연결

| 곳               | 연결                                                            |
| ---------------- | --------------------------------------------------------------- |
| session04~05     | Dataset · transform · DataLoader · MNIST                        |
| session06 (이번) | ANN · 퍼셉트론 · 활성화 · nn.Module · 순/역전파 · TensorDataset |
| 실습 06          | [`06_tensor_dataset.ipynb`](./PyTorch/06_tensor_dataset.ipynb)  |

---

## 복습 체크 (스스로)

1. ANN이 뇌에서 본뜬 최소 계산 단위에 가까운 이름은?
2. 입력층·은닉층·출력층 중 “최종 예측”을 내는 곳은?
3. 은닉층에 자주 쓰는 활성화는?
4. `nn.Module`에서 데이터 흐름을 정의하는 메서드 이름은?
5. 이미 만든 텐서 두 개를 같은 인덱스로 짝 짓는 클래스는?

<details>
<summary>답 보기</summary>

1. **퍼셉트론**(Perceptron)
2. **출력층**
3. **ReLU** (자주)
4. **`forward`**
5. **`TensorDataset`**

</details>

---

## 한눈에

```text
ANN       : 뉴런을 흉내 낸 수학 모델 (가중치·편향)
퍼셉트론  : 입력×가중치 합 + 편향 → 활성 → 출력
단층/MLP  : 직선으로 안 되면 은닉층
활성화    : Sigmoid(0~1) · tanh(-1~1) · ReLU · Softmax(확률)
torch.nn  : 층·손실·활성 공구함 / nn.Module 상속
순전파→손실→역전파→Optimizer 가중치 갱신
TensorDataset : from_numpy → 짝 짓기 → DataLoader(batch_size=2)

실습: 06_tensor_dataset.ipynb
복습: session05 DataLoader · Notion 딥러닝 기초 4
```

<!-- session-nav -->

**이동:** [← 세션 05](./session05.md) · [세션 07 →](./session07.md) · [세션 08 →](./session08.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md)
