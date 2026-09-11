# [Day 5 - Session 2] 클래스 상속(Inheritance), super(), 메서드 오버라이딩과 클래스 변수

- **실습 파일**: `session2.py`
- **주요 내용**:
  - 부모 클래스(슈퍼클래스)와 자식 클래스(서브클래스)의 상속 문법
  - `super()`를 통한 부모 클래스 생성자 및 메서드 호출
  - 메서드 오버라이딩(Method Overriding)의 개념과 구현
  - 점프 투 파이썬 5장 되새김 문제 (계산기 상속, 최대값 제한 계산기)
  - 클래스 변수를 이용한 인스턴스 카운팅 및 `__dict__` 네임스페이스 분석

---

## 1. 실습 코드 및 단계별 해설

### 1.1 상속과 super() 기본 문법: Car와 CampingCar

```python
# 부모 클래스 (Superclass)
class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.speed = 0

  def name(self):
    names = str(self.year) + ' ' + self.make + ' ' + self.model
    return names

  def getSpeed(self):
    print(str(self.speed) + '이다')

# 자식 클래스 (Subclass)
# 문법: class 자식클래스명(부모클래스명):
class CampingCar(Car):
  def __init__(self, make, model, year, bed):
    self.bed = bed
    super().__init__(make, model, year)  # 부모의 __init__ 호출

camp1 = CampingCar('tesla', 'A Class', 2017, 2)
print(camp1.name())
camp1.getSpeed()
```

- **설명**:
  - `class 자식클래스명(부모클래스명)` 형태로 기존 클래스의 모든 속성과 메서드를 상속받습니다.
  - `super().__init__(...)` 함수를 호출하여 부모 클래스의 초기화 로직을 그대로 재사용하고, 자식 클래스만의 속성(`self.bed`)을 추가로 확장합니다.

---

### 1.2 되새김 문제 1: 부모 기능 확장 (UpgradeCalculator)

```python
class Calculator:
  def __init__(self):
    self.value = 0

  def add(self, val):
    self.value += val

class UpgradeCalculator(Calculator):
  def __init__(self):
    super().__init__()

  def minus(self, val):
    self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)  # 출력: 3
```

- **설명**:
  - 부모 `Calculator`의 `add` 기능은 그대로 유지하면서 새로운 메서드인 `minus`를 자식 클래스에 추가하여 기능을 확장했습니다.

---

### 1.3 되새김 문제 2: 메서드 오버라이딩 (MaxLimitCalcurator)

```python
class MaxLimitCalcurator(Calculator):
  MAX_LIMIT = 100

  def __init__(self):
    super().__init__()

  # 부모의 add 메서드를 재정의 (메서드 오버라이딩)
  def add(self, val):
    super().add(val)
    if (self.value > self.MAX_LIMIT):
      self.value = 100

cal = MaxLimitCalcurator()
cal.add(50)
cal.add(60)
print(cal.value)  # 출력: 100 (110이 아닌 최댓값 100으로 제한)
```

- **설명**:
  - **메서드 오버라이딩(Method Overriding)**: 부모 클래스에 이미 정의된 메서드를 자식 클래스에서 동일한 이름으로 다시 작성하여 동작 방식을 덮어씌우거나 확장하는 기법입니다.
  - `super().add(val)`로 기본 덧셈을 수행한 후, 클래스 상수 `MAX_LIMIT`을 초과할 경우 100으로 고정하는 방어 로직을 적용했습니다.

---

### 1.4 되새김 문제 6: map과 람다 활용

```python
a = list(map(lambda i: i * 3, [1, 2, 3, 4]))
print(a)  # [3, 6, 9, 12]
```

- **설명**:
  - `map()` 함수와 `lambda` 표현식을 조합하여 리스트의 각 원소를 3배 곱한 새 리스트를 생성합니다.

---

### 1.5 클래스 변수 카운터와 `__dict__` 네임스페이스

```python
class Container:
  stock_num = 0  # 클래스 변수 (모든 인스턴스가 공유)

  def __init__(self, name):
    self.name = name
    Container.stock_num += 1  # 인스턴스 생성 시마다 클래스 변수 증가

c = Container('Lee')
c2 = Container('Kim')

print(Container.stock_num)  # 출력: 2
print(c.name)               # Lee
print(c2.name)              # Kim
print(c.__dict__)           # {'name': 'Lee'}
print(c2.__dict__)          # {'name': 'Kim'}
```

- **설명**:
  - `Container.stock_num`과 같이 클래스 이름을 통해 접근하여 수정하면 모든 인스턴스에서 누적 카운트가 공유됩니다.
  - `인스턴스.__dict__`는 해당 인스턴스가 독립적으로 보유하고 있는 인스턴스 네임스페이스(변수와 값의 매핑)를 딕셔너리로 보여줍니다. `stock_num`은 인스턴스의 `__dict__`에 없고 클래스에만 존재함을 확인할 수 있습니다.
