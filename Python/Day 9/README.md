# [Day 9] 가변 인자/예외 설계, 정규 표현식(re), CSV 처리 및 OS 파일 시스템 제어

- **학습 일자**: 2026-09-17
- **기본 교재**: _Do it! 점프 투 파이썬_ 및 파이썬 표준 라이브러리 (`re`, `csv`, `os`, `pickle`)
- **학습 개요**: 유연한 함수 호출을 위한 위치 가변 인자(`*args`), 내장 `Exception` 상속을 통한 커스텀 비즈니스 예외 계층 설계, 정규 표현식(`re`)을 활용한 문자열 유효성 검증(이메일, 전화번호) 및 그룹핑 추출, `csv` 모듈을 통한 데이터셋 읽기(`reader`, `DictReader`), `os` 모듈을 통한 파일 경로/디렉터리 조작 및 메타데이터 조회, `pickle`과 객체지향 설계를 종합한 할 일 관리 시스템(`TodoSystem`) 실습.

---

## 📑 세션별 상세 학습 노트 바로가기

각 세션별 실습 코드와 상세한 해설은 아래 개별 마크다운 문서에 정리되어 있습니다.

| 세션 | 실습 파일 | 정리 문서 | 주요 학습 내용 |
| :--- | :--- | :--- | :--- |
| **Session 1** | [`session1.py`](./session1.py) | 📖 [**Session 1 정리 문서**](./session1.md) | 가변 인자(`*args`), 조기 반환(Early Return), 사용자 정의 예외(`Exception` 상속), `raise`, 세부 `try-except` |
| **Session 2** | [`session2.py`](./session2.py) | 📖 [**Session 2 정리 문서**](./session2.md) | 정규 표현식(`re`), 메타문자(`\d`, `\w`, `\s`), `match()` vs `search()`, 이메일 정규식, `findall()`, 명명된 그룹(`?P<name>`) |
| **Session 3** | [`session3.py`](./session3.py) | 📖 [**Session 3 정리 문서**](./session3.md) | `csv.reader` vs `csv.DictReader`, `os.path`(`exists`, `isfile`, `isdir`, `join`), `os.listdir`, `os.path.getsize` |
| **종합 과제** | [`test.py`](./test.py) | 📋 [**TodoSystem 과제 코드**](./test.py) | 객체 모델링(`User`, `Task`), 직렬화(`pickle`), 인증/인가(일반 유저 및 관리자 권한 분기), 할 일 우선순위 CRUD |

---

## 1. Day 9 핵심 문법 및 기법 비교 (Quick Reference)

### 1.1 `re.match()` vs `re.search()` vs `re.findall()`

| 구분 | `re.match(pattern, string)` | `re.search(pattern, string)` | `re.findall(pattern, string)` |
| :--- | :--- | :--- | :--- |
| **탐색 범위** | **문자열의 시작 위치(인덱스 0)** | **문자열 전체(첫 매칭 위치)** | **문자열 전체(모든 매칭 항목)** |
| **반환 타입** | `Match` 객체 (불일치 시 `None`) | `Match` 객체 (불일치 시 `None`) | `List` (일치한 문자열 또는 튜플 리스트) |
| **주요 용도** | 전체 형식/시작 패턴 검증 (이메일 등) | 문장 속 키워드 또는 특정 포맷 첫 위치 탐색 | 문장 내 모든 대상 추출 (전화번호, 링크 등) |

### 1.2 CSV 데이터 읽기 방식 비교: `csv.reader` vs `csv.DictReader`

| 구분 | `csv.reader` | `csv.DictReader` |
| :--- | :--- | :--- |
| **데이터 행 반환 형식** | 문자열 리스트 (`list`) | 딕셔너리 (`dict`) |
| **컬럼 접근 방식** | 인덱스 기반 (`row[0]`, `row[1]`) | 헤더(컬럼명) 기반 (`row['날짜']`) |
| **장점** | 메모리 오버헤드가 적고 단순함 | 컬럼 순서 변경에 안전하며 가독성이 뛰어남 |
| **적합한 상황** | 헤더가 없거나 단순 인덱스 접근이 필요할 때 | 헤더가 있고 필드 의미가 명확한 데이터 분석 시 |

---

## 2. Day 9 핵심 복습 포인트 (Cheat Sheet)

1. **`*args` 패킹과 안전성 확보**:
   - `*args`는 전달된 인자를 튜플로 묶습니다. 비어 있는 경우 `if not args: return None` 처럼 조기 반환을 두어야 `max()` 등의 시퀀스 함수 호출 시 발생하는 에러를 막을 수 있습니다.
2. **도메인 예외 클래스 상속 (`class CustomError(Exception): pass`)**:
   - 업무 로직상 허용되지 않는 상황(재고 부족, 비정상 수량)은 일반 `ValueError`보다 사용자 정의 예외를 발생(`raise`)시키는 것이 디버깅과 호출자 분기 처리에 훨씬 명확합니다.
3. **정규 표현식의 Raw String 접두사 (`r'...'`)**:
   - 정규식의 백슬래시(`\d`, `\w`, `\s`)가 파이썬 인터프리터의 탈출 문자로 오작동하지 않도록 항상 패턴 문자열 앞에 `r`을 붙입니다.
4. **플랫폼 독립적인 경로 결합 (`os.path.join`)**:
   - OS마다 다른 디렉터리 구분자(`\` 또는 `/`) 문제를 해결하기 위해 경로를 문자열 덧셈(`+`) 대신 `os.path.join()`으로 결합해야 크로스 플랫폼 호환성이 유지됩니다.
5. **객체 영속화 (`pickle` vs `json`)**:
   - `pickle`은 파이썬 클래스 인스턴스(객체의 메서드 및 속성 구조)를 그대로 바이너리(`wb`/`rb`)로 저장/복원할 수 있어 `TodoSystem`과 같은 객체 기반 시스템의 상태 저장에 매우 유용합니다.
