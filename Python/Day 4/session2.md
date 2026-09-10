# [Day 4 - Session 2] 파이썬 주요 내장 함수 14종 및 map/filter/lambda/컴프리헨션 활용

- **실습 파일**: `session2.py`
- **기본 교재**: _Do it! 점프 투 파이썬_ (내장 함수 편)
- **주요 내용**: 
  - 수치 연산 및 판정 함수: `abs()`, `all()`, `any()`, `divmod()`, `pow()`, `round()`
  - 문자/인코딩 및 속성 검사: `chr()`, `ord()`, `dir()`
  - 시퀀스 인덱스 부여 및 병합: `enumerate()`, `zip()`, `range()`
  - 최댓값 및 최솟값: `max()`, `min()`
  - 함수형 프로그래밍 핵심: `filter()`와 `map()` (일반 함수 vs 람다 표현식 비교)
  - `map`/`filter`와 리스트 컴프리헨션(List Comprehension) 상호 변환 실전 패턴

---

## 1. 실습 코드 및 단계별 해설

### 1.1 절댓값(`abs`)과 참/거짓 판정(`all`, `any`)

```python
# 절대값
print(abs(3))    # 3
print(abs(-3))   # 3
print(abs(-1.2)) # 1.2

# 모든 요소가 참인지 판단 (all)
print(all([1, 2, 3]))    # True
print(all([1, 2, 3, 0])) # False (0은 거짓이므로 False)
print(all([]))           # True  (빈 이터러블인 경우 True 반환 - 공허참(Vacuous truth))

# 하나라도 참인지 판단 (any)
print(any([1, 2, 3, 0])) # True  (1, 2, 3이 참이므로 True)
print(any([0, '']))      # False (모든 요소가 거짓이므로 False)
print(any([]))           # False (빈 이터러블인 경우 False 반환)
```

- **설명**:
  - **`abs(x)`**: 숫자의 부호를 제거한 절댓값을 반환합니다.
  - **`all(iterable)`**: 모든 원소가 참(`True`)이어야 `True`를 반환합니다. 원소 중 하나라도 `0`, `""`, `None` 등 거짓이 있으면 `False`입니다. *(빈 리스트 `all([])`는 `True`를 반환함에 유의)*
  - **`any(iterable)`**: 원소 중 단 하나라도 참이면 `True`를 반환합니다. 모든 원소가 거짓이거나 비어있으면 `False`입니다.

---

### 1.2 문자 $\leftrightarrow$ 유니코드 코드 포인트 변환 (`chr`, `ord`)

```python
# chr - 정수(유니코드 코드 포인트)를 문자로 리턴
print(chr(97))    # 'a'
print(chr(44032)) # '가'

# ord - 문자를 정수(유니코드 코드 포인트)로 리턴
print(ord('a'))   # 97
print(ord('가'))  # 44032
```

- **설명**:
  - **`chr(i)`**: 유니코드 숫자(정수)에 해당하는 단일 문자를 반환합니다.
  - **`ord(c)`**: 단일 문자의 유니코드 정수 값을 반환합니다 (`chr`과 `ord`는 정확히 역함수 관계).
  - 암호화, 문자열 인코딩 판별, 알파벳 순서 비교 시 자주 쓰입니다.

---

### 1.3 객체의 속성/메서드 목록 확인 (`dir`)

```python
# dir - 객체가 지닌 변수나 메서드 목록을 리스트로 리턴
print(dir([1, 2, 3]))   # 리스트 객체의 메서드 목록 ('append', 'extend', 'sort' 등)
print(dir({'1': 'a'}))  # 딕셔너리 객체의 메서드 목록 ('keys', 'values', 'items' 등)
```

- **설명**:
  - `dir(객체)`: 해당 데이터 타입이나 객체가 내부적으로 지원하는 속성(변수)과 함수(메서드) 목록을 문자열 리스트로 한눈에 보여줍니다.
  - 파이썬 대화형 콘솔이나 디버깅 시 특정 객체의 사용 가능한 기능을 즉시 확인할 때 필수적인 함수입니다.

---

### 1.4 몫과 나머지 튜플 반환 (`divmod`)

```python
# divmod - 인자 a, b를 받아 몫과 나머지를 튜플로 리턴
print(divmod(7, 3)) # (2, 1) -> 몫: 2, 나머지: 1
```

- **설명**:
  - `divmod(a, b)`는 `(a // b, a % b)`와 동일하며, 연산을 한 번에 수행하여 튜플로 반환합니다.

---

### 1.5 인덱스와 요소를 함께 순회하는 `enumerate()`

```python
# 리스트 순회 (인덱스, 값)
for i, name in enumerate(['body', 'foo', 'bar']):
  print(i, name)
# 0 body
# 1 foo
# 2 bar

# 딕셔너리 순회 (인덱스, 키)
for i, key in enumerate({'a': 'body', 'b': 'foo', 'c': 'bar'}):
  print(i, key)
# 0 a
# 1 b
# 2 c
```

- **설명**:
  - `enumerate(iterable)`: 순서가 있는 시퀀스를 순회할 때 **현재 인덱스 번호와 원소값**을 `(인덱스, 원소)` 형태의 튜플로 묶어서 반환합니다.
  - 루프 외부에서 별도의 카운터 변수(`i = 0; i += 1`)를 둘 필요 없이 안전하고 깔끔하게 인덱스를 다룰 수 있습니다.

---

### 1.6 조건 필터링 함수: `filter()` (일반 함수 vs 람다)

```python
# 1. 기존 for 반복문 방식 (양수 필터링)
def positive(l):
  result = []
  for i in l:
    if i > 0:
      result.append(i)
  return result

print(positive([1, -3, 2, 0, -5, 6])) # [1, 2, 6]

# 2. filter + 일반 함수
def positive(x):
  return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6]))) # [1, 2, 6]

# 3. filter + lambda (가장 간결한 형태)
filter1 = list(filter(lambda x: x < 3, range(1, 6)))
print(filter1) # [1, 2]
```

- **설명**:
  - **`filter(함수, 이터러블)`**: 이터러블의 각 원소를 첫 번째 인자인 함수에 전달하여, **함수의 반환값이 `True`인 원소들만 걸러내는 이터레이터**를 반환합니다.
  - 최종 결과를 보려면 `list()`로 묶어 변환해야 합니다.

---

### 1.7 요소 일괄 변환 함수: `map()` (일반 함수 vs 람다)

```python
# 1. 기존 for 반복문 방식 (각 요소를 2배로)
def two_times(numberList):
  result = []
  for number in numberList:
    result.append(number * 2)
  return result

result = two_times([1, 2, 3, 4])
print(result) # [2, 4, 6, 8]

# 2. map + 일반 함수
def two_times(x):
  return x * 2

print(list(map(two_times, [1, 2, 3, 4]))) # [2, 4, 6, 8]

# 3. map + lambda
list1 = [1, 2, 3, 4, 5]
re3 = list(map(lambda x: x + 10, list1))
print(re3) # [11, 12, 13, 14, 15]

map2 = list(map(lambda x: x + 100, range(1, 11)))
print(map2) # [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
```

- **설명**:
  - **`map(함수, 이터러블)`**: 이터러블의 모든 원소에 지정한 함수를 적용한 결과로 구성된 이터레이터를 반환합니다.
  - 리스트의 모든 요소를 일괄적으로 형 변환(예: `map(int, input().split())`)하거나 계산식을 적용할 때 필수적으로 사용됩니다.

---

### 1.8 최댓값/최솟값, 거듭제곱, 반올림 (`max`, `min`, `pow`, `round`)

```python
# max, min
print(max([1, 2, 3]))   # 3
print(max("python"))    # 'y' (알파벳 아스키 코드 기준 가장 큰 값)

print(min([1, 2, 3]))   # 1
print(min("python"))    # 'h' (알파벳 아스키 코드 기준 가장 작은 값)

# pow (거듭제곱)
print(pow(2, 4)) # 16 (2의 4제곱, 2 ** 4와 동일)
print(pow(3, 3)) # 27 (3의 3제곱)

# round (반올림)
print(round(4.6))              # 5
print(round(3.141231234, 2))   # 3.14 (소수점 둘째 자리까지 반올림)
```

- **설명**:
  - `max()`, `min()`: 숫자뿐만 아니라 문자열에서도 알파벳/유니코드 코드 포인트 크기를 기준으로 최댓값과 최솟값을 찾습니다.
  - `round(숫자, 자릿수)`: 자릿수를 생략하면 가장 가까운 정수로, 지정하면 해당 소수점 위치까지 반올림합니다.

---

### 1.9 시퀀스 병합: `zip()`

```python
# 동일한 개수로 이루어진 시퀀스들을 같은 인덱스끼리 묶어서 튜플로 반환
print(list(zip([1, 2, 3], [4, 5, 6]))) # [(1, 4), (2, 5), (3, 6)]
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip('abc', 'def'))) # [('a', 'd'), ('b', 'e'), ('c', 'f')]
```

- **설명**:
  - `zip(*iterables)`: 여러 개의 반복 가능 객체에서 같은 위치(인덱스)에 있는 원소들을 묶어 튜플로 엮어줍니다.
  - 길이가 서로 다를 경우 가장 짧은 이터러블의 길이에 맞춰 종료됩니다.
  - 두 리스트를 `dict(zip(keys, values))` 형태로 한 번에 딕셔너리로 결합할 때 매우 유용합니다.

---

### 1.10 `map`/`filter` vs 리스트 컴프리헨션 상호 변환 비교

```python
list1 = [1, 2, 3, 4, 5]

# 1. 제곱 연산 (map + 일반 함수)
def square(x):
  return x ** 2
re1 = list(map(square, list1))
print(re1) # [1, 4, 9, 16, 25]

# 2. 제곱 연산 (map + lambda)
re2 = list(map(lambda x: x ** 2, list1))
print(re2) # [1, 4, 9, 16, 25]

# 3. 제곱 연산 (리스트 컴프리헨션)
re3 = [x ** 2 for x in list1]
print(re3) # [1, 4, 9, 16, 25]

# 4. 짝수 필터링 (리스트 컴프리헨션)
re4 = [x for x in range(1, 21) if x % 2 == 0]
print(re4) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

- **설명**:
  - 파이썬에서는 `map()`이나 `filter()`를 사용하는 것보다 **리스트 컴프리헨션(`[x**2 for x in list1]`)**을 사용하는 것이 더 직관적이고 가독성이 높으며, 파이써닉(Pythonic)한 코드로 널리 권장됩니다.
  - 그러나 기존에 선언된 함수가 있거나(예: `map(int, ...)`), 메모리를 절약하는 지연 평가(Lazy Evaluation)가 필요할 때는 `map`/`filter`도 여전히 강력합니다.

---

## 2. 핵심 요약 (내장 함수 총정리)

| 함수 | 기능 설명 | 반환 예시 |
| :--- | :--- | :--- |
| **`abs(x)`** | 숫자의 절댓값 | `abs(-5)` $\rightarrow$ `5` |
| **`all(iter)`** | 모든 요소가 참이면 `True` (빈 값은 `True`) | `all([1, 2, 0])` $\rightarrow$ `False` |
| **`any(iter)`** | 하나라도 참이면 `True` (빈 값은 `False`) | `any([0, 1])` $\rightarrow$ `True` |
| **`chr(i)`** | 유니코드 숫자를 해당 문자로 변환 | `chr(97)` $\rightarrow$ `'a'` |
| **`ord(c)`** | 문자를 유니코드 숫자로 변환 | `ord('a')` $\rightarrow$ `97` |
| **`dir(obj)`** | 객체의 변수/메서드 목록 리턴 | `dir([])` |
| **`divmod(a, b)`** | `(몫, 나머지)` 튜플 반환 | `divmod(7, 3)` $\rightarrow$ `(2, 1)` |
| **`enumerate(iter)`**| `(인덱스, 요소)` 튜플 생성 | `enumerate(['a', 'b'])` |
| **`filter(f, iter)`**| 조건 함수 `f`가 참인 요소만 추출 | `list(filter(lambda x: x>0, [-1, 2]))` $\rightarrow$ `[2]` |
| **`map(f, iter)`** | 모든 요소에 함수 `f`를 적용 | `list(map(lambda x: x*2, [1, 2]))` $\rightarrow$ `[2, 4]` |
| **`max()` / `min()`**| 최댓값 / 최솟값 반환 | `max([1, 3, 2])` $\rightarrow$ `3` |
| **`pow(x, y)`** | $x$의 $y$ 제곱 | `pow(2, 3)` $\rightarrow$ `8` |
| **`round(n, d)`** | 반올림 | `round(3.1415, 2)` $\rightarrow$ `3.14` |
| **`zip(*iters)`** | 동일 위치 요소들을 튜플로 묶기 | `list(zip([1, 2], ['a', 'b']))` $\rightarrow$ `[(1, 'a'), (2, 'b')]` |
