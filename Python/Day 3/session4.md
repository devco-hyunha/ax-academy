# [Day 3 - Session 4] 사용자 입출력(input, print) 및 형 변환 기초

- **실습 파일**: `session4.py`
- **주요 내용**: 
  - `input()` 함수의 동작 방식과 반환 자료형(`str`) 특성
  - `input()` 입력값의 산술 연산을 위한 명시적 형 변환(`int()`, `float()`)
  - `print()` 함수의 출력 기법 (문자열 리터럴 결합, 쉼표 구분 공백, `end` 인자 제어)
  - `format()`과 f-string을 활용한 동적 입력값 포매팅
  - 가변 인자(`*args`)를 활용한 실시간 평균 계산 함수

---

## 1. 실습 코드 및 단계별 해설

### 1.1 `input()` 함수의 기본 동작 및 반환 타입

```python
# 사용자 입출력
# num = input('숫자를 입력하세요 : ')
# print(num)
# print(type(num)) # <class 'str'>
```

- **설명**:
  - `input('안내문구')`: 사용자로부터 키보드 입력을 받는 파이썬 표준 함수입니다.
  - **중요**: 사용자가 숫자를 입력하더라도 `input()`의 반환값은 **무조건 문자열(`str`)**입니다.
  - 따라서 산술 연산을 수행하려면 반드시 `int()`나 `float()`로 감싸 형 변환을 해주어야 합니다.

---

### 1.2 `print()` 함수의 출력 옵션 비교

```python
# 큰따옴표를 연속으로 붙인 경우 (+ 연산과 동일하게 공백 없이 연결됨)
# print("life" "is" "too short") # lifelistoo short
# print("life" + "is" + "too short")

# 쉼표(,)로 구분한 경우 (자동으로 띄어쓰기 공백 하나가 추가됨)
# print("life", "is", "too short") # life is too short

# end 옵션 활용 (기본 개행 '\n' 대신 원하는 문자로 끝맺음)
# print("life", end = " ")
# print("is", "too short") # life is too short
```

- **설명**:
  - `print("a" "b")`: 따옴표로 둘러싸인 문자열 리터럴을 나열하면 `+` 연산자를 사용한 것과 같이 공백 없이 결합됩니다.
  - `print("a", "b")`: 콤마(`,`)로 인자를 나열하면 요소들 사이에 자동으로 공백(기본 구분자 `sep=' '`)이 들어갑니다.
  - `end=" "`: `print()` 실행 후 기본으로 들어가는 줄바꿈(`\n`) 대신 공백이나 다른 문자를 지정할 수 있습니다.

---

### 1.3 `input()` 값을 이용한 덧셈 연산과 형 변환

```python
# input1 = input('첫 번째 숫자를 입력하세요:')
# input2 = input('두 번째 숫자를 입력하세요:')

# total = int(input1) + int(input2)
# print('두 숫자의 합은 %s입니다' % total)
```

- **설명**:
  - `input1 + input2`를 그대로 실행하면 문자열 연결이 되어 `'3' + '5'`는 `'35'`가 됩니다.
  - 올바른 산술 덧셈을 위해 `int(input1) + int(input2)`로 형 변환한 후 연산합니다.

---

### 1.4 문자열 포매팅을 통한 입력값 출력

```python
height = input('키를 입력해 주세요: ')

# format() 키워드 방식
print('당신의 키는 {height}cm 입니다'.format(height = height))

# f-string 방식
print(f'당신의 키는 {height}cm 입니다')
```

- **설명**:
  - 사용자에게 입력받은 변수 `height`를 문자열 포매팅을 통해 직관적인 안내 문장으로 구성합니다.
  - `f'당신의 키는 {height}cm 입니다'` 형태의 f-string이 가장 읽기 쉽고 표준적인 방식입니다.

---

### 1.5 가변 인자(`*args`)를 이용한 평균 계산 함수 실습

```python
def avg(*args):
  sum = 0
  for i in args:
    sum += i
  result = sum / len(args)
  return print(result)

avg(1, 2)             # 1.5
avg(1, 2, 3, 4, 5)    # 3.0
```

- **설명**:
  - `*args` 매개변수로 임의 개수의 숫자 인자를 튜플로 받아 총합을 구한 뒤, 원소 개수(`len(args)`)로 나누어 평균값을 계산하고 출력합니다.

---

## 2. 핵심 요약 및 주의사항

1. **`input()` 반환값 주의**: 항상 문자열(`str`)로 입력되므로 숫자로 계산할 때는 `int(input())` 형 변환을 잊지 말아야 합니다.
2. **`print()` 콤마(`,`) vs 더하기(`+`)**:
   - `+`는 문자열끼리만 연결 가능하며 공백이 생기지 않습니다.
   - `,`는 서로 다른 자료형(문자열, 정수 등)도 함께 출력할 수 있으며 인자 사이에 공백 1칸이 자동 추가됩니다.
