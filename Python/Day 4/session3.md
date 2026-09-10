# [Day 4 - Session 3] 파일 입출력(File I/O) 종합: 읽기/쓰기, with문, 파일 순회 및 자동 넘버링

- **실습 파일**: `session3.py`
- **대상 리소스**: `./resource/news.txt`, `./resource/test2.txt`
- **주요 내용**:
  - 파일 열기 함수 `open()`과 파일 객체 생성
  - 파일 열기 3대 기본 모드 (`r`, `w`, `a`)
  - 인코딩 옵션 (`encoding='UTF-8'`)과 한글 깨짐 방지
  - 파일 객체의 주요 속성 (`name`, `mode`, `encoding`)
  - 파일 읽기 메서드 비교 (`readline()`, `readlines()`, `read()`, `read(n)`) 및 파일 포인터 동작 원리
  - 파일 순회 (`for line in f`, `while True` + `readline()`)
  - 파일 쓰기 메서드 (`f.write()`, `f.writelines()`)
  - 컨텍스트 매니저 (`with open() as f:`)를 통한 자동 자원 해제
  - [심화] 중복 파일명 방지 자동 넘버링 (`(1)`, `(2)` 등 생성) 패턴

---

## 1. 실습 코드 및 단계별 해설

### 1.1 파일 열기 (`open`)와 파일 열기 모드

```python
# 파일 입출력
# 객체 변수 = open(파일명, 파일 열기 모드, encoding=...)
# 파일 열기 모드:
#   r : 읽기 모드 (Read) - 기본값, 파일이 없으면 FileNotFoundError
#   w : 쓰기 모드 (Write) - 파일 생성, 동일 파일이 이미 존재하면 기존 내용 삭제(덮어쓰기)
#   a : 추가 모드 (Append) - 기존 파일 내용의 끝에 새로운 내용 추가

# 'w' 모드로 open 시 작업 후 close() 필수

f = open('./resource/news.txt', 'r', encoding='UTF-8')
```

- **설명**:
  - `open(파일경로, 모드, encoding)`: 파일을 열고 파일과 통신할 수 있는 파일 객체(File Handle)를 반환합니다.
  - **`encoding='UTF-8'`**: 한글이 포함된 텍스트 파일을 윈도우 환경에서 열 때 운영체제 기본 인코딩(CP949)으로 인한 문자 깨짐(`UnicodeDecodeError`)을 방지하기 위해 필수적으로 지정합니다.
  - **모드별 특징**:
    - `'r'` (읽기): 파일의 내용을 읽기만 할 때 사용하며, 파일이 존재하지 않으면 에러가 발생합니다.
    - `'w'` (쓰기): 파일을 새로 생성하여 쓸 때 사용하며, **기존 파일이 있으면 원래 내용이 모두 지워지고 새로 작성**되므로 주의해야 합니다.
    - `'a'` (추가): 기존 파일의 내용을 보존하면서 맨 끝에 이어 쓸 때 사용합니다.

---

### 1.2 파일 객체의 주요 속성 (Attributes)

```python
print(f)           # <_io.TextIOWrapper name='./resource/news.txt' mode='r' encoding='UTF-8'>
print(f.encoding)  # 'UTF-8'
print(f.name)      # './resource/news.txt'
print(f.mode)      # 'r'
```

- **설명**:
  - 파일 객체 `f`는 파일 자체의 메타데이터를 속성으로 가지고 있습니다.
  - `f.encoding`: 현재 파일을 읽고 쓰는 인코딩 방식 반환.
  - `f.name`: 열려 있는 파일의 경로와 이름 반환.
  - `f.mode`: 열려 있는 파일 모드(`'r'`, `'w'`, `'a'`) 반환.

---

### 1.3 파일 읽기 3대 메서드와 파일 포인터(Cursor) 동작

```python
print(f.readline())  # '1번째 줄입니다\n'
print(f.readlines()) # ['2번째 줄입니다\n', '3번째 줄입니다\n', ..., '9번째 줄입니다']
print(f.read())      # '' (빈 문자열)
```

- **설명**:
  - 파일은 내부적으로 **파일 포인터(커서, File Pointer)**를 가지고 있어서, 한 번 읽은 위치 다음부터 연속해서 읽기를 진행합니다.
  1. **`f.readline()`**:
     - 파일의 **단 한 줄**만 문자열로 읽어옵니다. 줄 끝의 개행 문자(`\n`)까지 포함됩니다.
     - 실행 후 파일 포인터는 2번째 줄의 시작 위치로 이동합니다.
  2. **`f.readlines()`**:
     - 현재 포인터 위치부터 파일 끝까지의 모든 줄을 읽어, **각 줄을 요소로 갖는 리스트**로 반환합니다 (`['2번째 줄입니다\n', ...]`).
     - 실행 후 파일 포인터는 파일의 맨 끝(EOF: End Of File)에 도달합니다.
  3. **`f.read()`**:
     - 파일의 내용을 통째로 하나의 거대한 문자열로 읽어옵니다.
     - 위의 실습에서는 이미 `readlines()`가 파일 끝까지 읽어버렸기 때문에, 뒤이어 호출한 `read()`는 읽을 내용이 없어 **빈 문자열(`''`)**을 반환하게 됩니다.

---

### 1.4 파일 닫기 (`close`)와 경로 주의점

```python
# f = open('./resource/news.txt', 'w')
# 상위 폴더(resource)가 없을 경우 FileNotFoundError 오류 발생

f.close()
```

- **설명**:
  - **`f.close()`**: 작업이 끝난 파일 객체는 반드시 닫아주어야 합니다.
    - 열려 있는 파일은 운영체제 리소스를 점유하고 있으므로, `close()`를 호출해야 다른 프로그램에서 해당 파일에 접근할 수 있고 메모리 누수를 방지할 수 있습니다.
    - 쓰기(`'w'`, `'a'`) 작업의 경우 `close()`가 호출되어야 버퍼에 남아있는 데이터가 디스크에 완전히 기록(Flush)됩니다.
  - **디렉터리 경로 주의점**:
    - 파일 자체는 `'w'` 모드에서 자동 생성되지만, 파일이 위치할 **상위 폴더(`resource/`)가 존재하지 않으면 자동으로 폴더가 만들어지지 않고 `FileNotFoundError`가 발생**합니다.

---

### 1.5 파일 객체 자체를 `for` 루프로 한 줄씩 순회하기

```python
f = open('./resource/news.txt', 'r', encoding='UTF-8')
for line in f:
  print(line)
f.close()
```

- **설명**:
  - **이터레이터(Iterator)로서의 파일 객체**: 파이썬의 파일 객체 `f`는 이터러블(Iterable) 프로토콜을 지원합니다.
  - `readlines()`처럼 모든 줄을 한꺼번에 메모리 리스트로 올리지 않고, `for line in f:` 구문을 쓰면 내부적으로 `readline()`을 호출하듯 한 줄씩 가져옵니다.
  - **메모리 절약 최적화**: 기가바이트(GB) 단위 이상의 초대형 로그 파일 등을 읽을 때 가장 이상적인 방식입니다.
  - `print(line)` 출력 시 `line` 문자열 끝에 개행(`\n`)이 들어있고 `print()`도 기본 개행을 출력하므로 줄과 줄 사이에 빈 줄이 하나씩 더 생기게 됩니다. (`end=''` 옵션이나 `line.strip()`으로 조절 가능)

---

### 1.6 `'w'` 모드로 반복문을 활용한 파일 쓰기 (`write`)

```python
f = open('./resource/news.txt', 'w', encoding='UTF-8')
for i in range(1, 20):
  data = '%d번째 줄입니다\n' % i
  f.write(data)

f.close()
```

- **설명**:
  - **`f.write(str)`**: 문자열 데이터를 파일에 씁니다. `print()`와 달리 자동으로 줄바꿈(`\n`)이 들어가지 않으므로 줄바꿈이 필요하다면 문자열 끝에 명시적으로 `\n`을 붙여야 합니다.
  - `'w'` 모드로 열었기 때문에 기존 `news.txt`의 내용은 지워지고, 1부터 19까지 `1번째 줄입니다\n` ~ `19번째 줄입니다\n` 총 19줄의 텍스트가 새롭게 기록됩니다.
  - `f.close()`를 호출해야 쓰기 버퍼가 비워지며 디스크에 온전히 저장됩니다.

---

### 1.7 `with` 문(Context Manager)을 통한 안전한 자동 닫기

```python
# with open('./resource/news.txt', 'w') as f:
#   f.write("Life is to short, you need python")

with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
  c = f.read()
  print(type(c))
  print(list(c))
```

- **설명**:
  - **`with` 문 (컨텍스트 매니저)**: `with open(...) as f:` 블록을 벗어나는 순간(정상 종료든 에러 발생이든) 파이썬이 **자동으로 `f.close()`를 호출**해줍니다. 실무 표준 권장 문법입니다.
  - **`f.read()` 결과 분석**:
    - `c`는 파일 전체 내용이 담긴 단일 문자열(`str`)입니다. (`type(c)` $\to$ `<class 'str'>`)
    - `list(c)`: 문자열을 `list()`로 감싸면 개별 문자(한글, 공백, 줄바꿈 `\n`) 하나하나가 쪼개져 문자 단위 리스트가 생성됩니다.

---

### 1.8 `read(size)`: 지정한 글자 수(문자 수)만큼 읽기

```python
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
  c = f.read(30)
  print(type(c))
  print(c)
```

- **설명**:
  - `f.read(30)`: 텍스트 모드(`'r'`)에서 인자로 숫자를 전달하면 **30개 문자(글자)**만큼만 읽어옵니다. (바이트 모드 `'rb'`인 경우 30바이트를 읽음)
  - 파일 전체를 한 번에 읽지 않고 일정 청크(chunk) 단위로 끊어서 읽고 처리하고자 할 때 유용합니다.

---

### 1.9 `while True` + `readline()`으로 파일 끝까지 읽기

```python
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
  while True:
    line = f.readline()
    if not line: break
    print(line)
```

- **설명**:
  - `readline()`은 파일 끝(EOF)에 도달하면 더 이상 읽을 데이터가 없어 **빈 문자열(`''`)**을 반환합니다.
  - 빈 문자열 `''`은 파이썬 조건식에서 `False`로 취급되므로, `if not line: break` 조건을 통해 파일 끝에서 무한 루프를 안전하게 빠져나옵니다.

---

### 1.10 `readlines()` vs `writelines()` (리스트 단위 일괄 입출력)

```python
# 1) readlines()로 전체 줄을 리스트로 읽기
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
  lines = f.readlines()
  print(lines)

# 2) writelines()로 리스트의 문자열들을 파일에 한 번에 쓰기
with open('./resource/test2.txt', 'w', encoding='UTF-8') as f:
  li = ['1\n', '2\n', '3\n']
  f.writelines(li)
```

- **설명**:
  - **`f.readlines()`**: 파일의 각 줄을 문자열 원소로 하는 리스트(`['1번째 줄입니다\n', '2번째 줄입니다\n', ...]`)로 반환합니다.
  - **`f.writelines(list)`**: 문자열 리스트(또는 이터러블)를 전달받아 파일에 순서대로 씁니다.
    - **주의**: 각 요소 끝에 줄바꿈(`\n`)이 포함되어 있어야 줄이 바뀌며 저장됩니다. `writelines()` 함수 자체는 자동으로 줄바꿈을 추가하지 않습니다.

---

## 2. 심화: 중복 파일명 방지 자동 넘버링 (`(1)`, `(2)` 붙이기)

파일을 새로 생성하거나 다운로드할 때 기존 파일명이 이미 존재하면, 덮어쓰지 않고 `파일명 (1).확장자`, `파일명 (2).확장자` 형태로 숫자를 1씩 증가시켜 새 파일명을 자동으로 생성하는 실무 패턴입니다.

### 2.1 `os.path`를 활용한 전통적 방식

```python
import os

def get_unique_filename(file_path):
    # 1. 대상 파일이 존재하지 않으면 원본 경로 그대로 반환
    if not os.path.exists(file_path):
        return file_path

    # 2. 디렉터리 경로와 파일명(확장자 포함) 분리
    dir_name, full_name = os.path.split(file_path)
    # 파일 이름(stem)과 확장자(ext) 분리 (예: 'news', '.txt')
    base_name, ext = os.path.splitext(full_name)

    # 3. 중복되지 않는 파일명을 찾을 때까지 번호(count) 증가
    count = 1
    while True:
        new_name = f"{base_name} ({count}){ext}"
        new_path = os.path.join(dir_name, new_name)

        if not os.path.exists(new_path):
            return new_path

        count += 1

# 사용 예시
target = "./resource/news.txt"
unique_file = get_unique_filename(target)
print("생성할 고유 경로:", unique_file)
# news.txt가 있으면 -> ./resource/news (1).txt
# news (1).txt도 있으면 -> ./resource/news (2).txt
```

- **설명**:
  - `os.path.exists(path)`: 해당 경로에 파일 또는 폴더가 존재하는지 불리언(`True`/`False`)으로 반환합니다.
  - `os.path.splitext(full_name)`: 확장자(`.txt`)와 순수 파일 이름(`news`)을 안전하게 튜플로 분리합니다.
  - `while True` 루프: 번호를 1부터 1씩 올려가며 존재하지 않는 빈 파일명을 찾을 때까지 탐색합니다.

---

### 2.2 `pathlib.Path`를 활용한 모던 파이썬 방식 (권장)

```python
from pathlib import Path

def get_unique_path(file_path_str):
    path = Path(file_path_str)

    # 이미 존재하지 않는다면 그대로 반환
    if not path.exists():
        return path

    parent = path.parent   # 폴더 경로 (예: ./resource)
    stem = path.stem       # 순수 파일명 (예: news)
    suffix = path.suffix   # 확장자 (예: .txt)

    count = 1
    while True:
        new_path = parent / f"{stem} ({count}){suffix}"
        if not new_path.exists():
            return new_path
        count += 1

# 사용 예시
unique_path = get_unique_path("./resource/news.txt")

# 확정된 안전한 경로로 파일 생성
with open(unique_path, "w", encoding="UTF-8") as f:
    f.write("중복 없이 안전하게 생성된 파일 내용입니다.")
```

- **설명**:
  - Python 3.4 이상에서 도입된 `pathlib.Path` 객체는 문자열 분리 함수 없이도 속성(`parent`, `stem`, `suffix`)으로 경로를 직관적으로 다룰 수 있습니다.
  - 슬래시 연산자(`/`)를 이용해 경로를 간결하게 결합(`parent / filename`)할 수 있습니다.

---

## 3. 핵심 요약 (파일 읽기 / 쓰기 메서드 비교)

### 3.1 파일 읽기 메서드 비교

| 메서드 | 반환 타입 | 읽는 범위 | 특징 및 실무 활용 |
| :--- | :--- | :--- | :--- |
| **`f.readline()`** | `str` (문자열 1개) | 한 줄 | 대용량 파일을 한 줄씩 메모리에 부담 없이 처리 (`while line:` 패턴) |
| **`f.readlines()`** | `list[str]` (문자열 리스트) | 파일 전체 (줄 단위) | 모든 줄을 리스트로 받아 인덱싱, 정렬 등 처리할 때 |
| **`f.read()`** | `str` (전체 문자열 1개) | 파일 전체 (통째로) | 파일 전체 내용에서 단어 검색, 정규표현식 파싱 등 전체 분석 |
| **`f.read(n)`** | `str` (문자열) | 지정한 `n`자 | 메모리 제한을 두고 청크(Chunk) 단위로 나누어 읽을 때 |
| **`for line in f:`** | `str` (반복자 요소) | 한 줄씩 스트리밍 | **파이썬 표준 권장!** 대용량 파일도 메모리 점유 없이 안전하게 순회 |

### 3.2 파일 쓰기 메서드 비교

| 메서드 | 입력 타입 | 동작 및 특징 |
| :--- | :--- | :--- |
| **`f.write(str)`** | `str` (단일 문자열) | 문자열을 파일에 기록 (자동 개행 없음, 필요 시 `\n` 추가) |
| **`f.writelines(iterable)`** | `list[str]` 등 반복 가능 객체 | 리스트 내 문자열들을 순서대로 연속 기록 (자동 개행 없음) |

### 3.3 `with` 문 vs 일반 `open() ... close()`

| 구분 | 일반 `open()` + `f.close()` | `with open() as f:` (권장) |
| :--- | :--- | :--- |
| **자원 해제** | 명시적으로 `f.close()` 호출 필수 | 블록 탈출 시 자동으로 자원 해제 |
| **예외 발생 시** | 중간에 에러 발생 시 `close()` 미호출 위험 | 에러 발생 여부와 무관하게 무조건 안전하게 닫힘 |
| **가독성** | 파일 열림과 닫힘의 유효 범위 불분명 | 인덴트(들여쓰기)를 통해 파일 사용 스코프가 명확 |
