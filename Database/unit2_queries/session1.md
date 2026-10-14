# Session 1 — SELECT 기초

> 단원: [unit2_queries — SQL Querying](#unit2-queries---sql-querying)  
> 이전: [Session 2 — DDL 실습](unit1_basic/session2.md) · 다음: [Session 2 — WHERE 조건](unit2_queries/session2.md)  
> 전제: Session 1의 `student` / `subject` / `enrol` 데이터가 있어야 한다.

```sql
USE hh;
```

---

## 이번 세션 목표

| 목표 | 내용 |
| ---- | ---- |
| 컬럼 선택 | `SELECT` 투영, `*` |
| 중복 제거 | `DISTINCT` |
| 별칭 | `AS` |
| 표현식 | 산술 연산, `CONCAT` |

---

## 1. SELECT 기본

```sql
SELECT 컬럼1, 컬럼2, ...
FROM 테이블명;
```

| 구문 | 의미 |
| ---- | ---- |
| `SELECT *` | 모든 컬럼 |
| `SELECT 컬럼` | 필요한 컬럼만 (투영) |
| `DISTINCT` | 중복 행 제거 |
| `AS` / 공백 | 결과 컬럼에 별칭 |
| 산술 (`+`, `-`, `*`, `/`) | 컬럼·상수 연산 |
| `CONCAT(...)` | 문자열 연결 |

### (추가) SQL 질의어 실행 순서 (중요!)

실제로 쓰는 문장 순서와 **엔진이 생각하는 순서**가 다르다.

```sql
SELECT 조회할 열              -- 5. 결과 선택
FROM   조회할 테이블 명        -- 1. 테이블 선택
WHERE  조회할 행 선별하는 조건식  -- 2. 행 필터링
GROUP BY 그룹화할 열 지정       -- 3. 그룹화
HAVING  출력 그룹 제한하는 조건식 -- 4. 그룹 필터링
ORDER BY 정렬하려는 열          -- 6. 정렬
```

```text
작성 순서:  SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY
처리 순서:  FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```

**핵심**: `SELECT`가 실제로는 나중에 처리되므로, 별칭을 `WHERE`에서 사용할 수 없다.

지금은 `FROM` → `SELECT`만 쓴다. 조건 필터는 [Session 4](session4.md)의 `WHERE`.

### (추가) 별칭 규칙

- `AS`는 생략 가능: `stu_no AS 학번` = `stu_no 학번`
- 한글·공백이 있으면 따옴표: `AS "학번"`
- 별칭은 **결과 표시용**. (이 단계에서는 `WHERE`에 별칭을 쓰지 않는다.)

---

## 2. 예제

```sql
SELECT * FROM student;
SELECT * FROM subject;
SELECT * FROM enrol;

SELECT stu_no, stu_name FROM student;
SELECT stu_dept FROM student;
SELECT DISTINCT stu_dept FROM student;

SELECT stu_no AS ID, enr_grade FROM enrol;
SELECT enr_grade + 10 FROM enrol;
```

---

## 3. 실습 문제

```sql
-- 1. 과목들의 과목번호와 과목이름을 검색하라.
SELECT sub_no, sub_name FROM subject;

-- 2. 학생들의 학번과 이름, 성별을 검색하라.
SELECT stu_no, stu_name, stu_gender FROM student;

-- 3. 학생들의 모든 정보를 검색하라.
SELECT * FROM student;

-- 4. 학생들의 학번과 이름, 학년, 반을 검색하라.
SELECT stu_no, stu_name, stu_grade, stu_class FROM student;

-- 5. 과목들의 과목이름과 교수이름을 검색하라.
SELECT sub_name, sub_prof FROM subject;

-- 6. 과목번호, 학번, 점수를 검색하라.
SELECT sub_no, stu_no, enr_grade FROM enrol;

-- 7. 학생들의 체중과 신장을 학번, 이름과 함께 검색하라.
SELECT stu_no, stu_name, stu_height, stu_weight FROM student;

-- 8. 학생들의 학과 중복을 제거하고 검색하라.
SELECT DISTINCT stu_dept FROM student;

-- 9. 학생들의 성별 중복을 제거하고 검색하라.
SELECT DISTINCT stu_gender FROM student;

-- 10. 학생들의 학년 중복을 제거하고 검색하라.
SELECT DISTINCT stu_grade FROM student;

-- 11. 학생들의 학과, 학년 중복을 제거하고 검색하라.
SELECT DISTINCT stu_dept, stu_grade FROM student;

-- 12. 학생들의 학과, 반 중복을 제거하고 검색하라.
SELECT DISTINCT stu_dept, stu_class FROM student;

-- 13. 학생들의 체중을 5만큼 증가시킨 값을 검색하라.
SELECT stu_weight + 5 FROM student;

-- 14. 학생들의 체중을 5만큼 감소시킨 값을 검색하라.
SELECT stu_weight - 5 FROM student;

-- 15. 학생들의 학번과 이름을 별칭 "학번", "이름"으로 부여하여 검색하라.
SELECT stu_no AS "학번", stu_name AS "이름" FROM student;

-- 16. 수강(enrol)테이블의 모든 정보를 검색하라.
SELECT * FROM enrol;

-- 17. 학생 테이블에서 학과명과 이름을 합쳐서 검색하라.
SELECT CONCAT(stu_dept, ' / ', stu_name) FROM student;

-- 18. 학생의 이름과 학과를 '컴퓨터정보과 옥한빛입니다'식으로 검색하라.
SELECT CONCAT(stu_dept, '과 ', stu_name, '입니다') FROM student;
```

---

## 한 줄 요약

1. **SELECT** = 필요한 열만 꺼내기 (투영)
2. **DISTINCT** = 중복 제거
3. **AS** = 결과 컬럼 이름(별칭)
4. **산술·CONCAT** = 조회 시점에 계산·문자열 조합
5. 처리 순서 개념: **FROM → (WHERE) → SELECT**

---

[이전: Session 1 — Basic Theory & DDL](unit1_basic/session1.md) · [다음: Session 2 — WHERE 조건](unit2_queries/session2.md)
