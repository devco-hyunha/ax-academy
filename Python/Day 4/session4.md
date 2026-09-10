# [Day 4 - Session 4] 객체지향 프로그래밍(OOP) 기초: 클래스, 객체, 인스턴스, 메서드와 변수

- **실습 파일**: `session4.py`
- **주요 내용**:
  - 클래스(Class)와 객체(Object), 인스턴스(Instance)의 개념 및 차이
  - 생성자 메서드 `__init__()`와 문자열 표현 메서드 `__str__()`
  - 인스턴스 변수(`self.변수명`)와 인스턴스 메서드(사칙연산 클래스 `Func`)
  - 클래스 변수 vs 인스턴스 변수의 동작 원리와 네임스페이스
  - 메서드 호출 방식: 클래스를 통한 호출(`ClassName.func(instance)`) vs 인스턴스를 통한 호출(`instance.func()`)
  - `self` 키워드의 본질과 메모리 주소(`id(self)`)

---

## 1. 실습 코드 및 단계별 해설

### 1.1 객체(Object)와 인스턴스(Instance)의 개념 및 차이

```python
# 객체
# class 설계도
# object 설계도를 바탕으로 실제 만들어진 제품

# 클래스
# self, 인스턴스 메소드, 인스턴스 변수
# 클래스 메소드, 클래스 변수

# 객체(Object) : 클래스의 인스턴스를 포함한 모든 파이썬 데이터

# 객체와 인스턴스의 차이
# 클래스로 만든 객체를 인스턴스라고 함
# 인스턴스라는 말은 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용
# a 는 인스턴스 보다 객체라는 말이 더 어울림
# b 는 a의 객체 보다 b는 a의 인스턴스라는 말이 더 어울림
# 인스턴스 : 특정 클래스에 의해 생성된 객체를 지칭
```

- **설명**:
  - **클래스(Class)**: 객체를 생성하기 위한 틀, 청사진, 설계도입니다.
  - **객체(Object)**: 파이썬에서 메모리에 할당된 모든 실체(데이터, 함수 등)를 포괄하는 넓은 의미의 단어입니다. (예: `p1은 객체이다.`)
  - **인스턴스(Instance)**: 특정 클래스와의 관계(소속감)를 강조할 때 사용하는 단어입니다. (예: `p1은 Func 클래스의 인스턴스이다.`)

---

### 1.2 생성자(`__init__`), 매직 메서드(`__str__`), 사칙연산 인스턴스 메서드

```python
class Func:
  def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email
    
  def __str__(self):
    return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"

  def set_data(self, a, b):
    self.a = a
    self.b = b

  def add(self):
    return self.a + self.b
  
  def sub(self):
    return self.a - self.b
  
  def mul(self):
    return self.a * self.b
  
  def div(self):
    return self.a / self.b


p1 = Func("John", 20, "john@example.com")
p1.set_data(1, 2)
print(p1.add())   # 3
print(p1.sub())   # -1
print(p1.mul())   # 2
print(p1.div())   # 0.5
print(p1)         # Name: John, Age: 20, Email: john@example.com
```

- **설명**:
  - **`__init__(self, ...)`**: 객체가 생성(`Func(...)`)될 때 자동으로 호출되는 **초기화(생성자) 메서드**입니다. `self.변수명` 형태로 인스턴스 고유의 상태(속성)를 바인딩합니다.
  - **`__str__(self)`**: `print(p1)`이나 `str(p1)`을 호출했을 때 사용자 친화적인 문자열로 객체를 표현하도록 정의하는 특수 매직 메서드(Dunder Method)입니다.
  - **`set_data(self, a, b)`**: 인스턴스 변수 `self.a`, `self.b`를 동적으로 생성하고 값을 할당합니다.
  - **사칙연산 메서드 (`add`, `sub`, `mul`, `div`)**: 인스턴스 변수에 접근(`self.a`, `self.b`)하여 연산 결과를 반환합니다.

---

### 1.3 클래스 변수 vs 인스턴스 변수

```python
class Profile:
  name = 'gildong' # 클래스 변수
  def __init__(self, age, name = name):
    self.name = name
    self.age = age

user1 = Profile(20, 'john')
print(user1.name)  # john
print(user1.age)   # 20

user2 = Profile(30, 'jane')
print(user2.name)  # jane
print(user2.age)   # 30

print(Profile.name)  # gildong

print("{0} {1} {2} {3} ".format(user1.name, user1.age, user2.name, user2.age))
# 출력: john 20 jane 30 
```

- **설명**:
  - **클래스 변수 (`Profile.name`)**:
    - 클래스 정의 바로 아래에 선언된 변수로, 해당 클래스로 생성된 모든 인스턴스가 공용으로 접근할 수 있는 공간에 저장됩니다.
    - `Profile.name`으로 직접 접근 가능합니다.
  - **인스턴스 변수 (`self.name`, `self.age`)**:
    - `self.name`처럼 각 인스턴스마다 독립적으로 생성되고 유지되는 고유한 변수입니다.
    - `user1.name`과 `user2.name`은 서로 다른 메모리 공간을 가집니다.
  - **매개변수 기본값 `name = name`**:
    - 클래스 정의 시점에 평가되어 클래스 변수 `'gildong'`이 인자의 기본값으로 지정됩니다. 인자가 주어지면(`'john'`, `'jane'`) 전달된 값으로 인스턴스 변수가 덮어씌워집니다.

---

### 1.4 메서드 호출 방식과 `self`의 동작 원리

```python
class Test:
  def func():# 클래스 메소드
    print("Test func")

  def func2(self):# 인스턴스 메소드
    print(id(self))
    print("Test func2")

Test.func()
t = Test()

# 클래스 메소드로 호출시, self 인자를 넘겨줘야 함
Test.func2(t)
# t.func() #인스턴스 메소드로 호출시, 자동으로 self 인자가 전달됨
t.func2()

Test.func2(Test)
```

- **설명**:
  - **`Test.func()`**:
    - 매개변수가 없는 함수입니다. 인스턴스를 거치지 않고 클래스 이름으로 직접 호출(`Test.func()`)할 수 있습니다.
    - 만약 인스턴스를 통해 호출하면(`t.func()`), 파이썬이 첫 번째 인자로 인스턴스 `t`를 자동 전달하므로 `TypeError: Test.func() takes 0 positional arguments but 1 was given` 에러가 발생합니다.
  - **`self`의 본질**:
    - `self`는 **호출한 인스턴스 객체 자기 자신**을 가리키는 참조값입니다.
    - `t.func2()`로 호출하면 파이썬 내부에서 자동으로 `Test.func2(t)`로 변환되어 첫 번째 인자(`self`)에 `t`가 전달됩니다.
    - `print(id(self))`와 `print(id(t))`를 실행해보면 **완전히 동일한 메모리 주소값**을 가집니다.
  - **`Test.func2(Test)`**:
    - 파이썬에서는 클래스 자체도 일급 객체이므로 문법적으로 에러 없이 실행되며, 이때 `self` 매개변수에는 `Test` 클래스 객체 자체가 전달됩니다.

---

## 2. 핵심 요약 (객체지향 프로그래밍 핵심 정리)

### 2.1 클래스 구성 요소 비교

| 구분 | 클래스 변수 | 인스턴스 변수 |
| :--- | :--- | :--- |
| **선언 위치** | 클래스 블록 내부 (메서드 밖) | 메서드 내부 (`self.변수명 = 값`) |
| **소유권** | 클래스 자체 및 모든 인스턴스가 공유 | 해당 인스턴스 객체만 단독 소유 |
| **접근 방식** | `클래스명.변수명` 또는 `인스턴스.변수명` | `인스턴스.변수명` |
| **용도** | 모든 객체가 공유해야 하는 공통 상수나 카운터 | 각 객체마다 달라야 하는 고유 상태값 |

### 2.2 메서드 호출 문법 비교

| 호출 방식 | 실제 파이썬 내부 동작 | 특징 |
| :--- | :--- | :--- |
| **`인스턴스.메서드(인자)`** | `클래스명.메서드(인스턴스, 인자)` | 가장 일반적이고 권장되는 호출 방식. `self`가 자동 전달됨 |
| **`클래스명.메서드(인스턴스, 인자)`** | `클래스명.메서드(인스턴스, 인자)` | 클래스를 통해 명시적으로 인스턴스를 넘겨 호출하는 방식 |
