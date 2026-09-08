# [Day 2 - Session 4] 조건문(if), 논리/멤버십 연산자 및 while 반복문

- **실습 파일**: `session4.py`
- **주요 내용**: 
  - 자료형의 참(True)과 거짓(False) 판정 기준
  - 논리 연산자 (`and`, `or`, `not`)
  - 멤버십 연산자 (`in`, `not in`: 리스트, 집합, 튜플, 딕셔너리 키 vs 값)
  - 중첩 조건문과 `pass` 키워드
  - `while` 반복문 기본 구조 및 조건 증감
  - 반복문 제어: `continue`, `break`
  - `while-else` 구문의 동작 원리

---

## 1. 실습 코드 및 단계별 해설

### 1.1 자료형의 참과 거짓 판정 기준

```python
# if boolean
# 참: "javascript", ["python"], (10,), {'a': 3}, 1, {'aa'}
# 거짓: "" (빈 문자열), [] (빈 리스트), () (빈 튜플), {} (빈 딕셔너리), 0, None
```

- **설명**:
  - 파이썬의 모든 자료형은 `if` 조건식에서 참 또는 거짓으로 평가될 수 있습니다.
  - **거짓(False)으로 평가되는 값**:
    - 빈 문자열(`""`), 빈 리스트(`[]`), 빈 튜플(`()`), 빈 딕셔너리(`{}`), 빈 집합(`set()`)
    - 숫자 `0`, 부동소수점 `0.0`
    - `None`, 불리언 `False`
  - **참(True)으로 평가되는 값**:
    - 비어 있지 않은 문자열, 리스트, 튜플, 딕셔너리, 집합
    - `0`이 아닌 모든 숫자(양수, 음수)

---

### 1.2 논리 연산자 (`and`, `or`, `not`)

```python
# and, or, not
money = 2000
card = True

print(money > 3000 and card) # False (False and True)
print(money > 3000 or card)  # True (False or True)
print(not money > 3000)      # True (not False)
```

- **설명**:
  - **`and` (논리곱)**: 양쪽 조건이 모두 참일 때만 `True` 반환.
  - **`or` (논리합)**: 양쪽 조건 중 하나라도 참이면 `True` 반환.
  - **`not` (논리부정)**: 조건식의 참/거짓 결과를 반대로 뒤집음.

---

### 1.3 멤버십 연산자 (`in`, `not in`)

```python
# in, not in
x = [10, 20, 30]
y = {70, 80, 90, 100}
z = { "name": "kim", "city": "seoul", "id": "gildong" }
m = (10, 20, 24)

print(25 in x)               # False (리스트 x에 25가 없음)
print(90 in y)               # True (집합 y에 90이 있음)
print(20 not in m)           # False (튜플 m에 20이 존재하므로 not in은 False)
print("city" in z)           # True (딕셔너리의 기본 in 검사는 Key 기준)
print("gildong" in z.values()) # True (Value 검사는 z.values()로 확인)
```

- **설명**:
  - **`x in 시퀀스/컬렉션`**: `x`가 해당 데이터 안에 포함되어 있으면 `True`.
  - **`x not in 시퀀스/컬렉션`**: `x`가 해당 데이터 안에 포함되어 있지 않으면 `True`.
  - **딕셔너리 주의점**:
    - `'city' in z`처럼 딕셔너리에 직접 `in`을 사용하면 **Key(키)**의 존재 여부를 검사합니다.
    - **Value(값)**의 존재 여부를 확인하려면 반드시 `z.values()`를 명시해야 합니다 (`"gildong" in z.values()`).

---

### 1.4 중첩 조건문과 `pass` 키워드

```python
# 중첩 조건문
grade = 'A'
total = 85

if grade == 'A':
  if total >= 90:
    print('장학생')
  elif total >= 80:
    pass # 아무 동작도 하지 않고 넘어감
  else:
    print('학생')
else:
  print('재시험')
```

- **설명**:
  - 조건문 내부에 또 다른 조건문을 넣어 세부적인 분기 처리가 가능합니다.
  - **`pass` 키워드**:
    - 문법적으로 문장이 필요하지만 아무런 동작도 수행하고 싶지 않을 때 사용합니다.
    - 임시로 코드를 비워둘 때 오류(IndentationError 등)를 방지하는 용도로 유용합니다.

---

### 1.5 `while` 반복문 기본 구조

```python
# while 조건:
#   실행코드
num = 5
while num > 0:
  print(num)
  num -= 1 # 조건 변화식 (없으면 무한 루프)
```

- **설명**:
  - 조건식이 참(`True`)인 동안 들여쓰기된 블록을 반복 실행합니다.
  - 반복문 내부에서 조건을 거짓으로 만들어줄 수 있는 증감식(`num -= 1`)이 반드시 포함되어야 무한 루프를 방지할 수 있습니다.

---

### 1.6 `continue`와 `break`

```python
n = 10
while n > 0:
  print(n)
  n -= 1
  if n == 2:
    continue # 아래 코드를 건너뛰고 바로 다음 반복 조건 검사로 이동
```

- **설명**:
  - **`break`**: 반복문 전체를 즉시 중단하고 빠져나옵니다.
  - **`continue`**: 이번 반복 주기의 나머지 코드를 건너뛰고, 곧바로 다음 반복 조건 검사로 건너뜁니다.

---

### 1.7 `while-else` 구문의 동작 원리

```python
a1 = ['water', 'python', 'java', 'phone']
s1 = 'py'
i = 0

while i < len(a1):
  if a1[i] == s1:
    break # 타깃을 찾으면 반복 탈출 (이때는 else 블록 실행 안 됨)
  i += 1
else:
  print('hi') # while문이 break로 끝나지 않고 정상 종료되었을 때 실행
```

- **설명**:
  - 파이썬 반복문은 고유하게 `else` 절을 가질 수 있습니다.
  - **`while-else` 동작 규칙**:
    - 조건식이 거짓이 되어 반복문이 **정상적으로 종료되었을 때 `else` 블록이 실행**됩니다.
    - 만약 반복 중간에 **`break`를 만나 루프를 빠져나오면 `else` 블록은 실행되지 않습니다.**
    - 검색 로직에서 "목표 대상을 끝내 찾지 못했을 때의 후처리"를 작성할 때 매우 유용합니다.

---

## 2. 핵심 요약 및 복습 포인트

| 문법 / 키워드 | 용도 및 동작 | 주의사항 |
| :--- | :--- | :--- |
| **빈 컨테이너** | `""`, `[]`, `()`, `{}`는 `if`에서 `False` | 데이터 존재 유무를 `if lst:`로 간결하게 검사 가능 |
| **`in` (딕셔너리)** | `'key' in dic`은 Key 존재 검사 | Value 검사 시 `dic.values()` 필수 |
| **`pass`** | 문법적 형태만 유지하고 아무 작업 안 함 | 미구현 함수나 빈 분기 처리에 사용 |
| **`break`** | 루프 즉시 탈출 | `while-else`의 `else` 블록도 건너뜀 |
| **`continue`** | 현재 회차 건너뛰고 다음 회차로 진행 | 무한 루프에 빠지지 않도록 증감식 위치 확인 |
| **`while-else`** | `break` 없이 루프 완료 시 실행 | 검색 실패 플래그 변수 없이 간결하게 작성 가능 |
