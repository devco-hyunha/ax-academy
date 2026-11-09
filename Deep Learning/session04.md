# 세션 04: 딥러닝 기초 3 — 행렬곱 · 연산 + 사용자 Dataset · DataLoader

<!-- session-nav -->

**이동:** [← 세션 03](./session03.md) · [세션 05 →](./session05.md) · [세션 01](./session01.md) · [세션 02](./session02.md)

날짜: 2026.11.06  
Notion: [딥러닝 기초 3](https://app.notion.com/p/3-27b974c0f4ae80e3ae6df4a5e68760b5)

session03의 텐서 **모양** 감각에 이어, 이번에는 **곱하기·합·최댓값 위치** 같은 연산과, **내 데이터**를 학습에 넣는 **Dataset · DataLoader**를 잡습니다.

> **이 세션이 하는 일 (쉬운 말)**  
> **파트 A** — 행렬과 벡터를 곱하고, 숫자 하나만 꺼내고, 표를 축 따라 더합니다.  
> **파트 B** — 파일·배열을 **한 장씩** 꺼내 주는 `Dataset`을 만들고, `DataLoader`로 **묶음(배치)** 을 준비합니다.

실습:

- 연산: [`PyTorch/03_tensor_matmul_ops.ipynb`](./PyTorch/03_tensor_matmul_ops.ipynb)
- Dataset: [`PyTorch/04_custom_dataset.ipynb`](./PyTorch/04_custom_dataset.ipynb)

(`torch-env` 커널 권장)

---

## 파트 A — 행렬곱 · item · linspace · sum · argmax

### 1. 행렬곱(matmul)이 왜 나오나요?

딥러닝 층은 대부분 **행렬 × 벡터**(또는 행렬 × 행렬) 형태입니다. session02의 **내적·행렬** 감각을 PyTorch에서 `matmul` / `@`로 실행합니다.

| 상황 | 쉬운 뜻 |
| ---- | ------- |
| 벡터 @ 행렬 | 한 줄 숫자가 표와 만나 **새 한 줄**이 됨 |
| 행렬 @ 벡터 | 표 한 장이 **한 사람 특징 벡터**를 받아 **여러 값**을 냄 |
| (배치, 행, 열) @ 벡터 | **여러 장**을 한 번에 같은 규칙으로 곱함 |

```python
import torch

A = torch.full((3, 2), 3)
x = torch.full((2,), 2)
print(torch.matmul(A, x))  # 길이 3
```

> **쉽게 이해하기**  
> 곱하기는 “**맞는 칸끼리 곱해서 더하기**”입니다.  
> **shape**만 맞으면 PyTorch가 알아서 맞춰 줍니다.

---

### 2. dtype · reshape · NumPy 왕복

- `torch.tensor(numpy_array)` → NumPy **dtype**을 그대로 가져올 수 있음  
- `reshape` → 칸 개수는 같고 **모양만** 바꿈  
- `from_numpy` / `.numpy()` → **같은 메모리**를 공유할 수 있으니, 한쪽을 바꾸면 다른 쪽도 바뀔 수 있음

---

### 3. item — 텐서에서 숫자 하나만

손실(loss)을 **출력**하거나 **if**에 넣을 때는 파이썬 **float**이 편합니다.  
원소가 **정확히 1개**일 때만 `.item()`을 씁니다.

```python
x = torch.randn(1)
loss_value = x.item()  # float 하나
```

---

### 4. linspace

-2부터 2까지 **5칸**으로 **균등** 나눈 배열을 만듭니다. NumPy·PyTorch 모두 같은 이름입니다.

---

### 5. sum(dim=...) · argmax / argmin

| 함수 | 하는 일 |
| ---- | ------- |
| `sum(dim=0)` | **세로**로 더함(열 방향) |
| `sum(dim=1)` | **가로**로 더함(행 방향) |
| `argmax` | **가장 큰 값의 위치**(인덱스) |
| `argmin` | **가장 작은 값의 위치** |

---

## 파트 B — 사용자 Dataset · DataLoader

### 6. 왜 Dataset이 필요한가요?

이미지·텍스트·표 파일은 **형식이 제각각**입니다.  
한꺼번에 RAM에 다 올리기 어렵기도 합니다.  
그래서 PyTorch는 **“i번째 샘플 하나만 주세요”** 규칙인 `Dataset`을 씁니다.

필수 메서드:

| 메서드 | 역할 |
| ------ | ---- |
| `__init__` | 경로·배열·전처리 옵션 **준비** |
| `__len__` | **몇 개**인지 |
| `__getitem__(idx)` | **idx번째** `(입력, 정답)` 한 쌍 |

> **쉽게 이해하기**  
> Dataset은 **뽑기 통**입니다.  
> `__getitem__`은 “**n번째 카드 한 장**”을 내놓는 손입니다.

---

### 7. transform — 꺼낼 때 전처리

크기 맞추기·스케일 맞추기는 **학습 전**에 해야 합니다.  
`__getitem__` 안에서 `transform`이 있으면 **꺼낼 때마다** 적용합니다.

노트북 `04`에서는 원본에 없던 `scaling`을 **x를 10으로 나누는** 최소 함수로 채웠습니다.

---

### 8. DataLoader — 배치로 묶기

GPU는 **한 장씩**보다 **묶음**이 효율적입니다.  
`DataLoader`는 Dataset에서 **batch_size**만큼 꺼내 **텐서 shape을 한 단계 더** 쌓습니다.

```python
from torch.utils.data import DataLoader

loader = DataLoader(dataset, batch_size=4, shuffle=True)
for batch_x, batch_y in loader:
    print(batch_x.shape)  # (4, 특징...)
    break
```

---

## 9. 앞 세션과의 연결

| 곳 | 연결 |
| -- | ---- |
| session02 | NumPy · 행렬 · 내적 |
| session03 | 텐서 ndim · shape · view |
| session04 (이번) | matmul · item · sum · argmax + Dataset · DataLoader |
| 실습 03 | [`03_tensor_matmul_ops.ipynb`](./PyTorch/03_tensor_matmul_ops.ipynb) |
| 실습 04 | [`04_custom_dataset.ipynb`](./PyTorch/04_custom_dataset.ipynb) |

---

## 복습 체크 (스스로)

1. `(3, 2)` 행렬과 길이 2 벡터를 `matmul`하면 결과 길이는?
2. `.item()`을 쓸 수 있는 텐서 원소 개수는?
3. `sum(dim=1)`은 **어느 방향**으로 더하나요?
4. Dataset에서 **샘플 개수**를 돌려주는 메서드는?
5. `DataLoader`의 `batch_size=4`면 `batch_x.shape[0]`은 보통?

<details>
<summary>답 보기</summary>

1. **3**
2. **1개**
3. **행 방향(가로)** — 각 행을 한 줄로 합침
4. **`__len__`**
5. **4**

</details>

---

## 한눈에

```text
파트 A — 연산
  matmul / @ : 행렬·벡터 곱 (shape 맞추기)
  item       : 원소 1개 → 파이썬 float
  linspace   : 구간 균등 나누기
  sum(dim)   : 0=세로, 1=가로
  argmax/min : 최댓·최솟값 위치

파트 B — 데이터
  Dataset: __init__ / __len__ / __getitem__
  transform: 꺼낼 때 전처리
  DataLoader: batch_size · shuffle → 배치 shape

실습: 03_tensor_matmul_ops.ipynb · 04_custom_dataset.ipynb
Notion: 딥러닝 기초 3
```

<!-- session-nav -->

**이동:** [← 세션 03](./session03.md) · [세션 05 →](./session05.md) · [세션 01](./session01.md) · [세션 02](./session02.md)
