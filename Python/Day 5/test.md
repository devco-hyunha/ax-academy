# [Day 5 - Test & 되새김 문제] 모듈 임포트, 내장/표준 라이브러리 응용, 은행 계좌 클래스

- **실습 파일**: `test/test.py`, `test/test2.py`, `test/test3.py`
- **주요 내용**:
  - 사용자 정의 모듈 생성 및 임포트 방식(`import test`, `from test import *`)
  - 점프 투 파이썬 5장 되새김 문제 풀이 (Q3, Q4, Q7, Q8, Q11, Q12, Q17)
  - 로또 번호 비복원 추출 알고리즘 (`random.randint` + `pop`)
  - 무작위 청소/당번 매칭 알고리즘 (`random.shuffle`, `zip`, `enumerate`)
  - 객체지향 캡슐화 실습: 은행 계좌(`Account`) 클래스

---

## 1. 실습 코드 및 단계별 해설

### 1.1 모듈 생성과 임포트 (`test/test.py` & `test/test2.py`)

```python
# test/test.py
def add(x, y): return x + y
def sub(x, y): return x - y
def multi(x, y): return x * y
def div(x, y): return x / y

if __name__ == "__main__":
  # 직접 실행 시만 구동되는 테스트 블록
  pass
```

```python
# test/test2.py에서 불러오기
# 방식 1: 모듈 전체를 네임스페이스로 import
import test
print(test.add(1, 2))  # 3

# 방식 2: 모듈의 함수를 직접 import
from test import *
print(add(1, 2))       # 3
```

---

### 1.2 되새김 문제 핵심 풀이 (`test/test2.py`)

#### Q3. 내장 함수 진위 판별 (`all`, `chr`, `ord`)
```python
all([1, 2, abs(-3) - 3])
# abs(-3) - 3 = 3 - 3 = 0 (False)
# 0이 포함되어 있으므로 결과는 False

chr(ord('a')) == 'a'
# ord('a')는 아스키코드 97, chr(97)은 'a'이므로 True
```

#### Q4. filter와 람다를 활용한 양수 추출
```python
numbers = [1, -2, 3, -5, 8, -3]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)  # [1, 3, 8]
```

#### Q7 & Q8. 최댓값/최솟값 합산 및 반올림
```python
# Q7: 최소값 + 최대값
a = [-8, 2, 7, 5, -3, 5, 0, 1]
b = min(a) + max(a)  # -8 + 7 = -1

# Q8: 소수점 4자리까지 반올림
print(round(17 / 3, 4))  # 5.6667
```

#### Q11. time 모듈로 날짜/시간 포맷 출력
```python
import time
now = time.localtime(time.time())
formatTime = time.strftime('%Y/%m/%d %H:%M:%S', now)
print(formatTime)  # 예: '2026/09/11 18:20:00'
```

#### Q12. 로또 번호 6개 추첨 알고리즘 (비복원 추출)
```python
import random

ball = list(range(1, 46))  # 1 ~ 45
loop = list(range(6))      # 6번 반복

lotto = list(
  map(
    lambda i: ball.pop(random.randint(0, len(ball) - 1)),
    loop
  )
)
print(lotto)
```
- **해설**: 원본 공 리스트(`ball`)에서 무작위 인덱스를 뽑아 `pop()`으로 꺼내어 제거하므로, 중복 없는 번호 6개가 정확하게 추출됩니다.

#### Q17. 당번 무작위 배정 및 예외 인원 처리
```python
people = ['김승현', '김진호', '강춘자', '이예준', '김현주']
work = ['청소', '빨래', '설거지']
etc = '휴식'

random.shuffle(people)  # 사람 명단을 무작위로 섞음

# 당번 항목 수보다 사람이 많으면 남은 사람 수만큼 '휴식' 추가
for i, p in enumerate(people):
  if len(work) == i:
    work.append(etc)

# 두 리스트를 1:1로 결합
paired = list(zip(people, work))
print(paired)
```

---

### 1.3 은행 계좌 Account 클래스 (`test/test3.py`)

```python
class Account:
  def __init__(self, name, money):
    self.name = name
    self.money = money

  def deposit(self, money):
    self.money += money

  def withdraw(self, money):
    # 잔액 부족 검증: 얼리 리턴(Early Return) 적용
    if self.money < money:
      print('잔액이 부족합니다')
      return
    self.money -= money

  def show_balance(self):
    print(f"{self.name}님의 현재 잔액 {self.money}원")

# 실행 테스트
acc1 = Account("홍길동", 10000)
acc1.show_balance()  # 홍길동님의 현재 잔액 10000원
acc1.deposit(5000)   # +5000원 -> 15000원
acc1.withdraw(3000)  # -3000원 -> 12000원
acc1.withdraw(20000) # 잔액이 부족합니다 (출금 거부)
acc1.show_balance()  # 홍길동님의 현재 잔액 12000원
```

- **설명**:
  - `deposit()`: 계좌 잔액 증가
  - `withdraw()`: 출금 희망액이 보유 잔액보다 클 경우 안내 메시지를 출력하고 조기 반환(`return`)하여 안전한 잔액 보호
  - `show_balance()`: f-string을 활용한 현재 잔액 출력
