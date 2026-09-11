# [Day 5 - Session 1] 클래스 심화: 인스턴스 메서드, 게터/세터, 객체 간 협력

- **실습 파일**: `session1.py`
- **주요 내용**:
  - 클래스 선언과 초기화(`__init__`)
  - 인스턴스 메서드 구현 및 문자열 포맷팅(`.format()`)
  - 학생 객체(`Student`)와 게터/세터(Getter/Setter) 패턴
  - 집계/관리 클래스(`Cal`)를 활용한 객체 간 협력 모델

---

## 1. 실습 코드 및 단계별 해설

### 1.1 Fruit 클래스: 클래스 변수와 인스턴스 메서드

```python
class Fruit:
  price = 20000
  def __init__(self, title, color):
    self.title = title
    self.color = color

  def info(self):
    return "{}과일은 {}색".format(self.title, self.color)

  def buy1(self, buy1):
    return "{}과일은 {}에서 사야지".format(self.title, buy1)


f = Fruit('apple', 'red')

print(f.info())
print(f.buy1('lotte'))
```

- **설명**:
  - `Fruit` 클래스는 인스턴스 생성 시 `title`과 `color`를 인스턴스 변수로 저장합니다.
  - `price = 20000`은 클래스 변수로 모든 인스턴스가 공통으로 공유합니다.
  - `info()`와 `buy1()` 메서드는 인스턴스 내부의 `self.title`, `self.color` 및 매개변수로 전달된 인자를 활용해 포맷된 문자열을 반환합니다.

---

### 1.2 Student 클래스: 데이터 은닉 및 게터/세터 패턴

```python
class Student():
  def __init__(self, id, name, score = 0):
    self.id = id
    self.name = name
    self.score = score

  def get(self):
    return {
      "id": self.id,
      "name": self.name,
      "score": self.score
    }
  def getId(self): return self.id
  def getName(self): return self.name
  def getScore(self): return self.score
  def setScore(self, score): self.score = score
```

- **설명**:
  - 기본값 매개변수(`score = 0`)를 사용하여 성적을 입력하지 않고도 학생 객체를 생성할 수 있습니다.
  - `getId()`, `getName()`, `getScore()` 메서드로 인스턴스 필드에 접근하며, `setScore()` 메서드로 점수를 수정할 수 있는 게터/세터 구조를 갖추고 있습니다.
  - `get()` 메서드는 객체의 전체 상태를 딕셔너리 형태로 직렬화하여 반환합니다.

---

### 1.3 Cal 클래스: 객체 컬렉션 관리와 통계 연산 (객체 협력)

```python
class Cal:
  def __init__(self):
    self.stu = list()

  def add(self, student):
    self.stu.append(student)

  def avg(self):
    sum = 0
    for student in self.stu:
      sum += student.getScore()
    count = len(self.stu)
    avg = sum / count
    return avg, count

cal1 = Cal()
user1 = Student(1, '찬웅')

user1.setScore(100)
user2 = Student(2, '예진', 90)
user3 = Student(3, '우정', 80)
user4 = Student(4, '소영', 80)

print(user1.getName())

cal1.add(user1)
cal1.add(user2)
cal1.add(user3)
cal1.add(user4)
avg, count = cal1.avg()

print('평균: {}'.format(avg))
```

- **설명**:
  - `Cal` 클래스는 내부적으로 `self.stu` 리스트를 유지하며 `Student` 객체들을 원소로 보관합니다.
  - `add()` 메서드를 통해 `Student` 객체를 리스트에 추가합니다.
  - `avg()` 메서드는 순회하며 각 학생의 `getScore()`를 호출하여 합산하고, 평균 점수와 전체 학생 수를 튜플 `(avg, count)` 형태로 언패킹 반환합니다.
  - **객체 지향적 설계**: 하나의 클래스가 모든 책임을 갖는 것이 아니라, 학생 정보 관리는 `Student`가, 학생들의 모음 및 통계 계산은 `Cal`이 담당하도록 역할을 분리(책임 분리)하였습니다.
