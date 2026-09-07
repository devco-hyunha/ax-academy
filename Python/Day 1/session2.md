# [Day 1 - Session 2] 문자열 기초, 이스케이프 코드 및 문자열 연산

- **실습 파일**: `session2.py`
- **주요 내용**: 이스케이프 시퀀스(Escape Sequences), 다중 행 문자열(`"""`, `'''`), 문자열 연산(`+`, `*`, `len()`)

---

## 1. 실습 코드 및 단계별 해설

### 1.1 이스케이프 시퀀스 (Escape Sequences)

```python
escape_code = """ 활용도가 높은 Escape 코드
\n : 개행 (enter)
\t : 탭 (tab)
\\ : 문자(백슬래시)
\' : 문자(작은따옴표)
\" : 문자(큰따옴표)
\000 : Null 문자
"""

print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")
print("It\'s Python")
print("\"Hello\"")
```

- **설명**:
  - `\`(백슬래시) 뒤에 특정 문자를 붙여 특수 동작이나 기호를 표현합니다.
  - `\n`: 줄바꿈(개행)을 수행합니다.
  - `\t`: 탭 간격만큼 띄웁니다.
  - `\\`: 백슬래시 문자 자체를 출력합니다.
  - `\'`, `\"`: 문자열 내부에서 따옴표 기호를 그대로 출력합니다.

---

### 1.2 다중 행 문자열 (Multiline Strings) 및 따옴표 포함 기법

```python
print("""python
well
come""")

print('''python
well
come''')
print() # 빈 줄 출력

food = "Python's favorite food is perl"
print(food)

say = '"Python is very easy." he said.'
print(say)

say2 = "'Python is very easy.' he said."
print(say2)
```

- **설명**:
  - `"""` 또는 `'''` 삼중 따옴표를 사용하면 `\n` 없이도 코드에서 작성한 줄바꿈 형태 그대로 여러 줄 문자열을 유지합니다.
  - 큰따옴표 안에 작은따옴표(`"Python's..."`)를 넣거나 작은따옴표 안에 큰따옴표(`' "..." '`)를 넣으면 이스케이프 문자 없이도 따옴표를 자연스럽게 포함할 수 있습니다.
  - 인자 없는 `print()`는 빈 줄(줄바꿈 1회)을 출력합니다.

---

### 1.3 문자열 기본 연산 (`+`, `*`, `len()`)

```python
# 문자열 연산
head = "Python"
tail = " is fun"
print(head + tail)
print(head * 2)
print(len(head))
```

- **설명**:
  - `head + tail`: 두 문자열을 하나로 연결합니다 (`"Python is fun"`).
  - `head * 2`: 문자열을 지정한 횟수만큼 반복합니다 (`"PythonPython"`).
  - `len(head)`: 문자열의 글자 수(길이)를 반환합니다 (`6`).

---

## 2. 핵심 요약

1. **따옴표 포함 시 규칙**: 큰따옴표/작은따옴표를 섞어 쓰면 이스케이프 문자 없이 깔끔한 코드 작성이 가능합니다.
2. **다중 행 작성**: SQL 쿼리문이나 긴 안내 메시지를 작성할 때 삼중 따옴표(`"""`)를 적극 활용합니다.
