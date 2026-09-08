# [Day 2] 파이썬 심화 기초 학습 요약 및 세션 목차

- **학습 일자**: 2026-09-08
- **기본 교재**: _Do it! 점프 투 파이썬_
- **학습 개요**: 튜플 언패킹, 딕셔너리(Dictionary), 집합(Set), 메모리 참조(id, is), 2장 종합 문제 풀이, 제어문(if, while) 및 루프 제어

---

## 📑 세션별 상세 학습 노트 바로가기

각 세션별 실습 코드와 상세한 해설은 아래 개별 마크다운 문서에 정리되어 있습니다.

| 세션 | 실습 파일 | 정리 문서 | 주요 학습 내용 |
| :--- | :--- | :--- | :--- |
| **Session 1** | [`session1.py`](./session1.py) | 📖 [**Session 1 정리 문서**](./session1.md) | 튜플 패킹/언패킹, 딕셔너리 기초 및 메서드(`keys`, `values`, `items`, `pop`, `clear`, `get`), 리스트 조작 복습 실습 |
| **Session 2** | [`session2.py`](./session2.py) | 📖 [**Session 2 정리 문서**](./session2.md) | 집합(Set) 특징(순서X, 중복X), 형 변환, 집합 연산(교/합/차집합), 관계 검사(`isdisjoint`, `issubset`), 메서드(`add`, `update`, `remove` vs `discard`) |
| **Session 3** | [`session3.py`](./session3.py) | 📖 [**Session 3 정리 문서**](./session3.md) | 메모리 주소(`id()`, `is`), 얕은 복사(`copy`), 2장 되새김 종합 문제 8종 풀이(평균, 홀짝, replace, join, 중복제거, 변수참조) |
| **Session 4** | [`session4.py`](./session4.py) | 📖 [**Session 4 정리 문서**](./session4.md) | 조건문(`if`), 논리연산자(`and`/`or`/`not`), 멤버십(`in`/`not in`), 중첩 조건문, `while` 루프, `continue`, `break`, `while-else` |
| **Session 5** | [`session5.py`](./session5.py) | 📖 [**Session 5 정리 문서**](./session5.md) | `while True` 무한 루프와 탈출, 딕셔너리 요소 추가/`del` 삭제, 리스트-집합-문자열 형 변환, 집합 연산 복습 |

---

## 1. Day 2 핵심 자료형 비교 (Quick Reference)

| 자료형 | 기호 | 순서 유지 | 중복 허용 | 가변성(수정/삭제) | 주요 용도 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **리스트 (`list`)** | `[]` | O | O | **가능 (Mutable)** | 순서가 있는 가변 목록 데이터 |
| **튜플 (`tuple`)** | `()` | O | O | **불가 (Immutable)** | 변경되면 안 되는 안전한 데이터, 언패킹 |
| **딕셔너리 (`dict`)** | `{Key: Value}` | O (3.7+) | Key 불가, Value 허용 | **가능 (Mutable)** | Key 기반의 빠른 검색 및 JSON 형태 매핑 |
| **집합 (`set`)** | `{}` 또는 `set()` | X | **불가 (Unique)** | **가능 (Mutable)** | 중복 제거, 합/교/차집합 연산, 고속 원소 탐색 |

---

## 2. Day 2 핵심 복습 포인트 (Cheat Sheet)

1. **튜플 언패킹**:
   - `w, x, y, z = tu22`와 같이 좌변 변수 개수와 우변 원소 개수가 반드시 같아야 함.
2. **딕셔너리 안전 조회 (`get`)**:
   - `dic['key']`는 키가 없으면 `KeyError` 발생, `dic.get('key')`는 `None` 반환으로 안전함.
3. **딕셔너리 순회 패턴**:
   - `for k, v in dic.items():` 구문으로 Key와 Value를 동시에 언패킹하며 순회하는 것이 가장 파이써닉한 방식.
4. **리스트 삭제 3대 방식 구분**:
   - `del a[i]`: 인덱스 위치 기준 삭제 (반환값 없음)
   - `a.pop(i)`: 인덱스 위치 기준 삭제 (꺼낸 값을 반환)
   - `a.remove(val)`: 일치하는 값 기준 첫 번째 항목 삭제
5. **빈 집합 생성 주의**:
   - `{}`는 빈 딕셔너리로 인식되므로 빈 집합은 반드시 `set()`으로 생성해야 함.
6. **집합 삭제 메서드 (`remove` vs `discard`)**:
   - `remove(x)`는 원소가 없으면 `KeyError`를 발생시키지만, `discard(x)`는 없어도 에러 없이 안전하게 통과함.
7. **얕은 복사 vs 참조 복사**:
   - `b = a`는 동일 메모리 주소를 공유(`b is a` -> `True`), `copy(a)` 또는 `a[:]`는 새로운 독립 복제본 생성(`b is a` -> `False`).
8. **딕셔너리 Key 조건**:
   - 불변(Immutable) 타입(`str`, `int`, `tuple`)만 가능하며, 가변 타입(`list`, `dict`)은 Key로 사용 시 `TypeError` 발생.
9. **`in` 연산자의 딕셔너리 검사 기준**:
   - `'item' in dic`은 Key 존재를 검사하므로, Value 존재를 검사하려면 `'item' in dic.values()`를 명시해야 함.
10. **`while-else` 동작 원리**:
    - 반복문이 `break` 없이 정상 종료되었을 때만 `else` 블록이 실행됨.
