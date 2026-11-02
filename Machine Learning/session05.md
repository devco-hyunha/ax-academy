# 세션 05: Matplotlib

- 파이썬에서 2D 데이터 시각화 라이브러리
- 막대그래프, 선그래프, 히스토그램, 산점도, 파이차트 등 거의 모든 기본 그래프 지원

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

## 주요 그래프 종류

### (1) 선 그래프 (Line Plot)

```python
plt.plot([1, 2, 3], [1, 4, 9], marker='o', color='red', linestyle='--')
plt.title("Line Graph")
plt.show()
```

### (2) 산점도 (Scatter Plot)

```python
x = [5, 7, 8, 7, 6, 9]
y = [99, 86, 87, 88, 100, 86]
plt.scatter(x, y, color='green')
plt.title("Scatter Plot")
plt.show()
```

### (3) 막대 그래프 (Bar Chart)

```python
x = ["A", "B", "C"]
y = [3, 7, 5]
plt.bar(x, y, color='blue')
plt.title("Bar Chart")
plt.show()
```

### (4) 히스토그램 (Histogram)

```python
import numpy as np

data = np.random.randn(1000)  # 정규분포 랜덤 데이터
plt.hist(data, bins=30, color='purple')
plt.title("Histogram")
plt.show()
```
