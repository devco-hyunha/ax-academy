# 세션 03: 딥러닝 기초 3 — 텐서 차원 · 모양 · view

<!-- session-nav -->

**이동:** [← 세션 02](./session02.md) · [세션 04 →](./session04.md) · [세션 05 →](./session05.md) · [세션 01](./session01.md)

날짜: 2026.11.06

session02의 NumPy · 벡터 · 행렬 감각을 **PyTorch 텐서**로 옮깁니다.  
실습은 [`PyTorch/02_tensor_ndim_view.ipynb`](./PyTorch/02_tensor_ndim_view.ipynb)에서 따라 합니다 (`torch-env` 커널 권장).

> **이 세션이 하는 일 (쉬운 말)**  
> **텐서**는 숫자를 담는 상자입니다.  
> 상자가 **몇 겹인지(차원)** 와 **몇 칸인지(모양)** 를 보고,  
> 칸 개수는 그대로 두고 **모양만 바꾸는** 방법을 배웁니다.

---

## 1. 텐서 · ndim · shape

**텐서(Tensor)** = PyTorch가 쓰는 **숫자 상자**입니다.  
NumPy의 `ndarray`와 친척이고, GPU에서도 같은 생각으로 씁니다.

| 말 | 쉬운 뜻 | 예 |
| -- | ------- | -- |
| **ndim** | 차원이 몇 **겹**인지 (축 개수) | 표는 보통 2 |
| **shape** | 각 축에 칸이 **몇 개**인지 | `(3, 4)` = 3행 4열 |
| **스칼라** | 숫자 **하나** (0차원) | `20` |
| **벡터** | 숫자 **한 줄** (1차원) | `[1, 2, 3]` |
| **행렬** | 숫자 **표** (2차원) | 2행 3열 |

> **쉽게 이해하기**  
> 상자를 열기 전에 **겹 수**와 **칸 수**부터 봅니다.  
> `ndim`이 “몇 겹?”, `shape`이 “각 겹에 몇 칸?”입니다.

---

## 2. 0차원 ~ 3차원

```text
0D  숫자 하나          →  ()
1D  한 줄              →  (n,)
2D  표(행·열)          →  (행, 열)
3D  표를 여러 장 겹침  →  (장, 행, 열)
```

- 컬러 이미지는 흔히 `(채널, 높이, 너비)`처럼 3차원으로 둡니다.
- 딥러닝 연산은 미세한 변화를 다루므로 실수(`float32`)가 기본입니다.

```python
import torch

d1 = torch.FloatTensor([1, 2, 3])
print(d1.ndim, d1.shape)   # 1, torch.Size([3])

mat = torch.FloatTensor([[1, 2], [3, 4], [5, 6]])
print(mat.ndim, mat.shape) # 2, torch.Size([3, 2])
```

> **쉽게 이해하기**  
> 바깥 대괄호부터 **한 겹씩** 세면 차원이 보입니다.  
> `[[[1]]]` 은 3겹입니다.

---

## 3. 채우기 — zeros · ones · full · rand

같은 모양을 **같은 값** 또는 **난수**로 빠르게 만듭니다.

| 함수 | 하는 일 |
| ---- | ------- |
| `zeros` | 0으로 채움 |
| `ones` | 1로 채움 |
| `full` | 지정한 값으로 채움 |
| `rand` | 0~1 사이 난수 |

```python
t0 = torch.zeros(4, 3)
filled = torch.full((2, 3), 200, dtype=torch.float32)
rnd = torch.rand(2, 2, 3)
```

> **쉽게 이해하기**  
> 빈 표를 손으로 채우지 않습니다.  
> “이 크기로, 이 값으로”라고 시키면 상자가 바로 생깁니다.

---

## 4. 모양 바꾸기 — view · reshape

**view / reshape** = 원소 **개수는 그대로** 두고 **모양만** 바꿉니다.

- 전체 칸 수는 반드시 같아야 합니다. 예: 6칸 → `(2, 3)` 또는 `(3, 2)`
- `-1` = “나머지 칸은 **알아서** 맞춰 주세요”라는 자리입니다.

```python
x = torch.tensor([1, 2, 3, 4, 5, 6])
y = x.view(2, 3)      # 2행 3열
z = x.view(2, -1)     # 행 2, 열은 자동(3)
```

> **쉽게 이해하기**  
> 레고 블록 **개수는 같고**, 쌓는 **모양만** 바꿉니다.  
> 그게 `view` · `reshape`입니다. (이 개념의 비유는 여기 하나만 둡니다.)

---

## 5. 자료형 — dtype

**dtype** = 칸에 **어떤 종류의 숫자**를 담을지입니다.

- `float32` (`FloatTensor`)가 기본으로 많이 쓰입니다.
- `float64` (`DoubleTensor`)는 더 정밀하지만 메모리·속도 부담이 큽니다.
- `type(...)`으로 자료형만 바꿀 수 있습니다.

```python
d = torch.zeros(3, dtype=torch.float)
d = d.type(torch.int)
print(d.dtype)
```

---

## 6. 전치 · arange

**전치(T)** = 행과 열을 **뒤집습니다**. `(2, 4)` → `(4, 2)`  
**arange** = 시작~끝 **직전**까지 일정한 간격의 수열을 만듭니다.

```python
d2 = torch.ones(2, 4)
print(d2.T.shape)           # torch.Size([4, 2])

print(torch.arange(5))      # 0~4
print(torch.arange(1, 15, 2))  # 1, 3, 5, ...
```

---

## 7. 원소 연산

같은 모양끼리 `+` `-` `*` `/` 하면 **칸마다** 계산합니다.  
(행렬 곱과는 다릅니다. 행렬 곱은 나중에 따로 배웁니다.)

```python
a = torch.full((3, 3), 3)
b = torch.full((3, 3), 4)
print(a + b)  # 칸마다 7
print(a * b)  # 칸마다 12
```

---

## 8. NumPy 왕복

데이터 준비는 NumPy로, 학습은 텐서로, 그래프는 다시 NumPy로 — **서로 바꿀 수 있습니다.**

```python
import numpy as np

arr = np.array([[1, 2], [3, 4]])
ten = torch.from_numpy(arr)  # NumPy → 텐서
back = ten.numpy()           # 텐서 → NumPy
```

> **쉽게 이해하기**  
> session02에서 익힌 NumPy 상자와 PyTorch 상자는 **문을 열고 오갈 수 있습니다.**

---

## 9. 인덱싱

표에서 원하는 칸만 고릅니다. 조건식(`>`)으로 고르는 것도 가능합니다.

```python
m = torch.IntTensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m[:, 1])           # 모든 행의 1열 → [2, 5, 8]
print(m[m > 5])          # 5보다 큰 값만
```

---

## 10. 앞 내용과의 연결

| 곳 | 연결 |
| -- | ---- |
| Deep Learning session01 | PyTorch 환경 · 텐서 입문 |
| Deep Learning session02 | NumPy · 벡터 · 행렬 · 내적 |
| Deep Learning session03 (이번) | 텐서 차원 · 모양 · view |
| 실습 노트북 | [`02_tensor_ndim_view.ipynb`](./PyTorch/02_tensor_ndim_view.ipynb) |

---

## 복습 체크 (스스로)

1. `ndim`과 `shape`의 차이를 한 문장으로?
2. 원소 6개인 1차원 텐서를 2행 3열로 바꾸는 방법은?
3. `view`에서 `-1`은 무슨 뜻인가요?
4. `zeros`와 `full`의 차이는?
5. NumPy 배열을 텐서로 바꾸는 함수는?

<details>
<summary>답 보기</summary>

1. `ndim`은 **몇 겹**, `shape`은 **각 겹의 칸 수**
2. `.view(2, 3)` 또는 `.reshape(2, 3)` (전체 개수 6이 같아야 함)
3. 나머지 축 크기를 **자동으로** 맞추라는 뜻
4. `zeros`는 0으로, `full`은 **지정한 값**으로 채움
5. `torch.from_numpy(...)`

</details>

---

## 한눈에

```text
텐서 = 숫자 상자
  ndim = 몇 겹?    shape = 각 겹에 몇 칸?

0D 스칼라 → 1D 벡터 → 2D 행렬 → 3D(장·행·열)

채우기: zeros / ones / full / rand
모양만 바꾸기: view · reshape  (−1 = 자동)
  칸 개수는 반드시 같아야 함

dtype · 전치(T) · arange
원소 연산(+ − * /) · NumPy 왕복 · 인덱싱

실습: PyTorch/02_tensor_ndim_view.ipynb
```

<!-- session-nav -->

**이동:** [← 세션 02](./session02.md) · [세션 04 →](./session04.md) · [세션 05 →](./session05.md) · [세션 01](./session01.md)
