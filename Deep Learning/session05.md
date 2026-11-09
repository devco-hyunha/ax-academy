# 세션 05: 딥러닝 기초 3 — `__call__` · Compose · MNIST · DataLoader

<!-- session-nav -->

**이동:** [← 세션 04](./session04.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md)

날짜: 2026.11.09

session04의 **Dataset · transform · DataLoader**에 이어, 객체를 함수처럼 쓰는 `__call__`, 전처리를 줄 세우는 `Compose`, 손글씨 숫자 **MNIST**까지 잡습니다.

> **이 세션이 하는 일 (쉬운 말)**  
> **transform**을 함수·객체로 연결하고, **Compose**로 순서를 맞춥니다.  
> **MNIST**를 받아 가운데 자르기·텐서로 바꾼 뒤, **한 장 shape**과 **배치 shape**을 보고 `matplotlib`으로 그립니다.

실습: [`PyTorch/05_mnist_transforms_dataloader.ipynb`](./PyTorch/05_mnist_transforms_dataloader.ipynb)

(`torch-env` 커널 권장 · 첫 실행 시 MNIST 다운로드에 네트워크가 필요합니다)

---

## 0. session04 복습 — Dataset 한 줄

`Dataset`은 **뽑기 통**입니다. `__len__`은 개수, `__getitem__`은 **한 샘플**입니다.  
`transform`이 있으면 `__getitem__` 안에서 **꺼낼 때마다** 전처리합니다.  
자세한 본편은 [`session04.md`](./session04.md) · [`04_custom_dataset.ipynb`](./PyTorch/04_custom_dataset.ipynb)를 보세요.

---

## 1. `__call__` — 객체를 함수처럼

일반 함수도 transform에 넣을 수 있습니다.  
**상태를 들고** 싶을 때는 클래스에 `__call__`을 둡니다.  
그러면 `객체(샘플)`처럼 쓰면 **자동으로** `__call__`이 실행됩니다.

```python
class adder:
    def __init__(self, add1=1):
        self.add1 = add1

    def __call__(self, sample):
        x, y = sample
        return x + self.add1, y + self.add1
```

> **쉽게 이해하기**  
> `a1 = adder()`로 도구를 만들고, `a1(샘플)`이면 “**이 도구로 한 번 손보기**”입니다.  
> Dataset 안 `self.transform(sample)`도 같은 규칙입니다.

---

## 2. Compose — 전처리를 줄 세우기

여러 transform을 **순서대로** 적용하려면 `transforms.Compose([...])`를 씁니다.  
리스트 앞이 먼저, 뒤가 나중입니다.

```python
from torchvision import transforms

pipe = transforms.Compose([scaling, adder()])
```

> **쉽게 이해하기**  
> Compose는 **조립 라인**입니다. 데이터가 들어오면 칸마다 한 번씩 지나갑니다.

---

## 3. MNIST + CenterCrop + ToTensor

**MNIST**는 0~9 손글씨 숫자 그림입니다. 원본은 보통 **28×28** 흑백입니다.

| 도구 | 쉬운 뜻 |
| ---- | ------- |
| `CenterCrop(20)` | 가운데 **20×20**만 남김 |
| `ToTensor()` | 그림 → 텐서, 값을 **0~1**로 맞춤 |
| `datasets.MNIST(...)` | 학습/테스트 셋 받기 (`download=True`면 첫 실행에 받음) |

```python
from torchvision import datasets, transforms

crop_trans = transforms.Compose([
    transforms.CenterCrop(20),
    transforms.ToTensor(),
])
train_data = datasets.MNIST(
    root="data", train=True, download=True, transform=crop_trans
)
```

한 샘플은 `(이미지 텐서, 정답 숫자)` 쌍입니다.

---

## 4. shape — 한 장 `(C,H,W)` · 배치 `(B,C,H,W)`

| 말 | 쉬운 뜻 | 이번 예 |
| -- | ------- | ------- |
| **C** | 색 채널(흑백이면 1) | 1 |
| **H, W** | 세로·가로 칸 | 20, 20 |
| **B** | 배치(한 번에 묶은 장수) | 64 |

- 한 장: `(1, 20, 20)` → **(C, H, W)**  
- `DataLoader(batch_size=64)` 한 묶음: `(64, 1, 20, 20)` → **(B, C, H, W)**

장문 텐서 전체를 출력하지 말고 **shape만** 확인합니다.

---

## 5. DataLoader · 한 장 그리기

```python
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

loader = DataLoader(train_data, batch_size=64, shuffle=True)
features, labels = next(iter(loader))
print(features.shape)  # (64, 1, 20, 20)

img = features[0].squeeze()  # (20, 20) — 채널 1칸 제거
plt.imshow(img, cmap="gray")
plt.title(int(labels[0]))
plt.show()
```

> **쉽게 이해하기**  
> `squeeze`는 **크기 1인 축**을 접어, `imshow`가 좋아하는 **2차원 표**로 만듭니다.

---

## 6. 앞 세션과의 연결

| 곳 | 연결 |
| -- | ---- |
| session03 | 텐서 ndim · shape |
| session04 | Dataset · transform · DataLoader |
| session05 (이번) | `__call__` · Compose · MNIST · 배치 shape · 시각화 |
| 실습 05 | [`05_mnist_transforms_dataloader.ipynb`](./PyTorch/05_mnist_transforms_dataloader.ipynb) |

---

## 복습 체크 (스스로)

1. `객체(샘플)`을 쓰면 자동으로 실행되는 메서드 이름은?
2. `Compose([A, B])`에서 **먼저** 도는 것은?
3. `CenterCrop(20)` 후 한 장 shape은 보통?
4. `batch_size=64`일 때 배치 shape의 **맨 앞** 숫자는?
5. `(1, 20, 20)`을 `imshow`용 2차원으로 만들 때 자주 쓰는 메서드는?

<details>
<summary>답 보기</summary>

1. **`__call__`**
2. **A** (리스트 앞)
3. **`(1, 20, 20)`** (채널 1)
4. **64**
5. **`squeeze()`** (또는 `view` / `reshape`)

</details>

---

## 한눈에

```text
__call__  : 객체를 함수처럼 호출
Compose   : transform을 순서대로
MNIST     : 손글씨 0~9 (첫 실행 download)
CenterCrop(20) + ToTensor → 한 장 (C,H,W)=(1,20,20)
DataLoader batch_size=64 → (B,C,H,W)=(64,1,20,20)
시각화    : squeeze → imshow (한 장만)

실습: 05_mnist_transforms_dataloader.ipynb
복습: session04 Dataset
```

<!-- session-nav -->

**이동:** [← 세션 04](./session04.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md)
