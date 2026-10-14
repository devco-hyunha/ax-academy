# Session 6 — 집계 함수 + GROUP BY

> 단원: [unit2_queries — SQL Querying](#unit2-queries---sql-querying)  
> 이전: [Session 5 — JOIN 실습](unit2_queries/session5.md) · 다음: [Session 7 — 서브쿼리](unit2_queries/session7.md)

데이터의 통계를 구하고 요약하는 집계 함수와 GROUP BY 절을 실습한다.

---

## 이번 세션 목표

| 목표 | 내용 |
| ---- | ---- |
| 집계 함수 | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` |
| GROUP BY | 같은 그룹으로 묶어 요약 |
| HAVING | GROUP 후 조건 필터 |
|ROLLUP / CUBE | 부분 totals |

---

## 1. 집계 함수 (Aggregate Functions)

| 함수 | 의미 | 비고 |
| ---- | ---- | ---- |
| `COUNT(*)` | 행의 전체 개수 | `NULL` 포함 여부와 무관 |
| `COUNT(컬럼)` | NULL이 아닌 값의 개수 | `NULL` 제외 |
| `SUM(컬럼)` | 값의 총합 | 숫자 전용 |
| `AVG(컬럼)` | 값의 평균 | 숫자 전용 |
| `MIN(컬럼)` | 최소값 | 모든 타입 |
| `MAX(컬럼)` | 최대값 | 모든 타입 |

###GROUP BY 절

- 같은 값들이 있는 행들을 **그룹**으로 묶음
- SELECT 절의 비집계 컬럼은 GROUP BY에 포함돼야 함

### HAVING 절

- GROUP BY 이후에 그룹을 필터링하는 조건
- WHERE는 행 단위 필터, HAVING은 그룹 단위 필터

---

## 2. 실습 예제

### 2.1 전체 사원 수와 급여 통계

```sql
SELECT COUNT(*) AS 전체사원수,
       COUNT(comm) AS 커미션수령자수,
       SUM(sal) AS 총급여액,
       AVG(sal) AS 평균급여,
       MIN(sal) AS 최소급여,
       MAX(sal) AS 최대급여
FROM emp;
```

### 2.2 부서별 급여 통계

```sql
SELECT deptno,
       COUNT(*) AS 인원수,
       SUM(sal) AS 부서총급여,
       AVG(sal) AS 평균급여,
       MIN(sal) AS 최소급여,
       MAX(sal) AS 최대급여
FROM emp
GROUP BY deptno
ORDER BY deptno;
```

### 2.3 직책별 평균 급여 (HAVING으로 필터)

```sql
SELECT job,
       AVG(sal) AS 평균급여
FROM emp
GROUP BY job
HAVING AVG(sal) >= 2000
ORDER BY 평균급여 DESC;
```

### 2.4 ROLLUP으로 부분 totals 추가

```sql
SELECT deptno,
       job,
       COUNT(*) AS 인원수,
       SUM(sal) AS 총급여
FROM emp
GROUP BY ROLLUP (deptno, job)
ORDER BY deptno;
```

---

## 3. 실습 문제

```sql
-- 1. 사원 전체 수를 검색하라.
SELECT COUNT(*) FROM emp;

-- 2. 보너스(comm)를 받는 사원 수를 검색하라.
SELECT COUNT(comm) FROM emp;

-- 3. 전체 급여의 합과 평균을 검색하라.
SELECT SUM(sal), AVG(sal) FROM emp;

-- 4. 가장 어린 사원과 가장 나이 많은 사원의 입사일을 검색하라.
SELECT MIN(hiredate), MAX(hiredate) FROM emp;

-- 5. 부서번호별로 사원수를 검색하라. (GROUP BY)
SELECT deptno, COUNT(*) FROM emp GROUP BY deptno ORDER BY deptno;

-- 6. 부서번호별로 평균 급여를 검색하고, 평균 급여가 2000 이상인 결과만 표시하라. (HAVING)
SELECT deptno, AVG(sal) FROM emp GROUP BY deptno HAVING AVG(sal) >= 2000 ORDER BY deptno;

-- 7. 직책별로 사원수를 검색하라.
SELECT job, COUNT(*) FROM emp GROUP BY job ORDER BY job;

-- 8. 부서번호와 직책의 조합별로 평균 급여를 검색하라.
SELECT deptno, job, AVG(sal) FROM emp GROUP BY deptno, job ORDER BY deptno, job;

-- 9. 부서번호별로 급여 평균이 2000 이상인 부서만 표시하고, 평균 급여가 높은 순으로 정렬하라.
SELECT deptno, AVG(sal) FROM emp GROUP BY deptno HAVING AVG(sal) >= 2000 ORDER BY AVG(sal) DESC;

-- 10. 직책이 'MANAGER'인 사람들에 대해 부서번호별 평균 급여를 검색하고,
--    평균 급여가 2500 이상인 그룹만 표시하라.
SELECT deptno, AVG(sal) FROM emp WHERE job = 'MANAGER' GROUP BY deptno HAVING AVG(sal) >= 2500 ORDER BY deptno;

-- [문제 68~75] student 테이블을 사용한 GROUP BY 실습
-- 68. 학생 중 키가 가장 큰 학생의 신장을 검색하라.
SELECT MAX(stu_height) FROM student;

-- 69. 학생의 이름 중 MAX와 MIN값을 검색하라.
SELECT MAX(stu_name), MIN(stu_name) FROM student;

-- 70. 학생테이블의 레코드(튜플)수를 검색하라.
SELECT COUNT(*) FROM student;

-- 71. 학과별 학생들의 인원수를 검색하라.
SELECT stu_dept, COUNT(*) FROM student GROUP BY stu_dept;

-- 72. 학과별 학생들의 인원수를 인원수가 많은 순으로 검색하라.
SELECT stu_dept, COUNT(*) FROM student GROUP BY stu_dept ORDER BY COUNT(*) DESC;

-- 73. 학년별 학생들의 인원수를 검색하라.
SELECT stu_grade, COUNT(*) FROM student GROUP BY stu_grade;

-- 74. 학과별 학년별 학생들의 평균 체중을 검색하라.
SELECT stu_dept, stu_grade, AVG(stu_weight) FROM student GROUP BY stu_dept, stu_grade;

-- 75. 학과별 학년별 학생들의 학번의 MAX와 MIN값을 검색하라.
SELECT stu_dept, stu_grade, MAX(stu_no), MIN(stu_no) FROM student GROUP BY stu_dept, stu_grade;
```

---

## 4. 한 줄 요약

1. **COUNT(*)** = 전체 행 수, **COUNT(컬럼)** = NULL 아님 값의 수
2. **SUM** = 총합, **AVG** = 평균, **MIN/MX** = 최댓/최솟값
3. **GROUP BY** = 같은 값끼리 그룹 묶기 (SELECT의 비집계 컬럼은 반드시 포함)
4. **HAVING** = GROUP 이후 그룹 필터 (WHERE는 행 단위)
5. **ROLLUP/CUBE** = 부분 totals 자동 생성

---

## [이전: Session 5 — JOIN 실습](unit2_queries/session5.md) · [다음: Session 7 — 서브쿼리](unit2_queries/session7.md)