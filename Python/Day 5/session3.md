# [Day 5 - Session 3] 내장 함수, 표준 라이브러리(time, random, pickle, webbrowser) 및 `__name__ == "__main__"`

- **실습 파일**: `session3.py`
- **주요 내용**:
  - 유용한 내장 함수(`sorted`, `sum`, `map`) 복습
  - 시간 처리 표준 라이브러리: `time`
  - 난수 생성 표준 라이브러리: `random`
  - 객체 직렬화/역직렬화 표준 라이브러리: `pickle`
  - 웹 제어 라이브러리: `webbrowser`
  - 파이썬 모듈 시스템과 `if __name__ == "__main__":` 실행 제어 원리

---

## 1. 실습 코드 및 단계별 해설

### 1.1 내장 함수: sorted, sum, map

```python
# map + lambda: 부호 반전
print(list(map(lambda x: -x, range(0, 10))))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

# sorted: 원본을 변경하지 않고 정렬된 새로운 리스트 반환
a = sorted([5, 6, 2, 1, 2, 4])
print(a)  # [1, 2, 2, 4, 5, 6]

# sum: 시퀀스의 모든 원소 합계
print(sum([1, 2, 3, 4, 5]))   # 15
print(sum(range(1, 101)))      # 5050 (1부터 100까지의 합)
```

- **설명**:
  - `list.sort()`는 원본 리스트를 제자리(in-place) 정렬하고 `None`을 반환하는 반면, `sorted()`는 정렬된 새 리스트를 생성하여 반환합니다.

---

### 1.2 표준 라이브러리: time 모듈

```python
import time

# 1970년 1월 1일 0시 0분 0초(UTC)를 기준으로 경과한 초(Epoch Time) 반환
print(time.time())

# 초 단위 시간을 현지 시간 구조체(struct_time)로 변환
print(time.localtime(time.time()))

# 포맷 문자열을 사용하여 읽기 쉬운 형태의 날짜/시간 문자열로 변환
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# 예: '2026-09-11 18:20:00'
```

- **주요 서식 지시자**:
  - `%Y`: 4자리 연도, `%m`: 2자리 월, `%d`: 2자리 일
  - `%H`: 24시간 형식 시, `%M`: 분, `%S`: 초

---

### 1.3 표준 라이브러리: random 모듈

```python
import random

# 0.0 이상 1.0 미만의 부동소수점 실수(float) 반환
print(random.random())

# a 이상 b 이하의 정수(int) 난수 반환 (a, b 모두 포함)
print(random.randint(1, 10))
```

---

### 1.4 표준 라이브러리: pickle 모듈 (객체 영속화/직렬화)

```python
import pickle

obj = {1: 'python', 2: 'study', 3: 'basic'}

# 1) 바이너리 쓰기 모드('wb')로 직렬화(dump)하여 파일 저장
with open('test.obj', 'wb') as f:
  pickle.dump(obj, f)

# 2) 바이너리 읽기 모드('rb')로 역직렬화(load)하여 원본 객체 복원
with open('test.obj', 'rb') as f:
  data = pickle.load(f)
  print(data)  # {1: 'python', 2: 'study', 3: 'basic'}
```

- **설명**:
  - **직렬화(Serialization)**: 파이썬의 복합 객체(딕셔너리, 리스트, 클래스 인스턴스 등)를 바이트 스트림으로 변환하여 파일이나 네트워크로 전송/저장하는 과정입니다.
  - 반드시 바이너리 모드(`'wb'`, `'rb'`)로 열어야 합니다.
  - `pickle.dump(data, file)`: 객체를 파일에 기록
  - `pickle.load(file)`: 파일에서 객체를 읽어 원본 형태로 복원

---

### 1.5 모듈과 `if __name__ == "__main__":` 동작 원리

```python
def add(x, y): return x + y
def sub(x, y): return x - y
def multi(x, y): return x * y
def div(x, y): return x / y

# 엔트리 포인트 분기
if __name__ == "__main__":
  # 직접 실행(Direct execution)할 때만 동작하는 테스트/메인 코드
  print(add(10, 20))
```

- **원리 및 중요성**:
  1. 파이썬 인터프리터는 파일을 읽어 실행할 때 내장 특수 변수인 `__name__`을 자동으로 설정합니다.
  2. 터미널에서 `python 파일명.py`로 **직접 실행**한 파일의 `__name__` 값은 `"__main__"`이 됩니다.
  3. 다른 파일에서 `import 파일명` 형태로 **모듈로서 가져올 때**의 `__name__` 값은 **해당 파일의 이름(모듈명)**이 됩니다.
  4. 따라서 `if __name__ == "__main__":` 블록을 사용하면, 해당 파일을 직접 실행할 때만 테스트 코드나 메인 로직이 실행되고, 다른 파일에서 import할 때는 불필요한 코드가 실행되지 않고 함수/클래스 정의만 깔끔하게 불러올 수 있습니다.
