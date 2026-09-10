# [Day 4 - Session 1] 변수의 스코프(Scope), 람다(lambda) 표현식, 일급 객체 함수 및 딕셔너리 동적 수집

- **실습 파일**: `session1.py`
- **주요 내용**: 
  - 함수의 변수 유효 범위(Scope): 지역 변수(Local Variable)와 전역 변수(Global Variable)의 차이
  - 람다(lambda) 표현식: 간결한 익명 함수 선언 및 `def` 함수와의 비교
  - 일급 객체(First-Class Citizen)로서의 함수: 함수를 변수에 할당(별칭/Alias) 및 다른 함수의 인자로 전달(고차 함수)
  - `while True`와 `input()`을 활용한 사용자 응답 기반 딕셔너리 동적 누적
  - 리스트 생성 기법 비교: 리스트 컴프리헨션 vs `list(range())`

---

## 1. 실습 코드 및 단계별 해설

### 1.1 함수 안에서 선언된 변수의 유효 범위 (Scope)

```python
a = 1
def vartest(a):
  a = a + 1

vartest(a)
print(a) # 1
```

- **설명**:
  - 함수 밖에서 정의된 `a = 1`은 **전역 변수(Global Variable)**입니다.
  - `vartest(a)`의 매개변수 `a`는 함수 내부에서만 살아있는 **지역 변수(Local Variable)**입니다.
  - 함수 안에서 `a = a + 1`을 수행하더라도, 이는 지역 변수 `a`의 값을 2로 바꾼 것일 뿐 함수 바깥의 전역 변수 `a`에는 아무런 영향을 주지 않습니다.
  - 따라서 함수 호출 후 `print(a)`의 결과는 여전히 원래 값인 `1`이 출력됩니다.
  - *(참고: 함수 내부의 변경값을 외부에 반영하려면 `return`으로 값을 돌려받아 재할당(`a = vartest(a)`)하거나 `global` 키워드를 사용합니다.)*

---

### 1.2 람다(lambda) 표현식과 일반 `def` 함수 비교

```python
# 1. 덧셈 람다 함수
add = lambda a, b: a + b
result = add(3, 4)
print(result) # 7

# 2. 곱셈 함수 def vs lambda
def multi(x, y):
  return x * y

multi = lambda x, y: x * y
print(multi(3, 4)) # 12

# 3. 10을 더하는 함수 def vs lambda
def plus(x):
  return x + 10

plus = lambda x: x + 10
print(plus(1)) # 11
```

- **설명**:
  - `lambda`는 함수를 딱 한 줄로 간결하게 만들 때 사용하는 **익명 함수(Anonymous Function)** 예약어입니다.
  - **기본 문법**: `lambda 매개변수1, 매개변수2, ... : 표현식`
  - `def` 키워드나 `return` 문 없이도 표현식의 평가 결과가 자동으로 반환됩니다.
  - `map()`, `filter()`, `sort(key=...)` 등 일회성 콜백 함수가 필요한 곳에 매우 빈번하게 사용됩니다.

---

### 1.3 일급 객체(First-Class Citizen)로서의 함수

```python
# 함수명을 변수에 할당 (별칭/Alias)
a = multi
print(a(4, 5)) # 20

# 함수를 다른 함수의 인자로 전달 (고차 함수)
def final(x, y, func1):
  print(x, y, func1(5, 6))

final(1, 2, multi) # 1 2 30
```

- **설명**:
  - 파이썬에서 **함수는 일급 객체(First-Class Citizen)**입니다.
    1. 함수를 일반 변수에 값처럼 대입할 수 있습니다 (`a = multi` $\rightarrow$ 이제 `a(4, 5)`로 호출 가능).
    2. 함수를 다른 함수의 매개변수(인자)로 전달할 수 있습니다 (`final(1, 2, multi)`).
    3. 함수의 반환값으로 또 다른 함수를 돌려줄 수도 있습니다 (클로저/데코레이터의 기반 원리).
  - `final(1, 2, multi)`는 내부에서 `func1(5, 6)`을 호출하며, 전달받은 `multi(5, 6)`이 실행되어 30이 계산됩니다.

---

### 1.4 `while True`와 `input()`을 활용한 딕셔너리 동적 수집

```python
dict = {}
while True:
  name = input('이름?')
  tv = input('좋아하는 방송?')
  dict[name] = tv

  ans = input('친구한테 물어볼까?')
  if ans == 'no':
    break

print(dict)
```

- **설명**:
  - `dict = {}` 빈 딕셔너리를 선언하고 사용자 입력을 반복해서 받아 저장합니다.
  - `dict[name] = tv`: 입력받은 이름을 Key로, 좋아하는 방송을 Value로 매핑하여 추가합니다.
  - `if ans == 'no': break`: 사용자가 'no'를 입력하면 `break`를 통해 무한 루프를 탈출하고 수집된 최종 딕셔너리를 출력합니다.

---

### 1.5 리스트 생성 방식 비교: 컴프리헨션 vs `list(range())`

```python
li1 = [i for i in range(1, 6)]
li2 = list(range(1, 6))

print(li1) # [1, 2, 3, 4, 5]
print(li2) # [1, 2, 3, 4, 5]
```

- **설명**:
  - **리스트 컴프리헨션 (`[i for i in range(1, 6)]`)**: 각 요소에 연산이나 조건 필터링(`if`)을 추가해야 할 때 유연하게 확장할 수 있습니다.
  - **`list(range(1, 6))`**: 단순 수열을 리스트로 바로 생성할 때는 가장 간결하고 명확한 방법입니다.

---

## 2. 핵심 요약 및 주의사항

1. **변수의 스코프 원칙**: 함수 내부에서 할당된 변수는 기본적으로 지역 변수이므로, 외부 전역 변수를 수정하지 않습니다.
2. **람다 표현식의 한계**: 람다는 단일 표현식만 지원하므로, 여러 줄의 로직이나 복잡한 조건 분기가 필요한 경우에는 `def` 함수를 사용하는 것이 바람직합니다.
3. **일급 함수**: 함수 이름을 변수에 담거나 인자로 전달할 때는 괄호 `()`를 붙이지 않고 **함수 이름 자체**를 넘겨야 합니다 (`multi` (O), `multi()` (X - 실행 결과가 전달됨)).
