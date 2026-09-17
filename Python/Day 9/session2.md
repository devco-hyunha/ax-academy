# [Day 9 - Session 2] 정규 표현식(re 모듈) 기초 및 문자열 패턴 매칭

- **실습 파일**: `session2.py`
- **주요 내용**:
  - 정규 표현식(Regular Expression) 개념과 기본 메타문자 체계
  - `re.compile()`을 통한 패턴 컴파일 및 재사용
  - `match()`와 `search()` 메서드의 핵심 차이점
  - 이메일 유효성 검사 패턴(`re.match`)
  - 전화번호 패턴 추출(`re.findall`) 및 명명된 그룹(`(?P<name>...)`) 활용

---

## 1. 정규 표현식 기본 메타문자 정리

| 메타문자 | 의미 및 동일 표현 | 예시 매칭 |
| :--- | :--- | :--- |
| `[a-zA-Z]` | 알파벳 대소문자 전체 | `'a'`, `'Z'` |
| `[0-9]` 또는 `\d` | 모든 숫자 (Digit) | `'0'`, `'9'` |
| `\D` | 숫자가 아닌 모든 문자 (`[^0-9]`) | `'a'`, `'-'`, `' '` |
| `\s` | 공백 문자 (스페이스, 탭 `\t`, 줄바꿈 `\n` 등) | `' '`, `'\t'` |
| `\S` | 공백이 아닌 모든 문자 (`[^\s]`) | `'A'`, `'1'`, `'!'` |
| `\w` | 단어 문자: 알파벳 + 숫자 + 언더스코어 (`[a-zA-Z0-9_]`) | `'user_1'` |
| `\W` | 단어 문자가 아닌 문자 (`[^\w]`) | `'@'`, `'#'`, `' '` |
| `.` (Dot) | `\n`(개행)을 제외한 모든 단일 문자 | `'a'`, `'1'`, `'#'` |
| `+` | 1회 이상 반복 | `a+` -> `'a'`, `'aaa'` |
| `*` | 0회 이상 반복 | `a*` -> `''`, `'a'`, `'aaa'` |
| `^` / `$` | 문자열의 시작 / 문자열의 끝 | `^start`, `end$` |

---

## 2. 실습 코드 및 단계별 해설

### 2.1 `re.compile()`, `match()`, `search()`의 차이

```python
import re

# 소문자 알파벳이 1개 이상 연속된 패턴 컴파일
p = re.compile("[a-z]+")

# 1. match(): 문자열의 '처음(시작)'부터 패턴과 일치하는지 확인
m1 = p.match('python')
print(m1)  # <re.Match object; span=(0, 6), match='python'>

m2 = p.match('3 python')
print(m2)  # None (시작 문자가 숫자인 '3'이므로 매칭 실패)

# 2. search(): 문자열의 '전체'를 검색하여 처음으로 일치하는 패턴 확인
m3 = p.search('python')
print(m3)  # <re.Match object; span=(0, 6), match='python'>

m4 = p.search('3 python')
print(m4)  # <re.Match object; span=(2, 8), match='python'> (중간의 'python'을 찾아냄)
```

- **`match()`**: 문자열의 인덱스 0부터 일치해야만 결과를 반환합니다. 시작이 맞지 않으면 즉시 `None`입니다.
- **`search()`**: 문자열의 처음이 아니더라도 전체 문자열 내부를 검색하여 가장 먼저 일치하는 위치를 반환합니다.

---

### 2.2 이메일 유효성 검사 함수

```python
def email(text):
    # ^: 시작, $: 끝
    # [\w+]+ : 문자, 숫자, 밑줄, + 가 1개 이상
    # @      : 골뱅이 기호 필수
    # [\w]+  : 도메인 명
    # \.     : 온점(마침표) 리터럴
    # [\w.]+ : 최상위 도메인 등
    pattern = r'^[\w+]+@[\w]+\.[\w.]+$'
    return re.match(pattern, text)

print(email("test@naver.com"))  # Match 객체 반환 (유효한 이메일)
print(email("test-naver-com"))  # None 반환 (유효하지 않음, @ 없음)
```

- **`r'...'` (Raw String)**: 백슬래시(`\`)를 파이썬의 이스케이프 문자로 해석하지 않고 정규식 패턴 그대로 전달하기 위해 반드시 붙여주는 접두사입니다.

---

### 2.3 전화번호 추출 (`re.findall`) 및 명명된 그룹 (`?P<name>`)

```python
# 1. 전화번호 추출 (findall: 일치하는 모든 문자열을 리스트로 반환)
def phone_number(text):
    pattern = r'010-\d{3,4}-\d{4}'
    return re.findall(pattern, text)

text = "내 연락처는 010-1234-5678이고 동생 연락처는 010-994-3433입니다"
print(phone_number(text))
# 출력: ['010-1234-5678', '010-994-3433']

# 2. 명명된 그룹핑 (?P<name>...)
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")

print(m.group("name"))  # park (이름으로 지정된 그룹)
print(m.group(1))       # park (첫 번째 괄호 그룹)
print(m.group(2))       # 010-1234-1234 (두 번째 괄호 그룹)
print(m.group(3))       # 010 (세 번째 내부 괄호 그룹)
```

- **`re.findall()`**: 패턴에 일치하는 모든 매칭 결과를 순회할 필요 없이 파이썬 리스트 형태로 즉시 반환합니다.
- **`(?P<그룹명>패턴)`**: 괄호 `()` 그룹에 이름을 부여하여, 인덱스 번호(`group(1)`) 대신 직관적인 키워드(`group("name")`)로 매칭된 텍스트를 추출할 수 있습니다.
