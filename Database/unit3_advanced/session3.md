# Session 3 — 정규화(Normalization)

> 단원: [unit3_advanced — Advanced Topics](#unit3-advanced---advanced-topics)  
> 이전: [Session 2 — 데이터 무결성](unit3_advanced/session2.md) · 다음: [Session 4 — NoSQL](unit3_advanced/session4.md)

## 1. 정규화(Normalization)의 개념

- 데이터베이스 설계에서 관계형 데이터베이스의 **이상현상을 제거**하기 위한 과정
- 반복되는 그룹을 분리하고 관계를 설정하여 데이터의 **일관성 유지**
- 정식형(1NF, 2NF, 3NF, BCNF) 수준으로 진행

## 3. 정리

1. 정규화: 데이터베이스 설계 과정에서의 이상 현상 제거 과정
2. 1NF → 2NF → 3NF → BCNF 단계로 진행
3. 실무에서는 트레이드오프(성능 vs 유지보수) 고려하여 적정 수준 결정

---

## 이번 세션 목표

| 목표           | 내용                                  |
| -------------- | ------------------------------------- |
| 분기 함수      | `IF`, `CASE WHEN`, `NULLIF`, `IFNULL` |
| 문자·숫자 변환 | `CAST`, `CONV`                        |
| NULL 안전 함수 | `COALESCE`, `NULLIF`                  |

---

## 1. 조건 분기 함수 (`IF`, `CASE WHEN`)

### 1-1. `IF(조건, 참, 거짓)`

```sql
IF(조건, 값1, 값2)
```

- 조건이 참이면 `값1`, 거짓이면 `값2`를 반환

### 1-2. `CASE WHEN` (다중 분기)

```sql
CASE WHEN 조건1 THEN 결과1
     WHEN 조건2 THEN 결과2
     ELSE 결과3
END
```

### 1-3. 단순 CASE (컬럼 비교)

```sql
CASE 컬럼
  WHEN 값1 THEN 결과1
  WHEN 값2 THEN 결과2
  ELSE 결과3
END
```

### 예시: 급여 등급 판단

```sql
SELECT ename,
  CASE
    WHEN sal >= 5000 THEN 'A급 (고액)'
    WHEN sal >= 3000 THEN 'B급 (중액)'
    ELSE 'C급 (소액)'
  END AS 급여등급
FROM emp;
```

---

## 2. NULL 관련 함수

### 2-1. `IFNULL(col, default)`

```sql
IFNULL(expr, default)
```

- `expr`이 NULL이면 `default`를 반환, 아니면 `expr`을 그대로 반환
- MySQL 전용 함수 (표준은 `COALESCE`)

### 2-2. `NULLIF(expr1, expr2)`

```sql
NULLIF(expr1, expr2)
```

- `expr1`과 `expr2`가 같으면 `NULL`을 반환
- 다르면 `expr1`을 반환
- 주로 `조건에 맞는 행은 NULL으로 숨기기`용

### 2-3. `COALESCE(col1, col2, ...)`

```sql
COALESCE(expr1, expr2, ...)
```

- 전달된 인자들 중 처음으로 NULL이 아닌 값을 반환
- 표준 SQL 지원 (MySQL, Oracle, PostgreSQL 등 호환성 좋음)

### 예시: 여러 컬럼 중 첫 번째 비NULL 값

```sql
-- commissions(커미션), bonus(보너스), 0 순서로 확인
SELECT ename, COALESCE(comm, bonuse, 0) AS 실제보너스
FROM emp;
```

---

## 3. 타입 변환 함수 (`CAST`, `CONV`)

### 3-1. `CAST(expr AS type)`

```sql
CAST(expr AS TYPE)
```

- 데이터 타입을 explícit하게 변환 (표준 SQL)
- 예: `CAST('2024-01-15' AS DATE)`, `CAST( AS CHAR)`

### 3-2. `CONV(num, from_base, to_base)`

```sql
CONV(num, from_base, to_base)
```

- 숫자를 다른 진법으로 변환
- `CONV('A', 16, 10)` → `10` (16진수 A를 10진수로)

### 예시: 숫자를 문자열로 변환

```sql
-- 급여를 문자열로 연결
SELECT ename, CONCAT(sal, '원') FROM emp;

-- 정수를 16진수로
SELECT CONV(255, 10, 16) FROM dual;  -- 'FF'
```

---

## 4. 실습 문제

```sql
-- 1. 급여가 3000 이상이면 '고액', 2000 이상이면 '중액', 그 이하라면 '소액'으로 등급을 분류하라.
SELECT ename, sal,
  CASE WHEN sal >= 3000 THEN '고액'
       WHEN sal >= 2000 THEN '중액'
       ELSE '소액' END AS 등급
FROM emp;

-- 2. 사원의 급여가 5000이면 NULL, 아니면 급여를 그대로 반환하는 NULLIF를 사용해 검색하라.
SELECT ename, NULLIF(sal, 5000) FROM emp;

-- 3. 커미션이 NULL인 경우를 0으로 표시하고, 부서번호가 NULL인 경우 '미배정'으로 표시하라.
SELECT ename, IFNULL(comm, 0), IFNULL(deptno, '미배정') FROM emp;

-- 4. 세 개의 컬럼 중 첫 번째로 NULL이 아닌 값을 찾아라 (COALESCE).
--    comm, bonuse, 0 중 가장 먼저 non-NULL인 값 반환
SELECT ename, COALESCE(comm, 0) FROM emp;

-- 5. '2024-01-15' 문자열을 DATE 타입으로 변환하여 연도만 추출하라.
SELECT CAST('2024-01-15' AS DATE);

-- 6. 숫자 255를 16진수 문자열로 변환하라.
SELECT CONV(255, 10, 16);

-- 7. 급여가 3000 초과이면 '우수', 3000 이하이면 '보통' 등급을 CASE WHEN으로 표시하라.
SELECT ename, sal,
  CASE WHEN sal > 3000 THEN '우수'
       ELSE '보통' END AS 등급
FROM emp;

-- 8. 부서번호가 10이면 '관리부', 20이면 '영업부', 30이면 '생산부', 그 외는 '기타'로 분류하라.
SELECT ename, deptno,
  CASE deptno
    WHEN 10 THEN '관리부'
    WHEN 20 THEN '영업부'
    WHEN 30 THEN '생산부'
    ELSE '기타' END AS 부서명
FROM emp;

-- 9. 급여가 5000 이상이면 '고액', 3000 이상이면 '중액', 2000 이상이면 '소액', 이하이면 '초급'으로 등급을 나누고,
--    각 등급별 평균 급여를 검색하라 (중첩 CASE WHEN).
SELECT CASE WHEN AVG(sal) >= 5000 THEN '고액'
            WHEN AVG(sal) >= 3000 THEN '중액'
            WHEN AVG(sal) >= 2000 THEN '소액'
            ELSE '초급' END AS 등급, AVG(sal) AS 평균급여
FROM emp
GROUP BY CASE WHEN AVG(sal) >= 5000 THEN '고액'
              WHEN AVG(sal) >= 3000 THEN '중액'
              WHEN AVG(sal) >= 2000 THEN '소액'
              ELSE '초급' END;

-- 10. DECODE() 호환 시뮬레이션: empno가 7369이면 'SMITH', 7499이면 'ALLEN', 7521이면 'WARD', 그 외는 '기타'로 표시.
SELECT ename, ename,
  CASE ename
    WHEN 'SMITH' THEN 'SMITH'
    WHEN 'ALLEN' THEN 'ALLEN'
    WHEN 'WARD' THEN 'WARD'
    ELSE '기타' END AS DECODEResult
FROM emp;

-- 64. 신장열의 값이 널인 학생의 경우 '미기록'으로 검색하라.
SELECT stu_no, stu_name, IFNULL(stu_height, '미기록') FROM student;

-- 65. 학생들의 성별을 소문자로 검색
SELECT LOWER(stu_gender) FROM student;

-- 66. 학생들의 학과, 이름을 연결하여 검색
SELECT CONCAT(stu_dept, ' ', stu_name) FROM student;

-- 67. 학생들의 이름과 이름의 첫 2글자를 검색
SELECT stu_name, LEFT(stu_name, 2) FROM student;

-- 68. 학생들의 이름, 학과 , 그리고 학과의 두번째부터 1자리 검색
SELECT stu_name, stu_dept, SUBSTRING(stu_dept, 2, 1) FROM student;
```

---

## 5. 한 줄 요약

1. **IF** = 3항 연산자 형태의 단순 조건
2. **CASE WHEN** = 다중 조건 분기 (복잡한 로직에 강함)
3. **NULLIF** = 같으면 NULL, 다르면 값 반환 (안전성 확보)
4. **IFNULL** = NULL을 기본값으로 치환 (MySQL 전용)
5. **COALESCE** = 표준 SQL, NULL이 아닌 첫 번째 값 반환
6. **CAST** = 데이터 타입 변환 (표준)
7. **CONV** = 진법 변환 (2진수→10진수 등)
8. 중첩 CASE WHEN 및 DECODE() 호환 시뮬레이션

---

## [이전: Session 3 — 날짜 함수](unit3_advanced/session3.md) · [다음: Session 5 — DB 모델링](unit3_advanced/session5.md)
