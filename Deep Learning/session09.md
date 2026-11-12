# 세션 09: 딥러닝 기초 7 — 보스턴 집값 · MLP · DataLoader

<!-- session-nav -->

**이동:** [← 세션 08](./session08.md) · [세션 10 →](./session10.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md) · [세션 05](./session05.md) · [세션 06](./session06.md) · [세션 07](./session07.md)

날짜: 2026.11.11

session08의 **커스텀 Module · 다출력 선형**에 이어, 실제 CSV로 **집값(회귀)** 를 맞춥니다.  
`MinMaxScaler`로 입력을 0~1로 맞추고, **MLP**(여러 층 신경망) `13→64→32→1`과 `DataLoader` 배치 학습까지 연결합니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 표(CSV)에서 특징과 집값을 나누고, 학습·테스트로 나눕니다.  
> 숫자 범위를 맞춘 뒤, 층을 세 개 쌓은 모델로 집값을 예측합니다.  
> `TensorDataset`·`DataLoader`로 32개씩 학습하고, 테스트 MSE·R²·산점도로 점수를 봅니다.

실습: [`PyTorch/10_boston_mlp.ipynb`](./PyTorch/10_boston_mlp.ipynb)

(`torch-env` 커널 권장. `pandas` · `scikit-learn`이 필요합니다.)

---

## 0. session08 복습 — Module · 학습 루프 한 줄

`nn.Module`을 상속해 `forward`를 쓰고, `zero_grad` → `backward` → `step`으로 학습합니다.  
이번엔 층이 하나(`Linear`)가 아니라 **여러 층 + ReLU**입니다.  
자세한 본편은 [`session08.md`](./session08.md) · [`09_multi_output_linear.ipynb`](./PyTorch/09_multi_output_linear.ipynb)를 보세요.

---

## 1. 데이터 — CSV · feature · target

경로: [`PyTorch/data/boston_house.csv`](./PyTorch/data/boston_house.csv) (노트북에서는 `data/boston_house.csv` 상대경로).

| 말 | 쉬운 뜻 |
| --- | --- |
| feature | 집값을 맞추는 데 쓰는 입력 열들(범죄율, 방 개수 등 13개) |
| target / `MEDV` | 맞추려는 집값 열 |
| `Unnamed: 0` | 인덱스 잔여 열. 학습에 쓰지 않고 제거 |

```python
df = pd.read_csv("data/boston_house.csv")
feature = df.drop(["MEDV", "Unnamed: 0"], axis=1)
target = df.pop("MEDV")
X = feature.to_numpy()
y = target.values
```

---

## 2. train / test 나누기

`train_test_split(..., test_size=0.2, random_state=1)`로 학습 80% · 테스트 20%로 나눕니다.  
테스트는 **학습에 안 쓴 점수표**입니다.

---

## 3. MinMaxScaler · 데이터 누수 주의

`MinMaxScaler`는 각 열을 **0과 1 사이**로 압축합니다.

```text
(값 - 최솟값) / (최댓값 - 최솟값)
```

**숫자 예시:** `[10, 20, 30, 40, 100]` → 최솟값 10, 최댓값 100

```text
10  → (10-10)/(100-10) = 0.00
20  → (20-10)/(100-10) = 0.11
30  → (30-10)/(100-10) = 0.22
40  → (40-10)/(100-10) = 0.33
100 → (100-10)/(100-10) = 1.00
```

큰 숫자·작은 숫자가 섞여 있어도, 이렇게 맞추면 모델이 한 열만 크게 보지 않습니다.

| 단계 | 쉬운 뜻 |
| --- | --- |
| `fit` | 학습 데이터에서만 열마다 최솟값·최댓값을 기억 |
| `transform` | 그 기억으로 숫자를 0~1로 바꿈 |

**데이터 누수:** 테스트 숫자로 최솟값·최댓값을 미리 알면, 학습에 테스트 정보가 살짝 섞입니다.  
그래서 `fit`은 **학습만**, 테스트는 `transform`만 합니다.

```python
mc = MinMaxScaler()
X_train = mc.fit_transform(X_train)
X_test = mc.transform(X_test)  # fit 금지
```

---

## 4. 텐서 · `view(-1, 1)`

모델 입력·정답은 `float32` 텐서입니다.  
정답은 열이 1개여야 마지막 층 출력 `(N, 1)`과 맞습니다.

```python
X_train_tensor = torch.FloatTensor(X_train)
y_train_tensor = torch.FloatTensor(y_train).view(-1, 1)
```

`view(-1, 1)`은 “행은 알아서, 열은 1개”로 모양을 바꿉니다.

---

## 5. MLP — `LinearReg` · `13→64→32→1` · ReLU

**MLP**(Multi-Layer Perceptron)는 선형 층을 여러 개 쌓고, 층 사이에 **활성화**를 넣는 신경망입니다.  
**ReLU**는 음수는 0, 양수는 그대로 두는 스위치입니다.

**쉬운 비유:** 집 특징 13개를 먼저 **64개 조합**으로 섞고, 겹치는 느낌을 줄여 **32개**로 줄인 뒤, 마지막에 **집값 1개**를 냅니다.

```text
입력 13 → fc1(64) + ReLU → fc2(32) + ReLU → fc3(1) 집값
```

| 층 | 쉬운 역할 |
| --- | --- |
| fc1 13→64 | 특징을 여러 조합으로 펼침 |
| fc2 64→32 | 핵심만 남기며 압축 |
| fc3 32→1 | 집값 하나 출력(여기서는 ReLU 없음) |

```python
class LinearReg(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        output = self.fc3(x)
        return output
```

손실은 `MSELoss`, Optimizer는 `SGD(lr=0.001, momentum=0.5)`입니다.

| 말 | 쉬운 뜻 |
| --- | --- |
| 학습률 `lr` | 한 번에 weight·bias를 **얼마나 크게** 고칠지. 크면 성큼, 작으면 조심조심 |
| **momentum** | 이전 갱신 방향을 조금 기억해 더 부드럽게 가는 설정 |

---

## 6. TensorDataset · DataLoader

`TensorDataset`은 **같은 집의 특징과 집값**을 한 묶음으로 맞춥니다.  
인덱스 0이면 “0번 집의 특징 + 0번 집값”이 같이 나옵니다.

`DataLoader(..., batch_size=32, shuffle=True)`는 한 번에 32개씩, epoch마다 순서를 섞어 줍니다.

```text
학습 샘플 약 404개 ÷ 32 ≈ 13 배치 / epoch
```

---

## 7. 학습 루프 · 테스트 MSE · R² · 산점도

배치마다 3연타(`zero_grad` → `backward` → `step`)를 돌립니다.  
끝난 뒤 `model.eval()`과 `torch.no_grad()`로 테스트 전체에 대해 점수를 봅니다.

| 지표 | 쉬운 뜻 |
| --- | --- |
| MSE | 예측과 정답 차이의 제곱 평균. **작을수록** 좋음 |
| R² (`r2_score`) | “평균만 찍는 것보다 얼마나 잘 맞췄는지”. **1에 가까울수록** 좋음(1=완벽, 0=평균 수준) |

**산점도:** 가로는 실제 집값, 세로는 예측 집값입니다.  
파란 직선 `y=x`는 “완벽히 맞춘 선”입니다. 점들이 이 선에 가까울수록 잘 맞춘 것입니다.

```text
for epoch:
    for x_batch, y_batch in train_loader:
        예측 → MSE → zero_grad → backward → step

테스트: pred = model(X_test) → MSE · r2_score
산점도: scatter(실제, 예측) + plot(실제, 실제)  # 파란 y=x
```

실습 본편: [`10_boston_mlp.ipynb`](./PyTorch/10_boston_mlp.ipynb)

---

## 8. 앞 세션과의 연결

| 곳 | 연결 |
| --- | --- |
| session05~06 | Dataset · DataLoader · TensorDataset |
| session07~08 | Optimizer 3연타 · 커스텀 Module · LinearReg |
| session09 (이번) | CSV · 스케일 · MLP · 배치 학습 · MSE · R² · 산점도 |
| session10 | epoch · 하이퍼파라미터 · 로지스틱 · Sequential · BCELoss |
| 실습 10 | [`10_boston_mlp.ipynb`](./PyTorch/10_boston_mlp.ipynb) |

---

## 복습 체크 (스스로)

1. `MinMaxScaler`의 `fit`은 학습·테스트 중 어디에만 하나요?
2. 테스트에 `fit`을 하면 생기는 문제는?
3. MLP 층 구성 `13→64→32→1`에서 마지막 숫자 1은 무엇을 뜻하나요?
4. `view(-1, 1)`을 정답에 쓰는 이유는?
5. `DataLoader`의 `batch_size=32`는 무엇을 하나요?
6. R²가 1에 가깝다는 것은 무엇을 뜻하나요?

<details>
<summary>답 보기</summary>

1. **학습 데이터에만**
2. **데이터 누수** — 테스트 정보가 학습 전처리에 섞임
3. **집값 출력 하나**
4. **모델 출력 모양 `(N, 1)`과 맞추려고**
5. **한 번에 32개씩 묶어 학습에 넣음**
6. **평균만 찍는 것보다 훨씬 잘 맞춤(완벽에 가까움)**

</details>

---

## 한눈에

```text
CSV        : data/boston_house.csv · feature 13 · MEDV
나누기     : train 80% / test 20%
스케일     : MinMaxScaler fit=train만 · transform=train·test
           : 예 [10,20,30,40,100] → 0~1
텐서       : FloatTensor · y는 view(-1, 1)
MLP        : LinearReg 13→64→32→1 · ReLU · MSE · SGD(lr=0.001, momentum=0.5)
           : lr = 한 번에 w·b를 얼마나 크게 고칠지
배치       : TensorDataset(같은 집 묶음) + DataLoader(batch=32, shuffle=True)
평가       : 테스트 MSE · R² · 산점도(가로=실제, 세로=예측, 파란 y=x)

실습: 10_boston_mlp.ipynb
복습: session08 LinearReg · session05~06 DataLoader
다음: session10.md
```

<!-- session-nav -->

**이동:** [← 세션 08](./session08.md) · [세션 10 →](./session10.md) · [세션 01](./session01.md) · [세션 02](./session02.md) · [세션 03](./session03.md) · [세션 04](./session04.md) · [세션 05](./session05.md) · [세션 06](./session06.md) · [세션 07](./session07.md)
