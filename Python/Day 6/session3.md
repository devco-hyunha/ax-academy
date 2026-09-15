# [Day 6 - Session 3] 가변 인자 연산 함수 및 사용자 입력 예외 처리 실습

- **실습 파일**: `session3.py`
- **주요 내용**:
  - 가변 인자(`*args`)와 문자열 연산자 분기를 활용한 계산기 함수 `calc()`
  - 미지원 연산자 전달 시 `ValueError` 발생 및 내부 예외 복구
  - 사용자 나이 입력 유효성 검사 및 복합 예외 처리 (`ValueError`, `AgeError`)

---

## 1. 실습 코드 및 단계별 해설

### 1.1 가변 인자 계산기 함수 (`calc`)

```python
def calc(oper, *args):
  try:
    if oper == 'add':
      print(sum(args))
      return sum(args)
    elif oper == 'mul':
      result = 1
      for x in args:
        result *= x
      print(result)
      return result
    elif oper == 'avg':
      avg_val = sum(args) / len(args)
      print(avg_val)
      return avg_val
    else:
      raise ValueError('잘못된 연산입니다')
  except ValueError as e:
    print(e)
    return None

calc("add", 1, 2, 3)        # 출력: 6
calc("mul", 1, 2, 3, 4)     # 출력: 24
calc("avg", 10, 20, 30)     # 출력: 20.0
calc("sub", 10, 5)          # 출력: 잘못된 연산입니다 -> None 반환
```

- **설명**:
  - `*args`로 개수가 정해지지 않은 복수의 숫자 인자를 튜플 형태로 수신합니다.
  - 지원하지 않는 연산자(`oper`)가 입력되면 `raise ValueError('잘못된 연산입니다')`를 통해 명시적으로 오류를 발생시킵니다.
  - 발생한 `ValueError`를 내부의 `except` 블록에서 잡아 에러 메시지를 출력하고 `None`을 반환하여 프로그램이 중단되지 않고 안전하게 처리됩니다.

---

### 1.2 사용자 나이 입력 유효성 검사 및 예외 처리

```python
# 사용자 정의 예외 클래스
class AgeError(Exception):
  def __str__(self):
    return "나이는 0보다 작을수 없습니다"

try:
  age = int(input('나이를 입력하세요: '))
  if age < 0:
    raise AgeError()
  print('입력 완료')
except ValueError as e:
  # 숫자로 변환할 수 없는 문자열을 입력했을 때
  print('숫자만 입력해야 합니다')
except AgeError as e:
  # 0 미만의 음수 숫자를 입력했을 때
  print(e)
```

- **입력 시나리오별 처리 흐름**:
  1. **정상 입력 (`age = 25`)**:
     - `int()` 변환 성공, `age < 0` 조건 통과 → `"입력 완료"` 출력.
  2. **문자열 입력 (`age = "스물다섯"`)**:
     - `int()` 함수에서 내장 `ValueError` 발생 → `except ValueError` 블록 실행 (`"숫자만 입력해야 합니다"` 출력).
  3. **음수 입력 (`age = -5`)**:
     - `int()` 변환은 성공하지만 `age < 0` 조건에 의해 `raise AgeError()` 실행 → `except AgeError` 블록 실행 (`"나이는 0보다 작을수 없습니다"` 출력).
- **의의**:
  - 서로 다른 원인의 에러(데이터 형식 오류 vs 도메인 비즈니스 규칙 위반)를 개별 `except` 블록으로 분리하여 사용자에게 정확한 피드백을 제공합니다.
