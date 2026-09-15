# [Day 7 - Session 3] 이터레이터(Iterator)와 제너레이터(Generator)

- **실습 파일**: `session3.py`
- **주요 내용**:
  - 이터러블(Iterable)과 이터레이터(Iterator)의 개념 및 차이
  - `iter()`, `next()` 내장 함수와 `StopIteration` 예외 처리
  - `for` 반복문의 내부 동작 원리 및 이터레이터의 1회성 소비(Exhaustion)
  - `__iter__()`, `__next__()`를 구현한 커스텀 이터레이터 클래스(`Cnt`)
  - 제너레이터(Generator)의 개념, `yield` 키워드, 지연 평가(Lazy Evaluation)와 메모리 효율성

---

## 1. 실습 코드 및 단계별 해설

### 1.1 이터러블과 이터레이터 기초

```python
# 리스트는 반복 가능한 객체(Iterable)
a = [1, 2, 3]

# iter() 함수를 호출하여 이터레이터(Iterator)로 변환
ia = iter(a)
print(type(ia))  # <class 'list_iterator'>

# next() 함수를 호출하여 원소를 하나씩 순차적으로 반환
print(next(ia))  # 1
print(next(ia))  # 2
print(next(ia))  # 3
# print(next(ia))  # 더 이상 꺼낼 원소가 없으면 StopIteration 예외 발생
```

- **설명**:
  - **이터러블(Iterable)**: `for` 문이나 `iter()` 함수에 전달할 수 있는 반복 가능한 모든 객체 (예: `list`, `str`, `tuple`, `dict` 등).
  - **이터레이터(Iterator)**: `next()` 메서드를 통해 원소를 하나씩 꺼내올 수 있는 객체.
  - 끝에 도달하면 `StopIteration` 예외를 발생시켜 반복이 종료되었음을 알립니다.

---

### 1.2 `for` 문의 내부 동작과 이터레이터의 1회성 소비

```python
ia = iter(a)

for i in ia:
  print(i)
# 1, 2, 3 출력

# 이터레이터는 한 번 끝까지 소비되면 재사용할 수 없음
for i in ia:
  print(i)
# 아무것도 출력되지 않음
```

- **설명**:
  - `for` 문은 내부적으로 `iter()`를 호출하여 이터레이터를 생성하고, 매 반복마다 `next()`를 호출하며, `StopIteration` 예외가 발생하면 조용히 반복을 종료합니다.
  - 이터레이터는 내부 커서(Position)가 이미 마지막을 가리키고 있으므로 재사용할 수 없으며, 다시 순회하려면 새 이터레이터를 생성해야 합니다.

---

### 1.3 커스텀 이터레이터 클래스 구현: `Cnt`

```python
class Cnt:
  def __init__(self, stop):
    self.current = 0
    self.stop = stop

  def __iter__(self):
    return self  # 이터레이터 프로토콜 준수: 자기 자신을 반환

  def __next__(self):
    if self.current < self.stop:
      result = self.current
      self.current += 1
      return result
    else:
      raise StopIteration  # 종료 시 예외 발생

c = Cnt(5)
for i in c:
  print(i)
# 출력: 0, 1, 2, 3, 4
```

- **설명**:
  - 클래스가 이터레이터로 동작하려면 **이터레이터 프로토콜(Iterator Protocol)**을 만족해야 합니다.
  - `__iter__()`: 이터레이터 객체 자신(`self`)을 반환합니다.
  - `__next__()`: 다음 원소를 반환하며, 종료 조건 도달 시 `raise StopIteration`을 수행합니다.

---

### 1.4 제너레이터(Generator)와 `yield`

```python
def get():
  for i in range(1, 100000):
    yield i * 2

g = get()  # 함수가 즉시 실행되지 않고 제너레이터 객체만 생성
print(next(g))  # 2 (요청 시점에 비로소 1번째 계산 수행)
print(next(g))  # 4 (요청 시점에 2번째 계산 수행)
```

- **설명**:
  - 제너레이터는 `yield` 키워드를 사용하여 이터레이터를 손쉽게 만드는 특수한 함수입니다.
  - **지연 평가(Lazy Evaluation)**: 100,000개의 데이터를 메모리에 한꺼번에 올리지 않고, `next()`로 값을 요구할 때마다 1개씩 연산하여 반환합니다.
  - 일반 함수는 `return` 시 스택 프레임이 정리되지만, 제너레이터 함수는 `yield` 위치에서 함수의 실행 상태(로컬 변수, 실행 위치 등)가 자동으로 보존됩니다.

---

## 2. 이터레이터 vs 제너레이터 비교표

| 구분 | 이터레이터 (Iterator) | 제너레이터 (Generator) |
| :--- | :--- | :--- |
| **정의 방식** | 클래스 내부에 `__iter__`, `__next__` 구현 | 함수 내부에 `yield` 키워드 사용 |
| **코드 복잡도** | 상태 변수(`self.current`) 관리 및 예외 처리 코드 필요 | 간결함 (상태 변수와 `StopIteration`이 자동 관리됨) |
| **메모리 효율** | 데이터 전체를 보관하지 않고 순차 생성 가능 | **극대화** (필요한 순간에만 값을 계산하여 방출) |
| **종료 방식** | `raise StopIteration` 명시적 발생 | 함수의 실행이 끝나면 자동으로 `StopIteration` 발생 |
| **상태 유지** | 인스턴스 변수에 직접 상태 보존 | 함수 실행 컨텍스트(스택 상태)가 자동 보존 |
