# 세션 03: Numpy (대규모 산술계산 시 많이 사용)

- **ndarray (N-dimensional array)**: NumPy의 핵심 데이터 구조는 다차원 배열 객체
- 파이썬 기본 리스트보다 훨씬 빠르고 효율적
- 특징:
  - 모든 원소가 같은 타입 (ex: 전부 int, 전부 float)
  - 메모리에 연속적으로 저장 → 연산 속도 빠름
  - 벡터화 연산 지원 (반복문 없이도 배열 전체에 연산 가능)
- numpy array: 1차원 = vector, 2차원 = matrix, 3차원 이상 = tensor
- rank = array의 dimension (차원), shape = 각 dimension의 size

```python
import numpy as np

arr = np.array([1, 2, 3, 4])   # 1차원 배열
print(arr)                     # [1 2 3 4]
print(arr.dtype)               # int64
print(arr.shape)               # (4,) → 원소 4개짜리 1차원

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[0, 1])     # 2  (0행 1열)
print(arr[:, 2])     # [3 6] (모든 행, 2열)
print(arr[1, :])     # [4 5 6] (1행 전체)

arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())   # 평균 → 3.0
print(arr.std())    # 표준편차
print(arr.sum())    # 합
print(arr.max())    # 최댓값
```

## Transpose (행·열 전치)

- transpose는 행과 열의 위치를 바꾸는 연산이다.
- 수학적으로 `Aᵀ`는 원소 (i, j)를 (j, i)로 옮기는 연산이며, `ndarray.T`와 같은 의미다.

```python
import numpy as np

arr = np.array([[1, 2, 3],
               [4, 5, 6]])           # 2행 3열
print(arr.T)
# [[1 4]
#  [2 5]
#  [3 6]]                           # 3행 2열

print(arr.T.shape)                   # (3, 2) → shape가 (2, 3)에서 (3, 2)로 바뀜
print(arr.T[0, 1])                   # 4 → arr[1, 0]과 같은 위치
```

- 1차원 배열은 transpose해도 내용이 변하지 않는다. 벡터는 축이 하나뿐이라 전치해도 shape는 `(n,)` 그대로다.
- ML에서 특징(features)은 열, 표본은 행으로 배치하는 형태가 흔하다.

## transpose가 필요한 연산과 형태

- **내적·외적 연산에서 transpose가 연산 방향을 맞춰준다.** `X.T @ X`는 표본·특징 행렬을 축 순서에 따라 정리하는 대표 형태다.

```python
X = np.array([[1, 2, 3],
              [4, 5, 6]])           # 2행(표본) × 3열(특징)
Z = X.T @ X                         # (3×2) @ (2×3) → 특징 축 기준 (3, 3) 정리
print(Z)
# [[17 22 27]
#  [22 29 36]
#  [27 36 45]]
```

- 선형 회귀 `(X.T @ X)` 역을 구하는 공식도 대표적으로 transpose가 축 정렬을 담당한다.

## 다차원 transpose

- 3차원 tensor는 축 순서 `0, 1, 2`가 `2, 1, 0`으로 뒤집혀 `shape`가 거꾸로 바뀐다.
- 축 순서를 직접 지정하면 특정 축끼리만 전치할 수 있다.

```python
x = np.arange(24).reshape(2, 3, 4)  # 축 = (0, 1, 2)
print(x.T.shape)                     # (4, 3, 2) → 전체 축 순서 = (2, 1, 0)
print(x.transpose(0, 2, 1).shape)    # (2, 4, 3) → 축 순서 = (0, 2, 1)
```

## transpose가 계산 속도가 빠른 이유

- `.T`는 배열을 복사하지 않고 축 순서만 바꾸는 view 연산이다.

## `range()` vs `numpy.arange()`

| 구분      | range()               | numpy.arange()       |
| --------- | --------------------- | -------------------- |
| 소속      | 파이썬 내장 함수      | NumPy 라이브러리     |
| 반환 타입 | range 객체 (이터러블) | NumPy 배열 (ndarray) |
| 지원 타입 | 정수만 가능           | 정수 + 실수 가능     |
| 활용 분야 | 반복문, 인덱싱        | 수치계산, 배열 연산  |

## 난수 생성

- `np.random.seed()`: 난수를 생성할 때 사용하는 시작점(seed)을 고정
  - → 실행할 때마다 똑같은 난수 배열이 나온다. (재현 가능성 확보)
- `np.random.randn(5, 4)`: 표준 정규분포 (N(0, 1))에서 난수 생성
  - 평균(μ) = 0, 표준편차(σ) = 1
  - (5, 4) → 5행 4열짜리 2차원 배열
