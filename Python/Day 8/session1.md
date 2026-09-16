# [Day 8 - Session 1] 비동기 프로그래밍(asyncio)과 멀티스레딩(threading) 기초

- **실습 파일**: `session1.py`
- **주요 내용**:
  - 파이썬 비동기 프로그래밍 기초: `async def`, `await`, `asyncio.sleep`, `asyncio.run()`
  - 복수 코루틴 동시 실행: `asyncio.gather()`
  - 멀티스레딩 기본 사용법: `threading.Thread`, `start()`, `join()`
  - 동시성(Concurrency) vs 병렬성(Parallelism), GIL(Global Interpreter Lock)
  - 비동기(코루틴)와 멀티스레드의 동작 원리 및 장단점 비교

---

## 1. 실습 코드 및 단계별 해설

### 1.1 비동기 프로그래밍 (`asyncio`) 기초

```python
import asyncio

# 1. 코루틴 함수 정의 (비동기 함수)
async def show(text, sec):
    print('start')
    await asyncio.sleep(sec)  # I/O 논블로킹 대기 (제어권을 이벤트 루프에 양보)
    print(f'{text} end')

# 단일 코루틴 실행: 이벤트 루프를 생성하고 코루틴이 완료될 때까지 실행 후 루프를 닫음
asyncio.run(show('Hello, World!', 3))
```

- **설명**:
  - `async def`: 일반 함수가 아닌 **코루틴(Coroutine)** 객체를 반환하는 비동기 함수를 선언합니다.
  - `await`: 비동기 작업이 완료될 때까지 기다립니다. 단, 스레드를 멈추는(Blocking) 것이 아니라 제어권을 이벤트 루프(Event Loop)에 반환하여 다른 코루틴이 작업할 수 있도록 양보(Non-blocking)합니다.
  - `asyncio.run()`: 파이썬 3.7+ 표준 진입점 함수로, 새 이벤트 루프를 생성하여 최상위 코루틴을 실행하고 완료 후 루프를 종료합니다.

---

### 1.2 `asyncio.gather()`를 활용한 복수 코루틴 동시 실행

```python
async def main():
    # 비동기 함수들을 묶어서 동시(Concurrent)에 실행
    await asyncio.gather(
        show('Hello,', 2),
        show('World!', 1)
    )

asyncio.run(main())
```

- **동작 흐름**:
  1. `show('Hello,', 2)` 시작 → `'start'` 출력 → 2초 대기 요청 (제어권 양보)
  2. 제어권이 이벤트 루프로 넘어가 `show('World!', 1)` 시작 → `'start'` 출력 → 1초 대기 요청
  3. 1초 경과 후 `show('World!', 1)` 재개 → `'World! end'` 출력 및 완료
  4. 2초 경과 후 `show('Hello,', 2)` 재개 → `'Hello, end'` 출력 및 완료
  5. 순차 실행 시 3초가 걸릴 작업이 **약 2초**만에 완료됩니다.

---

### 1.3 멀티스레딩 (`threading`) 기초

```python
import threading
import time

def download(name, sec):
    print(f'{name} start')
    time.sleep(sec)  # 블로킹 방식의 지연 (해당 스레드 일시 중단)
    print(f'{name} end, {sec} delay')

# 스레드 객체 생성
t1 = threading.Thread(target=download, args=('t1', 2))
t2 = threading.Thread(target=download, args=('t2', 3))

# 스레드 실행 시작
t1.start()
t2.start()

# 메인 스레드가 각 작업 스레드의 종료를 대기
t1.join()
t2.join()

print('all done')
```

- **설명**:
  - `threading.Thread(target=..., args=(...))`: 별도의 OS 스레드에서 실행할 함수와 인자를 지정합니다. (`args`는 반드시 튜플이어야 함)
  - `start()`: 신규 스레드를 활성화하고 내부적으로 `run()` 메서드를 호출합니다. 메인 스레드는 블로킹되지 않고 즉시 다음 코드로 넘어갑니다.
  - `join()`: 메인 스레드가 해당 스레드가 완전히 종료될 때까지 대기(동기화)하도록 만듭니다. `join()`을 호출하지 않으면 작업 완료 전에 `all done`이 먼저 출력될 수 있습니다.

---

## 2. 핵심 개념 심화: 비동기(Async) vs 멀티스레드(Thread)

### 2.1 주요 차이점 비교

| 비교 항목 | 멀티스레딩 (`threading`) | 비동기 프로그래밍 (`asyncio`) |
| :--- | :--- | :--- |
| **작업 단위** | 스레드 (OS 스레드) | 코루틴 (단일 스레드 내 가벼운 태스크) |
| **동작 주체** | OS 커널 스케줄러가 스레드 전환 (선점형) | 이벤트 루프가 협력적으로 전환 (협력형, `await`) |
| **컨텍스트 스위칭 비용** | 큼 (레지스터, 스택 저장 등 오버헤드) | 매우 작음 (단순 함수 프레임 전환 수준) |
| **메모리 사용량** | 스레드당 수 MB의 독립 스택 할당 | 코루틴당 수 KB 이하 |
| **동기화 문제 (동시성 버그)** | 경쟁 상태(Race Condition), 데드락 위험 큼 | 공유 메모리에 동시 쓰기가 없으므로 락 문제 비교적 적음 |
| **적합한 작업** | 레거시 블로킹 I/O 처리, 복수 작업 분기 | 대규모 네트워크 I/O, 웹소켓, API 요청 처리 |

### 2.2 파이썬의 GIL (Global Interpreter Lock)

- 파이썬(CPython) 인터프리터에는 **GIL(글로벌 인터프리터 락)**이 존재하여 **하나의 프로세스 내에서는 한 번에 단 하나의 스레드만 파이썬 바이트코드를 실행**할 수 있습니다.
- 따라서 **CPU 바운드 작업**(대규모 연산, 이미지 처리 등)에는 멀티스레딩이 성능 향상을 가져오지 못하며, 멀티프로세싱(`multiprocessing`) 모듈을 사용해야 합니다.
- 반면 파일 입출력, 네트워크 요청, `time.sleep()`과 같은 **I/O 바운드 작업**은 시스템 콜 대기 중 GIL이 자동으로 해제되므로 멀티스레딩과 비동기 프로그래밍 모두 효율적인 처리가 가능합니다.

---

## 3. 실행 결과 비교 요약

```text
# 1. asyncio.run(show('Hello, World!', 3)) 실행
start
Hello, World! end

# 2. asyncio.gather() 동시 실행 (약 2초 소요)
start
start
World! end
Hello, end

# 3. threading 동시 실행 (약 3초 소요)
t1 start
t2 start
t1 end, 2 delay
t2 end, 3 delay
all done
```
