# [Day 6 - Session 2] 예외 처리, 매직 메서드(`__call__`), 데코레이터(Decorator)

- **실습 파일**: `session2.py`
- **주요 내용**:
  - `try-except-else-finally` 예외 처리 기본 메커니즘
  - 파이썬 주요 내장 예외 종류 및 처리 방법
  - `Exception` 클래스 상속을 통한 사용자 정의 예외와 `raise`
  - `__call__` 매직 메서드를 활용한 호출 가능한(Callable) 객체
  - 함수형 데코레이터(`*args`, `**kwargs`)와 클래스형 데코레이터

---

## 1. 실습 코드 및 단계별 해설

### 1.1 예외 처리 기본 문법 및 주요 내장 예외

```python
# 예외 처리 기본 구조
try:
  # 예외 발생 가능성이 있는 코드
  pass
except ZeroDivisionError:
  # 숫자를 0으로 나눌 때 발생
  print('0으로 나눌 수 없습니다')
except IndexError:
  # 리스트 등 시퀀스의 인덱스 범위를 초과할 때 발생
  print('인덱싱 할 수 없습니다')
except NameError:
  # 정의되지 않은 변수를 참조할 때 발생
  print('선언되지 않은 변수입니다')
except KeyError:
  # 딕셔너리에 존재하지 않는 키를 조회할 때 발생
  print('존재하지 않는 키입니다')
except ValueError as e:
  # 부적절한 값(자료형은 맞으나 값이 올바르지 않음)일 때 발생
  print(e)
except TypeError:
  # 서로 다른 호환되지 않는 타입 간의 연산 수행 시 발생
  print('타입이 올바르지 않습니다')
else:
  # 예외가 전혀 발생하지 않았을 때만 실행
  print('정상 실행')
finally:
  # 예외 발생 여부와 상관없이 무조건 마지막에 실행 (리소스 해제 등)
  print('항상 실행')
```

---

### 1.2 사용자 정의 예외와 `raise`

```python
class MyError(Exception):
  def __str__(self):
    return '허용되지 않는 별명입니다'

def say_nick(nick):
  if nick == '바보':
    raise MyError()  # raise: 의도적으로 예외를 발생시키는 키워드
  print(nick)

try:
  say_nick('a')
  say_nick('바보')
except MyError as e:
  print(e)  # 출력: 허용되지 않는 별명입니다
```

- **설명**:
  - 내장 `Exception` 클래스를 상속받아 커스텀 예외 클래스(`MyError`)를 정의합니다.
  - `__str__()` 메서드를 오버라이딩하여 에러 출력 메시지를 지정할 수 있습니다.
  - `raise` 구문을 사용하여 비즈니스 로직에 맞지 않는 값이 전달되었을 때 예외를 발생시킵니다.

---

### 1.3 `__call__` 매직 메서드 (호출 가능한 객체)

```python
class add:
  def __init__(self, x):
    self.x = x

  def __call__(self, y):
    return self.x + y

# 인스턴스를 함수처럼 소괄호()로 호출
add2 = add(2)
print(add2(3))     # 출력: 5
print(add(2)(3))   # 출력: 5
```

- **설명**:
  - 클래스 내에 `__call__()` 메서드가 정의되어 있으면, 그 클래스로 만들어진 **인스턴스 객체를 함수처럼 `인스턴스(인자)` 형태로 호출**할 수 있습니다.
  - 이를 통해 객체의 상태(`self.x`)를 유지하면서 클로저(Closure) 함수처럼 동작시킬 수 있습니다.

---

### 1.4 함수형 데코레이터 (가변 인자 지원)

```python
def trace(func):
  def wrapper(*args, **wkargs):
    result = func(*args, **wkargs)
    print(args, wkargs, result)
    return result
  return wrapper

@trace
def big(*args):
  return max(args)

@trace
def mini(**kwargs):
  return min(kwargs.values())

print(big(10, 20))
# 출력:
# (10, 20) {} 20
# 20

print(mini(x=20, y=30, z=40))
# 출력:
# () {'x': 20, 'y': 30, 'z': 40} 20
# 20
```

- **데코레이터 동작 원리**:
  - `@trace`는 함수 정의 시점에 `big = trace(big)`을 자동으로 수행합니다.
  - 래퍼 함수 `wrapper`에서 `*args`와 `**kwargs`로 임의의 위치 인자 및 키워드 인자를 모두 받아 기존 함수(`func`)에 전달하고 결과를 가로채어 로깅/출력한 뒤 반환합니다.

---

### 1.5 클래스형 데코레이터

```python
class Tr:
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwds):
    print(self.func.__name__, 'start')
    self.func()
    print(self.func.__name__, 'end')

@Tr  # hi = Tr(hi) 실행 -> hi는 Tr의 인스턴스가 됨
def hi():
  print('hi')

hi()  # hi() 호출 시 Tr 인스턴스의 __call__() 실행
# 출력:
# hi start
# hi
# hi end
```

- **설명**:
  - 클래스를 데코레이터로 사용할 경우, `__init__`에서 대상 함수(`func`)를 속성으로 저장합니다.
  - 함수 호출 시 `__call__` 메서드가 실행되므로 전/후 처리 로직을 객체지향적인 방식으로 구현할 수 있습니다.
