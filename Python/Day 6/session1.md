# [Day 6 - Session 1] 파이썬 패키지(Package)와 모듈(Module) 임포트 및 `__init__.py`

- **실습 디렉토리**: `session1/` (`a.py`, `pro_test/test1/`, `pro_test/test2/`)
- **주요 내용**:
  - 패키지와 서브패키지, 모듈의 계층 구조
  - 모듈 임포트 3가지 방식 (`import`, `from ... import ... as`, `from ... import *`)
  - `__init__.py`의 역할과 `__all__`을 통한 공개 모듈 제어

---

## 1. 패키지 디렉토리 구조

```
Python/Day 6/session1/
├── a.py                               # 메인 실행 파일
└── pro_test/                          # 루트 패키지
    ├── test1/                         # 서브 패키지 1
    │   ├── __init__.py                # __all__ = ['module1']
    │   └── module1.py                 # mod1_test1(), mod1_test2()
    └── test2/                         # 서브 패키지 2
        ├── __init__.py                # __all__ = ['module2']
        └── module2.py                 # mod2_test1(), mod2_test2()
```

---

## 2. 실습 코드 및 단계별 해설

### 2.1 서브 모듈 정의 (`module1.py`, `module2.py`)

```python
# pro_test/test1/module1.py
def mod1_test1():
  print('mod1 => test1')

def mod1_test2():
  print('mod1 => test2')
```

```python
# pro_test/test2/module2.py
def mod2_test1():
  print('mod2 => test1')

def mod2_test2():
  print('mod2 => test2')
```

---

### 2.2 패키지 초기화 파일과 공개 범위 설정 (`__init__.py`)

```python
# pro_test/test1/__init__.py
# __init__.py: 해당 디렉토리가 패키지의 일부임을 알려주는 역할
# 패키지 단위의 공통 변수와 함수 정의 가능
__all__ = ['module1']
```

```python
# pro_test/test2/__init__.py
__all__ = ['module2']
```

- **`__init__.py`의 역할**:
  1. **패키지 인식**: 해당 폴더가 일반 디렉토리가 아닌 파이썬 패키지임을 인터프리터에 명시합니다. (Python 3.3+부터는 파일이 없어도 네임스페이스 패키지로 인식되나, 호환성과 초기화 설정을 위해 작성을 권장합니다.)
  2. **`__all__` 제어**: `from 패키지 import *` 문법을 사용할 때 외부로 export/노출할 모듈이나 식별자의 이름을 리스트 형태로 정의합니다. `__all__`에 포함되지 않은 모듈은 `*`로 불러와지지 않습니다.

---

### 2.3 모듈 임포트 방식 비교 (`a.py`)

```python
# 방식 1: 전체 패키지 경로를 명시하여 임포트
# import pro_test.test1.module1
# import pro_test.test2.module2
# pro_test.test1.module1.mod1_test1()
# pro_test.test2.module2.mod2_test1()

# 방식 2: 특정 모듈 가져오기 및 별칭(alias) 지정
# from pro_test.test1 import module1
# from pro_test.test2 import module2 as m2
# module1.mod1_test1()
# m2.mod2_test1()

# 방식 3: __init__.py의 __all__ 설정을 기반으로 한 와일드카드(*) 임포트
from pro_test.test1 import *
from pro_test.test2 import *

module1.mod1_test1()  # 출력: mod1 => test1
module2.mod2_test1()  # 출력: mod2 => test1
```

- **설명**:
  - **전체 경로 임포트**: 출처가 명확하지만 코드가 길어지는 단점이 있습니다.
  - **`as` 별칭(Alias)**: 모듈명이 길거나 모듈명 간 충돌이 발생할 때 간결한 이름으로 대체하여 사용합니다.
  - **`from ... import *`**: 사용은 편리하지만 네임스페이스 오염 위험이 있으므로 `__init__.py` 내에 `__all__`을 신중하게 정의해야 합니다.
