# [Day 7 - Session 4] 무한 제너레이터 vs 이터레이터 클래스, 권한 검사 데코레이터, JSON 직렬화/역직렬화

- **실습 파일**: `session4.py`
- **주요 내용**:
  - 기본 제너레이터 함수 및 `yield` 동작
  - 무한 짝수 생성기: 제너레이터 함수(`while True` + `yield`) vs 이터레이터 클래스(`__iter__` / `__next__`) 비교
  - 상태 검증 데코레이터(`@login`)를 활용한 접근 제어 (로그인 상태에 따른 얼리 리턴)
  - `json` 모듈을 이용한 데이터 직렬화(`json.dump`) 및 역직렬화(`json.load`)
  - `ensure_ascii=False` 및 `indent` 옵션을 통한 한글 보존과 가독성 확보

---

## 1. 실습 코드 및 단계별 해설

### 1.1 무한 짝수 생성: 제너레이터 함수 vs 이터레이터 클래스

#### 방식 A: 제너레이터 함수 (권장)
```python
def even_gen():
  num = 0
  while True:
    yield num
    num += 2

g = even_gen()
print(next(g))  # 0
print(next(g))  # 2
print(next(g))  # 4
print(next(g))  # 6
```

#### 방식 B: 이터레이터 클래스
```python
class even_gen:
  def __init__(self):
    self.current = 0

  def __iter__(self):
    return self

  def __next__(self):
    result = self.current
    self.current += 2
    return result
```

- **설명**:
  - `while True` 무한 루프라도 `yield`를 만나면 연산을 일시 중단하고 호출자에게 제어권을 넘깁니다. 메모리에 무한한 수열을 저장하지 않고 필요할 때마다 1개씩 지연 계산(Lazy Evaluation)합니다.
  - 클래스 방식에 비해 제너레이터 함수 방식이 코드가 훨씬 간결하고 가독성이 뛰어납니다.

---

### 1.2 권한 검사 데코레이터 (`@login`)

```python
login_state = False

def login(func):
  def wrapper():
    # 얼리 리턴: 비로그인 시 즉시 함수 실행 중단
    if not login_state:
      print('로그인')
      return
    return func()
  return wrapper

@login
def write_post():
  print('글 작성 완료')

write_post()  # 출력: '로그인' (비로그인 상태이므로 글 작성 함수 미실행)

login_state = True
write_post()  # 출력: '글 작성 완료' (로그인 상태이므로 원본 함수 정상 실행)
```

- **설명**:
  - 데코레이터를 이용하면 본래 기능(`write_post`)의 내부 코드를 수정하지 않고도 권한 검사나 유효성 확인 로직을 횡단 관심사(Cross-cutting Concern)로 분리할 수 있습니다.
  - 로그인 상태가 거짓(`False`)이면 얼리 리턴(Early Return)하여 본 함수 실행을 사전에 차단합니다.

---

### 1.3 JSON 파일 읽기/쓰기 (`json.dump` / `json.load`)

```python
import json

# JSON 파일 읽기 (역직렬화)
def loading():
  try:
    with open('myinfo.json', 'r', encoding='UTF-8') as f:
      return json.load(f)
  except FileNotFoundError:
    print('no file')

# JSON 파일 저장 (직렬화)
def add(data):
  with open('C:/AX Academy/study/Python/Day 7/stu.json', 'w', encoding='UTF-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

data = [
  { 'name': 'Tom', 'score': 100 },
  { 'name': 'Juli', 'score': 80 }
]

add(data)
print('저장')
```

- **주요 옵션 및 메서드 설명**:
  - `json.dump(obj, fp)`: 파이썬 객체(리스트, 딕셔너리 등)를 JSON 포맷 텍스트로 직렬화하여 파일에 기록합니다.
  - `json.load(fp)`: JSON 형식의 파일 내용을 파이썬 데이터 타입(dict, list 등)으로 역직렬화하여 읽어옵니다.
  - `ensure_ascii=False`: 한글 등의 비아스키(Non-ASCII) 문자가 `\uXXXX` 유니코드 이스케이프 형태로 변환되지 않고 한글 그대로 저장되도록 보장합니다.
  - `indent=2`: 사람이 읽기 쉽도록 2칸 들여쓰기 서식을 적용(Pretty Print)합니다.
