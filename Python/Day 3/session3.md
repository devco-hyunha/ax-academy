# [Day 3 - Session 3] 함수(Function) 기초, 가변 인자(*args, **kwargs), 반환값 및 매개변수 기본값

- **실습 파일**: `session3.py`
- **주요 내용**: 
  - 함수 정의(`def`) 및 키워드 인자(`name=value`) 호출
  - 다중 반환값의 튜플 반환과 언패킹 처리
  - 딕셔너리 형태의 반환값 처리
  - 위치 가변 인자(`*args`)와 키워드 가변 인자(`**kwargs`)
  - 함수 매개변수의 선언 순서 규칙
  - 할인 계산기 실습 함수 `calcu()` (문자열 포매팅 3종 비교 및 `%` 기호 이스케이프 `%%`)
  - 매개변수 기본값(Default Parameter) 설정
  - 홀짝 판별 함수 및 가변 인자 평균 함수 작성

---

## 1. 실습 코드 및 단계별 해설

### 1.1 함수 정의, 반환값, 키워드 인자 호출

```python
# 함수 정의
def add(a, b):
  print('a:', a, end = ' + ')
  print('b:', b, end = ' = ' )
  return a + b

print(add(1, 2))          # 위치 인자 전달
print(add(a = 1, b = 2))  # 키워드 인자 지정
print(add(b = 2, a = 1))  # 키워드 인자 지정 시 순서 변경 가능

def say():
  return 'hi'             # 매개변수가 없는 함수

def printAdd(a, b):
  print(a + b)            # return이 없는 함수 (반환값은 None)

def printSay():
  print('hi')             # 매개변수와 return 모두 없는 함수
```

- **설명**:
  - `def 함수명(매개변수):` 형태로 선언하고 `return`으로 결과값을 돌려줍니다.
  - **키워드 인자(Keyword Arguments)**: `add(b=2, a=1)`처럼 매개변수 이름을 명시하여 호출하면 인자의 전달 순서가 바뀌어도 안전하게 매핑됩니다.
  - `return` 문이 없는 함수는 내부 코드를 실행한 뒤 암묵적으로 `None`을 반환합니다.

---

### 1.2 다중 반환값과 튜플 언패킹

```python
def multi(x):
  y1 = x * 5
  y2 = x * 10
  y3 = x * 20
  return y1, y2, y3 # 여러 값을 쉼표로 나열하여 반환 -> 튜플 1개로 패킹되어 반환됨

x, y, z = a = multi(2)

print(x, y, z)   # 10 20 40 (언패킹)
print(list(a))   # [10, 20, 40]
```

- **설명**:
  - 파이썬에서 `return y1, y2, y3`처럼 여러 값을 반환하면, 실제로는 **단 하나의 튜플 `(y1, y2, y3)`로 묶여서 반환**됩니다.
  - `x, y, z = multi(2)`와 같이 호출 측에서 **튜플 언패킹**을 통해 개별 변수로 나누어 받을 수 있습니다.

---

### 1.3 딕셔너리 형태의 반환값 처리

```python
def func3(x):
  y1 = x * 5
  y2 = x * 10
  y3 = x * 20
  return {'y1': y1, 'y2': y2, 'y3': y3}

a = func3(5)
print(a) # {'y1': 25, 'y2': 50, 'y3': 100}
print(a.get('y2')) # 50

for k in a.keys():
  print(k, end = ' : ')
  print(a.get(k))

print(list(a.values())) # [25, 50, 100]
```

- **설명**:
  - 결과값에 이름표(Key)를 붙여 구조화된 데이터를 반환하고자 할 때 딕셔너리 반환이 매우 효과적입니다.

---

### 1.4 위치 가변 인자 (`*args`)

```python
# *args : 인자들을 튜플(tuple)로 묶어서 받음
def add_many(*args):
  result = 0
  for i in args:
    result += i
  return result

c = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(c) # 55
```

- **설명**:
  - 매개변수 이름 앞에 `*`를 붙이면, 전달되는 임의 개수의 위치 인자들을 **하나의 튜플**로 묶어 처리합니다.
  - 인자의 개수가 몇 개가 되든 유연하게 동작하는 함수를 만들 수 있습니다.

---

### 1.5 키워드 가변 인자 (`**kwargs`) 및 매개변수 선언 순서

```python
# **kwargs: 키워드 인자들을 딕셔너리(dict)로 묶어서 받음
def func2(**kwargs):
  for i in kwargs.keys():
    print(i)

func2(name1 = '철수')
func2(name1 = '철수', name2 = '영희')
func2(name1 = '길동', name2 = '철수', name3 = '영희')

# 복합 매개변수 순서: (일반 인자 -> *args -> **kwargs)
def func3(arg1, arg2, *args, **kwargs):
  print(arg1, arg2, args, kwargs)
  return

func3(10, 20, 'kim', 'lee', age=10, addr='seoul')
# arg1=10, arg2=20, args=('kim', 'lee'), kwargs={'age': 10, 'addr': 'seoul'}
```

- **설명**:
  - `**kwargs`: `key=value` 형태로 전달된 임의 개수의 인자들을 **딕셔너리**로 묶어 받습니다 (`kwargs = {'name1': '철수', ...}`).
  - **매개변수 선언 순서 규칙 (매우 중요)**:
    - `일반 매개변수` $\rightarrow$ `*args` $\rightarrow$ `**kwargs` 순서를 반드시 지켜야 구문 에러(`SyntaxError`)가 발생하지 않습니다.

---

### 1.6 실전 문제: 조건별 할인 계산 함수 (`calcu`)

```python
# 15시에 방문하고 3개 이상 구매 시 10% 할인
# 12시에 방문하고 5개 이상 구매 시 20% 할인
def calcu(name, time, count, price):
  discount = 0
  if time == 15 and count >= 3:
    discount = 10
  elif time == 12 and count >= 5:
    discount = 20
  
  final_price = int(price / 100 * (100 - discount))

  # 1. f-string
  print(f'{name}씨는 {discount}% 할인= {final_price}원')
  
  # 2. C 스타일 서식문자 (% 기호 자체를 출력할 때는 %% 로 이스케이프!)
  print('%s씨는 %d%% 할인= %d원' % (name, discount, final_price))
  
  # 3. str.format()
  print('{0}씨는 {1}% 할인= {2}원'.format(name, discount, final_price))

calcu("형민", 15, 4, 20000)
calcu("종진", 12, 5, 50000)
calcu("한빈", 10, 2, 70000)
```

- **설명**:
  - 다중 조건문(`if-elif`)으로 할인율을 계산합니다.
  - **C 스타일 포매팅 주의점**: C 스타일 포매팅 문자열 내에서 퍼센트 기호(`%`) 자체를 일반 문자로 출력하려면 **`%%`**로 두 번 써서 이스케이프해야 합니다.

---

### 1.7 기본값 매개변수(Default Parameter)와 연습 함수

```python
# 홀짝 판별 함수
def is_odd(number):
  if number % 2 == 1:
    return True
  else:
    return False

# 가변 인자 평균 계산 함수
def avg_numbers(*args):
  result = 0
  for i in args:
    result += i
  return result / len(args)

# 기본값 매개변수 (old = 20)
def say(name, man, old = 20):
  print(name)
  if man:
    print('남자', old)
  else:
    print('여자', old)

say('juli', True)       # old를 생략하면 기본값 20 적용 -> '남자 20'
say('tom', False, 10)   # old에 10 전달 -> '여자 10'
```

- **설명**:
  - `old = 20`: 인자를 넘기지 않았을 때 사용할 기본값을 지정할 수 있습니다.
  - **주의**: 기본값을 설정하는 매개변수는 **반드시 일반 매개변수의 뒤쪽에 위치**해야 합니다 (`def say(old=20, name, man):`는 구문 에러).

---

## 2. 핵심 요약

| 개념 | 문법 | 동작 특징 |
| :--- | :--- | :--- |
| **다중 반환값** | `return a, b` | 실제로는 `(a, b)` 튜플 1개로 반환됨 |
| **위치 가변 인자** | `*args` | 전달된 임의 개수의 인자를 **튜플**로 수집 |
| **키워드 가변 인자**| `**kwargs` | 전달된 `k=v` 인자들을 **딕셔너리**로 수집 |
| **선언 순서** | `(arg, *args, **kwargs)` | 일반 인자 $\rightarrow$ 가변 인자 $\rightarrow$ 키워드 가변 인자 순서 준수 |
| **기본값 매개변수**| `def f(a, b=10):` | 기본값 매개변수는 반드시 뒤쪽에 배치 |
| **포매팅 % 이스케이프**| `'%d%%' % 10` | C 스타일에서 `%` 문자 출력 시 `%%` 사용 |
