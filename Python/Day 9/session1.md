# [Day 9 - Session 1] 가변 인자(*args) 및 사용자 정의 예외(Exception) 클래스

- **실습 파일**: `session1.py`
- **주요 내용**:
  - 위치 가변 인자(`*args`)를 활용한 유연한 함수 매개변수 처리
  - 내장 `Exception` 클래스 상속을 통한 커스텀(사용자 정의) 예외 설계
  - `raise` 키워드를 활용한 비즈니스 로직 조건부 예외 발생
  - `try-except` 블록을 활용한 다중 예외 처리 및 에러 메시지 캡처(`as e`)

---

## 1. 실습 코드 및 단계별 해설

### 1.1 위치 가변 인자 (`*args`)

```python
# 가변 인자: 전달받는 인자의 개수가 정해지지 않았을 때 사용
def find_max(*args):
    # 인자가 하나도 전달되지 않은 경우(빈 튜플) None 반환
    if not args:
        return None
    return max(args)

print(find_max(3, 8, 2))  # 8
print(find_max())         # None
```

- **설명**:
  - `*args`: 함수 호출 시 전달되는 임의 개수의 위치 인자들을 **튜플(tuple)** 형태로 패킹(packing)하여 받습니다.
  - `if not args:`: 빈 튜플은 불리언 컨텍스트에서 `False`로 평가되므로, 인자가 전달되지 않은 경우를 안전하게 조기 반환(Early Return) 처리하여 내장 `max()` 함수의 빈 시퀀스 에러(`ValueError`)를 방지합니다.

---

### 1.2 사용자 정의 예외 클래스 설계

```python
# 구매할 수량(qty)이 재고보다 많을 때 발생시킬 예외
class OutofCtockError(Exception):
    pass

# 수량(qty)이 0 이하일 때 발생시킬 예외
class InvalidError(Exception):
    pass
```

- **설명**:
  - 파이썬의 표준 최상위 예외 클래스인 `Exception`을 상속받아 고유한 의미를 갖는 사용자 정의 예외를 정의합니다.
  - 내장 표준 예외(예: `ValueError`, `RuntimeError`) 대신 도메인 특화 예외를 사용하면 코드의 가독성이 높아지고, 상위 호출부에서 예외의 원인을 명확하게 분기 처리할 수 있습니다.

---

### 1.3 `raise`를 통한 비즈니스 로직 검증 및 예외 처리

```python
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def sell(self, qty):
        # 1. 수량 유효성 검증: 0 이하의 수량은 잘못된 입력
        if qty < 0:
            raise InvalidError('수량을 잘못 입력')
        
        # 2. 재고 수량 검증: 재고 초과 판매 불가
        if qty > self.stock:
            raise OutofCtockError('재고 부족')
        
        # 정상 판매 시 재고 차감
        self.stock -= qty
        print(f'{self.name} {qty}개 판매')


# 정상 케이스 동작
product = Product('노트북', 5)
product.sell(2)
print(product.stock)  # 3

# 예외 발생 및 처리 케이스
try:
    product.sell(10)  # 재고(3)보다 많은 10개 판매 시도 -> OutofCtockError 발생
except OutofCtockError as e:
    print(e)          # 출력: 재고 부족
except InvalidError as e:
    print(e)
```

- **동작 흐름**:
  1. `product.sell(2)` 호출 시 `qty(2) <= stock(5)`이므로 정상 차감되어 재고는 `3`이 됩니다.
  2. `product.sell(10)` 호출 시 `10 > 3` 조건을 만족하여 `raise OutofCtockError('재고 부족')`이 실행됩니다.
  3. `try` 블록 내에서 발생한 예외는 즉시 일치하는 `except OutofCtockError as e:` 블록으로 이동하여 `'재고 부족'` 메시지를 출력하고, 비정상 종료(Crash) 없이 안전하게 복구됩니다.

---

## 2. 핵심 요약

| 개념 | 문법 / 키워드 | 핵심 역할 |
| :--- | :--- | :--- |
| **위치 가변 인자** | `*args` | 0개 이상의 위치 인자를 하나의 튜플로 묶어서 전달받음 |
| **사용자 정의 예외** | `class MyError(Exception):` | 도메인 로직에 특화된 오류 식별자 정의 |
| **예외 발생** | `raise ExceptionClass("메시지")` | 특정 조건 위반 시 실행 흐름을 중단하고 예외를 호출자에게 전달 |
| **세부 예외 포착** | `except SpecificError as e:` | 구체적인 예외 유형별로 맞춤형 예외 처리 로직 수행 |
