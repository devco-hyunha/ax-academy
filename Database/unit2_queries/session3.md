# Session 3 — 문자열 함수 + ORDER BY

> 단원: [unit2_queries — SQL Querying](#unit2-queries---sql-querying)  
> 이전: [Session 2 — WHERE 조건](unit2_queries/session2.md) · 다음: [Session 4 — SCOTT 스키마](unit2_queries/session4.md)  
> 전제: Session 1의 `student` / `subject` / `enrol` 데이터

```sql
USE hh;
```

---

## 이번 세션 목표

| 목표 | 내용 |
| ---- | ---- |
| 문자열 함수 | `LENGTH`, `INSTR`, `LPAD`, `RPAD` |
| (참고) 추가 함수 | `SUBSTRING`, `UPPER`, `LOWER`, `REPLACE`, `TRIM`, `CONCAT` |
| 정렬 | `ORDER BY` ASC / DESC |

---

## 1. 문자열 함수

| 함수 | 의미 | 예 |
| ---- | ---- | -- |
| `LENGTH(str)` | 바이트/길이 (문자셋에 따라 다름) | `LENGTH(stu_name)` |
| `INSTR(str, substr)` | `substr`이 처음 나오는 위치 (없으면 0) | `INSTR(stu_name, '김')` |
| `RPAD(str, len, pad)` | 오른쪽에 `pad`를 채워 `len` 길이 | `RPAD(stu_name, 15, '&')` |
| `LPAD(str, len, pad)` | 왼쪽에 `pad`를 채워 `len` 길이 | `LPAD(stu_dept, 20, '%')` |
| `REPLACE(str, from_str, to_str)` | `from_str`을 `to_str`으로 치환 | `REPLACE(stu_name, '김', '박')` |
| `TRIM(str)` | 문자열의 양쪽 공백 제거 | `TRIM(stu_name)` |
| `CONCAT(str1, str2)` | 문자열 결합 | `CONCAT(stu_dept, stu_name)` |
| `REVERSE(str)` | 문자열 뒤집기 | `REVERSE(stu_name)` |
| `SOUNDEX(str)` | 발음 유사성 코드 | `SOUNDEX('김민수')` |
| `FIELD(str, str1, str2, ...)` | 문자의 위치 반환 (IN 역연산) | `FIELD(stu_dept, '기계', '컴퓨터정보')` |

### (참고) 자주 쓰는 추가 함수

```sql
-- 부분 문자열 (시작 위치 1부터)
SELECT SUBSTRING(stu_name, 1, 1) FROM student;

-- 대소문자 (영문)
SELECT UPPER('hello'), LOWER('HELLO');
```

> 한글 이름에 `LENGTH`를 쓰면 문자셋(예: utf8mb4)에 따라 **글자 수 ≠ 바이트 수**일 수 있다.  
> 글자 수가 필요하면 `CHAR_LENGTH(stu_name)`을 쓴다.

---

## 2. ORDER BY — 정렬

```sql
SELECT 컬럼들
FROM 테이블명
WHERE 조건          -- 선택
ORDER BY 컬럼 [ASC | DESC], ...;
```

| 키워드 | 의미 |
| ------ | ---- |
| `ASC` | 오름차순 (기본값) |
| `DESC` | 내림차순 |

```sql
-- 학년 오름차순
SELECT stu_no, stu_name, stu_grade FROM student ORDER BY stu_grade;

-- 체중 내림차순
SELECT stu_no, stu_name, stu_weight FROM student ORDER BY stu_weight DESC;

-- 학과 오름차순, 같은 학과면 이름 오름차순
SELECT stu_dept, stu_name FROM student ORDER BY stu_dept, stu_name;

-- NULL 키는 정렬 시 맨 앞 또는 맨 뒤(설정·버전 영향). 보통 명시적으로 확인한다.
SELECT stu_no, stu_name, stu_height FROM student ORDER BY stu_height;
```

처리 순서 개념:

```text
FROM → WHERE → SELECT → ORDER BY
```

---

## 3. 실습 문제 — 문자열 함수

```sql
-- 1. 학생들의 이름과 이름의 길이를 검색하라.
SELECT stu_name, LENGTH(stu_name) FROM student;

-- 2. 학생들의 학과와 학과명의 길이를 검색하라.
SELECT stu_dept, LENGTH(stu_dept) FROM student;

-- 3. 학생들의 이름에 '김'이 처음 몇번째 있는지 검색하라.
SELECT stu_name, INSTR(stu_name, '김') FROM student;

-- 4. 학생의 이름을 15자리로 하고, 뒤에 '&'를 채워 검색하라.
SELECT RPAD(stu_name, 15, '&') FROM student;

-- 5. 학생의 학과를 20자리로 하고, 앞에 '%'를 채워 검색하라.
SELECT LPAD(stu_dept, 20, '%') FROM student;

-- 6. 학생 이름의 '김'을 '박'으로 바꾸어 검색하라.
SELECT REPLACE(stu_name, '김', '박') FROM student;

-- 7. 학생 이름의 양쪽 공백을 제거하여 검색하라.
SELECT TRIM(stu_name) FROM student;

-- 8. 학생의 학과와 이름을 연결하여 검색하라.
SELECT CONCAT(stu_dept, ' ', stu_name) FROM student;

-- 9. 학생 이름의 순서를 뒤집어 검색하라.
SELECT REVERSE(stu_name) FROM student;

-- 10. 학생 이름의 발음 유사성 코드( SOUNDEX )를 검색하라.
SELECT SOUNDEX(stu_name) FROM student;

-- 11. 전공이 '기계'이거나 '전기전자'인 학생의 찾기(FIELD 함수).
SELECT FIELD(stu_dept, '기계', '전기전자', '컴퓨터정보') FROM student;
```

## 4. 실습 문제 — ORDER BY (추가)

```sql
-- 6. 학생을 학번 오름차순으로 검색하라.
SELECT * FROM student ORDER BY stu_no;

-- 7. 학생의 학번, 이름, 체중을 체중 내림차순으로 검색하라.
SELECT stu_no, stu_name, stu_weight FROM student ORDER BY stu_weight DESC;

-- 8. 컴퓨터정보 학생을 학년 오름차순, 이름 오름차순으로 검색하라.
SELECT stu_no, stu_name, stu_grade FROM student
WHERE stu_dept = '컴퓨터정보'
ORDER BY stu_grade, stu_name;

-- 9. 수강 점수를 높은 순으로 학번, 과목번호, 점수와 함께 검색하라.
SELECT stu_no, sub_no, enr_grade FROM enrol ORDER BY enr_grade DESC;
```

---

## 한 줄 요약

1. **LENGTH / INSTR / LPAD / RPAD** = 문자열 길이·위치·패딩
2. 한글 글자 수 → **`CHAR_LENGTH`** 고려
3. **REPLACE** = 문자열 치환
4. **TRIM** = 공백 제거
5. **CONCAT** = 문자열 연결
6. **REVERSE** = 문자열 뒤집기
7. **SOUNDEX** = 발음 코드 생성
8. **FIELD** = 문자 위치 찾기 (IN 역연산)
9. **ORDER BY** = 결과 정렬 (`ASC` 기본, `DESC` 내림차순)
10. 여러 컬럼 정렬 가능: `ORDER BY a, b`
11. 처리 순서: **FROM → WHERE → SELECT → ORDER BY**

---

[이전: Session 2 — WHERE 조건](unit2_queries/session2.md) · [다음: Session 4 — SCOTT 스키마](unit2_queries/session4.md)
