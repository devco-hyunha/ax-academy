# 세션 01: 딥러닝 기초 1 — 함수 · 미분 · 신경망 입문 · PyTorch 환경

**이동:** [세션 02 →](./session02.md) · [세션 03 →](./session03.md) · [세션 04 →](./session04.md) · [세션 05 →](./session05.md) · [세션 06 →](./session06.md) · [세션 07 →](./session07.md) · [세션 08 →](./session08.md)

날짜: 2026.11.05  
카페: [딥러닝 기초 1](https://cafe.naver.com/f-e/cafes/31780422/articles/635)  
Notion: [딥러닝 기초 1](https://app.notion.com/p/1-279974c0f4ae8083bdf6fed2b41468be)

수업 Notion에 이어서 추가된 내용(미분 예제 · 딥러닝 개요 · 선형회귀·경사하강 · PyTorch/TensorFlow · conda 환경)까지 반영합니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 먼저 **직선·곡선**이 무엇인지 보고, **미분**(한 점의 기울기)을 익힙니다.  
> 그다음 **딥러닝**이 “여러 층으로 패턴을 찾는 방법”임을 잡고,  
> 직선 \( y=wx+b \) 를 조금씩 고쳐 가는 **학습** 감각과 **PyTorch 환경**까지 갑니다.

---

## 1. 1차 함수: \( y = ax + b \)

\[
y = ax + b
\]

| 기호    | 이름                        | 쉬운 뜻                        |
| ------- | --------------------------- | ------------------------------ |
| \( x \) | 독립변수                    | **입력**                       |
| \( y \) | 종속변수                    | **출력**                       |
| \( a \) | 기울기 / **가중치(weight)** | 직선의 **기울기**              |
| \( b \) | y절편 / **편향(bias)**      | 직선을 **위·아래**로 옮기는 값 |

- **가중치 \( a \)가 변하면** 그래프 **기울기**가 변합니다.
- **편향 \( b \)가 변하면** 그래프 **높낮이**가 변합니다.

예시 \( y = 3x + 5 \):

| \( x \)  | \( y = 3x + 5 \) |
| -------- | ---------------- |
| \( -2 \) | \( -1 \)         |
| \( 0 \)  | \( 5 \)          |
| \( 2 \)  | \( 11 \)         |

```text
y
|
|           /
|         /   ← 기울기 a=3
|       /
|     /
|   /
| /_________ x
      ↑ b=5 (y절편)
```

Notion 예시 코드:

```python
import numpy as np
import matplotlib.pyplot as plt

def plot_linear(a, b):
    x = np.linspace(-10, 10, 100)
    y = a * x + b

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = {a}x + {b}", color="blue", lw=2)
    plt.axhline(0, color="black", lw=1) # axhline 함수 - x 축을 그리는 함수
    plt.axvline(0, color="black", lw=1) # axvline 함수 - y 축을 그리는 함수
    plt.grid(True, linestyle="--")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.title(f"Graph of y = {a}x + {b}")
    plt.legend()
    plt.show()

plot_linear(a=1, b=0)
# 예: plot_linear(a=3, b=5)
```

> **쉽게 이해하기**  
> 직선을 그릴 때 **기울기**와 **높이**만 정하면 됩니다.  
> 학습에서 말하는 **가중치 \( a \)**, **편향 \( b \)** 가 바로 그 두 손잡이입니다.  
> 손잡이를 돌리면 예측 직선이 기울어지거나 위아래로 움직입니다.

---

## 2. 2차 함수

대표 예: \( y = x^2 \) (아래로 볼록한 포물선).

| \( x \)  | \( y = x^2 \) |
| -------- | ------------- |
| \( -2 \) | \( 4 \)       |
| \( -1 \) | \( 1 \)       |
| \( 0 \)  | \( 0 \)       |
| \( 1 \)  | \( 1 \)       |
| \( 2 \)  | \( 4 \)       |

```text
y
|
|  \         /
|   \       /
|    \     /
|     \   /
|      \ /
|_______●_______ x
        O
     y = x^2
```

| 비교                 | 모양 | 한 줄                         |
| -------------------- | ---- | ----------------------------- |
| 1차 \( y = ax + b \) | 직선 | 기울기가 **한 값**으로 일정   |
| 2차 \( y = x^2 \)    | 곡선 | 위치에 따라 **기울기가 바뀜** |

> **쉽게 이해하기**  
> 직선은 어디서 봐도 **같은 가파름**입니다.  
> \( y = x^2 \) 같은 곡선은 **위치에 따라** 가파름이 달라집니다.  
> 그래서 “지금 이 점에서 얼마나 가파른가?”를 묻는 도구가 다음의 **미분**입니다.

---

## 3. 미분

### 3-1. 뜻

**미분** = 함수의 **순간 변화율**을 구하는 방법.  
⇒ 그래프에서 **한 점의 접선 기울기**를 구하는 것.

예를 들어 함수 \( y = f(x) \)가 있을 때:

### 3-2. 평균 변화율 → 미분계수

\[
\frac{\Delta y}{\Delta x}
= \frac{f(x + \Delta x) - f(x)}{\Delta x}
\]

\[
f'(x)
= \lim*{\Delta x \to 0}
\frac{f(x + \Delta x) - f(x)}{\Delta x}
= \lim*{h \to 0}
\frac{f(x + h) - f(x)}{h}
\]

| 표기                              | 뜻                                      |
| --------------------------------- | --------------------------------------- |
| \( f'(x) \), \( \dfrac{dy}{dx} \) | \( x \)에서의 **순간 기울기**(미분계수) |
| \( \Delta x \), \( h \)           | \( x \)의 아주 작은 변화                |

> **쉽게 이해하기**  
> 평균 변화율 = 두 점을 이은 직선 기울기.  
> 미분 = 두 점을 **아주 가깝게** 붙였을 때의 기울기.

### 3-3. 예: \( f(x) = x^2 \)

\[
\begin{aligned}
f'(x)
&= \lim*{h \to 0}\frac{(x+h)^2 - x^2}{h}
= \lim*{h \to 0}\frac{2xh + h^2}{h}
= \lim\_{h \to 0}(2x + h)
= 2x
\end{aligned}
\]

\[
f(x) = x^2 \quad \Rightarrow \quad f'(x) = 2x
\]

### 3-4. Notion 예제

- **1차 함수** \( y = 3x + 2 \)
  - 기울기 3 → **미분값 = 3**
- **2차 함수** \( y = x^2 \)
  - \( x = 2 \)에서 순간 변화율 \( = 2 \cdot 2 = 4 \)
  - 즉, \( x = 2 \)일 때 그래프가 **4만큼** 가파르게 올라가는 감각

### 3-5. 기본 미분표

| 함수                | 미분            |
| ------------------- | --------------- |
| \( f(x) = c \)      | \( 0 \)         |
| \( f(x) = ax + b \) | \( a \)         |
| \( f(x) = x^n \)    | \( n x^{n-1} \) |
| \( f(x) = x^2 \)    | \( 2x \)        |

> **쉽게 이해하기**  
> \( x^2 \) 를 \( x=2 \)에서 보면 순간 기울기가 \( 4 \)입니다.  
> “지금은 이만큼 가파르다”는 **숫자 하나**로 요약하는 것이 미분계수입니다.  
> 학습에서는 이 숫자로 “오차를 줄이려면 어느 쪽으로 조금 움직일지”를 정합니다.

---

## 4. 딥러닝(deep learning)

- 현실 세계 데이터를 **텐서(행렬)** 로 표현합니다.
- 핵심은 **신경망(Neural Network)** 입니다.
- **딥(Deep)** = **층(Layer)** 이 여러 개인 신경망을 뜻합니다.
- 사람처럼 “감각”을 흉내내어 복잡한 문제를 풀 수 있습니다.

| 분야        | 예                         |
| ----------- | -------------------------- |
| 이미지 인식 | 사진 속 고양이·강아지 구별 |
| 음성 인식   | 스마트폰 음성 명령         |
| 자연어 처리 | 번역, 챗봇                 |
| 추천 시스템 | 넷플릭스, 유튜브 추천      |

> **쉽게 이해하기**  
> 표·사진·소리를 **숫자 덩어리(텐서)** 로 바꾼 뒤,  
> **여러 층 신경망**이 그 안에서 패턴을 스스로 찾습니다.

---

## 5. 딥러닝 vs 머신러닝

| 구분      | 머신러닝                              | 딥러닝                            |
| --------- | ------------------------------------- | --------------------------------- |
| 특징      | 사람이 **특징(feature)** 을 직접 설계 | 컴퓨터가 특징을 **자동으로 학습** |
| 데이터 양 | 적은 데이터도 가능                    | **데이터가 많을수록** 유리        |
| 구조      | 단순 모델 (결정트리, SVM 등)          | **신경망**, 층이 많음 → “Deep”    |

> **쉽게 이해하기**  
> 예전 방식은 사람이 “어떤 칸이 중요할지”를 많이 정해 줬습니다.  
> 딥러닝은 층이 쌓이면서 **그 칸(특징)을 스스로 찾아** 가는 쪽에 가깝습니다.  
> 대신 보통 **데이터가 많을수록** 빛이 납니다.

---

## 6. 신경망의 구조

인간의 두뇌 신경망을 **모방한 이름**이지만, **실제 작동 방식은 인간 두뇌와 전혀 다릅니다.**

```text
입력층(Input) → 은닉층(Hidden Layer) → 출력층(Output)
```

| 층     | 역할                               |
| ------ | ---------------------------------- |
| 입력층 | 데이터를 넣는 곳                   |
| 은닉층 | 데이터의 **패턴을 학습**           |
| 출력층 | 최종 결과 (예: 고양이/강아지 분류) |

> **쉽게 이해하기**  
> 공장 라인처럼 생각하면 쉽습니다.  
> **입력층**에 재료를 넣고, **은닉층**에서 여러 번 다듬고, **출력층**에서 최종 답을 꺼냅니다.  
> 이름이 “신경망”이어도, 실제로는 **숫자 계산의 층 쌓기**입니다.

---

## 7. 선형 회귀와 학습 감각

### 7-1. 식

\[
y = wx + b
\]

목표: **예측값과 실제값의 차이**를 작게 만드는 적절한 **가중치 \( w \)**, **편향 \( b \)** 를 구하기.

### 7-2. 손실 → 경사 → 학습률 → 갱신

흐름:

1. **실제값 / 예측값** 확인 (**손실 함수**)
2. 어느 방향으로 움직여야 오차가 줄어드는지 계산 (**경사 = 기울기**, 편미분)
3. **학습률(learning rate)** 만큼 조금씩 직선을 움직임 (**업데이트**)
4. 오차가 최소가 될 때까지 2~3을 **반복**

갱신 식 (수업 Notion):

\[
\text{New } W = \text{old } W - (\text{Learning Rate}) \times (\text{Gradient})
\]

| 말                 | 쉬운 뜻                                                |
| ------------------ | ------------------------------------------------------ |
| **Gradient(경사)** | 지금 손실이 **어느 쪽으로** 기울었는지                 |
| **Learning Rate**  | 한 번에 **얼마나** 움직일지 (보폭)                     |
| **마이너스**       | 기울기가 가리키는 방향의 **반대**로 가야 오차가 줄어듦 |

추가로 정리한 말:

- 직선 방정식으로 예측
- 예측값과 실제값 차이의 **제곱을 평균** → 손실
- 손실을 최소화하도록 \( \theta_0 \), \( \theta_1 \) 조정
- **기울기**: 얼마나 가파르게 데이터를 설명하냐
- **절편**: 직선의 위치를 위아래로 이동
- ⇒ **기울기·절편 둘 다** 업데이트

### 7-3. 편미분 · 연쇄법칙 (수업 문장)

**편미분** 관련 수업 설명:  
수학(미분)에서 ‘덩어리 안에 또 다른 식’이 들어 있을 때 쓰는 **합성함수 미분법(Chain Rule)**.  
전체 변화에 주는 영향력(기울기)을 한 번 더 곱해 줘야 정확한 값이 나오므로, **겉미분과 편미분을 곱한다**고 정리합니다.

> **쉽게 이해하기**  
> 오차 골짜기에서 “지금 기울기”를 보고, **반대쪽**으로 한 걸음씩 내려갑니다.  
> Machine Learning session10의 **경사하강법**과 같은 생각입니다.

---

## 8. 파이토치 · 텐서플로우

### 8-1. PyTorch

페이스북 AI 연구팀이 만든 **파이썬 기반 딥러닝 라이브러리**.  
딥러닝 모델을 만들고 학습시키는 도구입니다.

- **동적 계산 그래프(Dynamic Computation Graph)** — 계산 과정이 실시간으로 만들어짐
- **GPU 지원** — 행렬 연산을 GPU에서 빠르게, 이미지·영상·자연어에 유리
- **Python 친화적** — 일반 파이썬처럼 작성, NumPy와 호환

### 8-2. TensorFlow

구글이 만든 딥러닝/머신러닝 프레임워크.  
PyTorch와 비슷하지만, **산업용 서비스·배포**에 강점이 있는 경우가 많습니다.

1. **GPU/TPU 지원** — TPU(구글 전용 하드웨어)까지, 대규모 연산에 유리
2. **풍부한 배포 옵션** — 웹·모바일·서버·IoT 등

수업 메모: **PyTorch 기반 논문이 더 많이 나오고 있다.**

> **쉽게 이해하기**  
> 둘 다 “딥러닝 레고 상자”입니다.  
> 이 수업은 **PyTorch**로 실습합니다. 연구·실험 예제가 많은 편입니다.  
> TensorFlow는 **서비스에 올려 배포**할 때 자주 거론됩니다. 입문 단계에서는 하나만 먼저 익혀도 됩니다.

---

## 9. conda로 PyTorch 환경 만들기

### Windows (CPU)

```bash
# 1. 새 conda 환경 (Python 3.10)
conda create -n torch-env python=3.10 -y

# 2. 활성화
conda activate torch-env

# 3. PyTorch 설치 (CPU)
conda install pytorch torchvision torchaudio cpuonly -c pytorch -y

# 4. Jupyter 커널 등록
conda install ipykernel -y
python -m ipykernel install --user --name=torch-env --display-name "Python (torch-env)"

# 5. 노트북
conda install notebook -y
# (또는: pip install notebook)
python -m notebook
```

입문 실습 노트북: [`PyTorch/01_tensor_linear_regression.ipynb`](./PyTorch/01_tensor_linear_regression.ipynb) (`torch-env` 커널 권장)

### macOS

```bash
# 1. 환경 만들기
conda create -n torch-env python=3.10 -y

# 2. 활성화
conda activate torch-env

# 3. PyTorch 설치 (cpuonly 제외)
conda install pytorch torchvision torchaudio -c pytorch -y

# 4. Jupyter 커널 등록
conda install ipykernel -y
python -m ipykernel install --user --name=torch-env --display-name "Python (torch-env)"

# 5. 노트북
conda install notebook -y
python -m notebook
```

입문 실습 노트북: [`PyTorch/01_tensor_linear_regression.ipynb`](./PyTorch/01_tensor_linear_regression.ipynb) (`torch-env` 커널 권장)

참고 링크 (Notion 북마크):

- [Pytorch Tensor 소개](https://tutorials.pytorch.kr/beginner/introyt/tensors_deeper_tutorial.html)
- [torch.Tensor — PyTorch 문서](https://docs.pytorch.org/docs/stable/tensors.html)

> **쉽게 이해하기**  
> `torch-env` 는 “딥러닝 연습용 방”입니다.  
> 방에 Python · PyTorch · Jupyter를 넣고, 노트북에서 그 방을 고르면 됩니다.  
> 다음 세션에서는 그 위에서 **NumPy · 벡터 · 내적**을 정리합니다([`session02`](./session02.md)).

---

## 10. 앞 내용과의 연결

| 곳                             | 연결                                    |
| ------------------------------ | --------------------------------------- |
| Machine Learning session10     | MSE · 경사하강 · \( w, b \)             |
| Deep Learning session01 (이번) | 미분 · 딥러닝 개요 · 신경망 · 환경 설정 |
| Deep Learning session02        | NumPy · 선형대수 · 내적                 |

머신러닝 노트: [`../Machine Learning/README.md`](../Machine%20Learning/README.md)

---

## 복습 체크 (스스로)

1. \( a \)와 \( b \) 중 기울기를 바꾸는 것은?
2. \( f'(x) \) 의 극한 식을 적어 보세요.
3. \( y = x^2 \) 에서 \( x = 2 \)일 때 순간 변화율은?
4. 딥러닝에서 “Deep”이 뜻하는 것은?
5. 가중치 갱신식 `New W = old W − (Learning Rate) × (Gradient)` 에서 마이너스는 왜 붙나요?
6. PyTorch 환경 이름 `torch-env`를 만드는 conda 명령은?

답 보기

1. \( a \) (가중치)
2. \( f'(x)=\lim\_{\Delta x \to 0}\dfrac{f(x+\Delta x)-f(x)}{\Delta x} \)
3. \( 4 \)
4. 층(Layer)이 여러 개인 신경망
5. 기울기 방향의 **반대**로 가야 손실(오차)이 줄어들기 때문
6. `conda create -n torch-env python=3.10 -y`

---

## 한눈에

```text
y=ax+b → a=가중치, b=편향
y=x^2  → f'(x)=2x  (예: x=2 → 4)

딥러닝 = 여러 층 신경망 + 텐서
입력층 → 은닉층 → 출력층

학습: 손실 확인 → 경사(편미분) → 학습률만큼 갱신 반복
New W = old W − lr × Gradient

도구: PyTorch / TensorFlow
환경: conda create -n torch-env ...
```

**이동:** [세션 02 →](./session02.md) · [세션 03 →](./session03.md) · [세션 04 →](./session04.md) · [세션 05 →](./session05.md) · [세션 06 →](./session06.md) · [세션 07 →](./session07.md) · [세션 08 →](./session08.md)
