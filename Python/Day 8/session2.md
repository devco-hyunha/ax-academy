# [Day 8 - Session 2] 반복문을 활용한 다중 스레드 관리와 동기화

- **실습 파일**: `session2.py`
- **주요 내용**:
  - 반복문(`for`)을 활용한 다중 스레드 동적 생성 및 실행
  - 스레드 풀 수집 패턴: 리스트를 활용한 스레드 인스턴스 보관
  - 일괄 동기화: 순회하며 `join()` 호출을 통한 전체 작업 대기
  - 스레드 스케줄링의 비결정성(Non-deterministic Execution) 이해
  - 스레드 안전성(Thread Safety)과 동기화 기법 개요

---

## 1. 실습 코드 및 단계별 해설

### 1.1 다중 스레드 생성, 실행 및 동기화

```python
import threading
import time

def game(name):
    print(f'{name} start')
    time.sleep(2)
    print(f'{name} end')

names = ['t1', 't2', 't3', 't4', 't5']

threads = []
# 1. 반복문 안에서 스레드 생성 및 시작
for name in names:
    t = threading.Thread(target=game, args=(name,))
    threads.append(t)
    t.start()  # 백그라운드 스레드 즉시 실행

# 2. 모든 스레드의 종료를 순차적으로 대기
for t in threads:
    t.join()   # 해당 스레드가 끝날 때까지 메인 스레드 블로킹

# 3. 모든 스레드가 종료된 후 최종 완료 처리
print('all done')
```

---

## 2. 세부 동작 원리 및 핵심 포인트

### 2.1 튜플 인자 전달 주의점 (`args=(name,)`)
- `threading.Thread`의 `args` 매개변수는 반드시 **이터러블(주로 튜플)**이어야 합니다.
- 원소가 하나뿐인 튜플을 만들 때는 반드시 쉼표를 붙여 `(name,)` 형태로 작성해야 합니다.
  - `(name)`은 단순 괄호로 둘러싸인 문자열이 되어, 각 글자(`'t'`, `'1'`)가 개별 인자로 풀려 들어가 에러(`TypeError`)가 발생합니다.

### 2.2 생성/실행 루프와 `join` 루프의 분리
- **올바른 패턴 (병렬/동시 실행)**:
  ```python
  for name in names:
      t.start()  # 모두 먼저 시작시켜 동시에 실행
  for t in threads:
      t.join()   # 이후에 한꺼번에 대기
  ```
- **흔히 하는 안티 패턴 (직렬 순차 실행)**:
  ```python
  for name in names:
      t = threading.Thread(...)
      t.start()
      t.join()  # 하나 시작하고 끝날 때까지 기다리므로 멀티스레드의 의미가 상실됨 (단일 스레드처럼 순차 실행됨)
  ```

### 2.3 실행 순서의 비결정성 (Non-determinism)
- 코드는 `t1, t2, t3, t4, t5` 순서로 `start()`를 호출하지만, 출력되는 순서는 실행할 때마다 달라질 수 있습니다.
- 스레드의 CPU 할당과 컨텍스트 스위칭 타이밍은 운영체제(OS)의 **스레드 스케줄러**가 결정하므로, `start()` 순서가 곧 실행/종료 순서를 보장하지 않습니다.

---

## 3. 실무 지식 확장: 스레드 안전성과 락(Lock)

여러 스레드가 동일한 자원(전역 변수, 파일, 리스트 등)을 동시에 읽고 쓸 때 데이터 불일치가 일어나는 현상을 **경쟁 상태(Race Condition)**라고 합니다.

```python
# 공유 자원 동기화 예시 (threading.Lock)
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    with lock:  # 임계 영역(Critical Section) 보호
        counter += 1
```

- 안전한 멀티스레딩을 위해서는 `threading.Lock`을 사용하거나, 파이썬 표준 라이브러리의 `queue.Queue`처럼 스레드 안전(Thread-safe)한 자료구조를 활용하는 것이 권장됩니다.
