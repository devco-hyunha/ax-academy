# 세션 05: Matplotlib

<!-- session-nav -->
**이동:** [← 세션 04](./session04.md) · [세션 06 →](./session06.md)

- 파이썬에서 2D 데이터 시각화 라이브러리
- 막대그래프, 선그래프, 히스토그램, 산점도, 파이차트 등 거의 모든 기본 그래프 지원

> **이 세션이 하는 일 (쉬운 말)**  
> 숫자만 잔뜩 적힌 표는 읽기 어렵습니다.  
> **Matplotlib**은 그 숫자를 **그림(그래프)** 으로 바꿔 주는 파이썬 도구입니다.  
> 오늘은 “어떤 상황에 어떤 그래프를 쓰는지”와,  
> 가장 자주 쓰는 그리기 코드(`plot`, `scatter`, `bar`, `hist`)를 익힙니다.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)          # 선 그래프
plt.title("Line Plot")  # 그래프 제목
plt.xlabel("X-axis")    # x축 이름
plt.ylabel("Y-axis")    # y축 이름
plt.show()
```

> **쉽게 이해하기**  
> **Matplotlib**은 숫자를 그래프로 그리는 도구입니다. `plt`로 불러 씁니다.  
> `plot` 등으로 그린 뒤 `title`·`xlabel`·`ylabel`을 붙이고 `show()`로 화면에 띄웁니다.

---

## 주요 그래프 종류

### (1) 선 그래프 (Line Plot)

```python
plt.plot([1, 2, 3], [1, 4, 9], marker='o', color='red', linestyle='--')
plt.title("Line Graph")
plt.show()
```

> **쉽게 이해하기**  
> **선 그래프(line plot)** 는 순서나 시간에 따른 **추세**를 볼 때 씁니다.  
> `marker`·`color`·`linestyle`로 모양을 바꿉니다.  
> 반·요일처럼 이름끼리 크기만 비교할 때는 막대 그래프가 더 잘 맞습니다.

---

### (2) 산점도 (Scatter Plot)

```python
x = [5, 7, 8, 7, 6, 9]
y = [99, 86, 87, 88, 100, 86]
plt.scatter(x, y, color='green')
plt.title("Scatter Plot")
plt.show()
```

> **쉽게 이해하기**  
> **산점도(scatter plot)** 는 두 숫자가 함께 커지는지, 흩어져 있는지 볼 때 씁니다.  
> 관측마다 점 하나씩 두고 선으로 이지 않습니다.  
> **피처(feature)** 와 **라벨(label)** 관계를 먼저 훑을 때 자주 씁니다.

---

### (3) 막대 그래프 (Bar Chart)

```python
x = ["A", "B", "C"]
y = [3, 7, 5]
plt.bar(x, y, color='blue')
plt.title("Bar Chart")
plt.show()
```

> **쉽게 이해하기**  
> **막대 그래프(bar chart)** 는 카테고리(이름)끼리 숫자를 비교할 때 씁니다.  
> x축은 그룹 이름, y축은 합·개수·평균 등입니다.  
> 시간 흐름은 선 그래프가 더 자연스럽습니다.

---

### (4) 히스토그램 (Histogram)

```python
import numpy as np

data = np.random.randn(1000)  # 정규분포 랜덤 데이터
plt.hist(data, bins=30, color='purple')
plt.title("Histogram")
plt.show()
```

> **쉽게 이해하기**  
> **히스토그램(histogram)** 은 연속 숫자가 어느 구간에 몰려 있는지 봅니다.  
> `bins`는 구간 개수입니다.  
> 막대 그래프는 정해진 이름을 비교하고, 히스토그램은 숫자를 구간으로 잘라 분포를 봅니다.

---

## 그래프 고르기 한눈에

```text
흐름·추세(시간/순서)     → 선 그래프 (Line)
두 숫자의 관계·흩어짐    → 산점도 (Scatter)
카테고리끼리 크기 비교   → 막대 그래프 (Bar)
숫자 값의 분포·몰림      → 히스토그램 (Histogram)
```

---

## 복습 체크 (스스로)

1. Matplotlib을 한 줄로 말하면 무엇인가요?
2. “날짜별 매출 변화”에는 어떤 그래프가 잘 맞나요?
3. 산점도와 선 그래프의 느낌 차이는 무엇인가요?
4. 막대 그래프와 히스토그램은 어떻게 다른가요?
5. `plt.show()`는 왜 쓰나요?

<details>
<summary>답 보기</summary>

1. 숫자를 2D 그래프로 그려 보는 파이썬 시각화 라이브러리.
2. 선 그래프(Line Plot). 흐름·추세를 보기 좋음.
3. 선은 순서/흐름을 이어서 보여 주고, 산점도는 관측을 점으로만 흩뿌려 관계를 봄.
4. 막대는 정해진 카테고리 비교. 히스토그램은 연속 숫자를 구간으로 나눠 분포를 봄.
5. 그려 둔 그래프를 화면에 실제로 보여 주기 위해.

</details>

<!-- session-nav -->
**이동:** [← 세션 04](./session04.md) · [세션 06 →](./session06.md)
