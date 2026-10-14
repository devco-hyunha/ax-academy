# Session 7 — 서브쿼리 (Subquery)

> 단원: [unit2_queries — SQL Querying](#unit2-queries---sql-querying)  
> 이전: [Session 6 — 집계 함수 + GROUP BY](unit2_queries/session6.md) · 다음: [unit3_advanced — Advanced Topics](../unit3_advanced/session1.md)

단일 SELECT 문 안에서 또 다른 SELECT 문을 사용하는 서브쿼리를 실습한다. 단일행, 다중행, 상관서브쿼리 등 다양한 형태를 다룬다.

---

## 이번 세션 목표

| 목표 | 내용 |
| ---- | ---- |
| 서브쿼리 기본 | SELECT FROM 절, WHERE 절 내 서브쿼리 |
| 단일행 서브쿼리 | 결과가 1행인 경우 |
| 다중행 서브쿼리 | 결과가 여러 행인 경우 (`IN`, `ANY`, `ALL`) |
| 상관 서브쿼리 | 바깥 쿼리와 연동된 서브쿼리 |
| EXISTS / NOT EXISTS | 존재 여체 기반 필터 |

---

## 1. 서브쿼리 기본 구조

```sql
SELECT 컬럼들
FROM 테이블 [별칭]
WHERE 조건 = (단일행 서브쿼리)
   OR 컬럼 IN (다중행 서브쿼리)
   OR EXISTS (SELECT * FROM 테이블 WHERE 조건);
```

### 서브쿼리의 위치

- **SELECT 절** (스칼라 서브쿼리)
- **FROM 절** (인라인 뷰)
- **WHERE 절** (조건 서브쿼리)

---

## 2. 단일행 서브쿼리 (Single-row Subquery)

결과가 **1행**만 반환되는 서브쿼리. 비교 연산자(`=`, `>`, `<`, `>=`, `<=`, `<>`)와 함께 사용.

### 예시: 'KING' 사원과 동일한 급여를 받는 사원들 조회

```sql
SELECT ename, sal
FROM emp
WHERE sal = (SELECT sal FROM emp WHERE ename = 'KING');
```

### 예시: '30' 부서 평균 급여보다 많이 받는 사원들 조회

```sql
SELECT ename, sal, deptno
FROM emp
WHERE sal > (SELECT AVG(sal) FROM emp WHERE deptno = 30);
```

---

## 3. 다중행 서브쿼리 (Multi-row Subquery)

결과가 **여러 행**을 반환하는 서브쿼리. `IN`, `ANY`, `ALL` 연산자와 함께 사용.

### `IN` 서브쿼리: 특정 부서('ACCOUNTING', 'RESEARCH')에 속한 사원들

```sql
SELECT ename, deptno
FROM emp
WHERE deptno IN (SELECT deptno FROM dept WHERE dname IN ('ACCOUNTING', 'RESEARCH'));
```

### `ANY` / `SOME` 서브쿼리: 어떤 한 명 이상이 조건을 만족하면 참

```sql
-- 'SALESMAN' 중에서 가장 낮은 급여보다 많이 받는 사원들
SELECT ename, sal
FROM emp
WHERE sal > ANY (SELECT sal FROM emp WHERE job = 'SALESMAN');
```
- `sal > ANY (...)` → `sal`이 서브쿼리 결과 중 **하나라도 큰 경우** 참
- `SOME`은 `ANY`와 동일한 별칭 (둘 다 사용 가능)

| 다중행 연산자 | 설명 |
|--------------|------|
| `IN` | 메인쿼리의 데이터가 서브쿼리의 결과 중 하나라도 일치하면 true |
| `ANY`, `SOME` | 메인쿼리의 조건식을 만족하는 서브쿼리의 결과가 하나 이상이면 true |
| `ALL` | 메인쿼리의 조건식을 서브쿼리의 결과 모두가 만족하면 true |
| `EXISTS` | 서브쿼리의 결과가 존재하면 true |

### `ALL` 서브쿼리: 모든 조건을 만족해야 함

```sql
-- 'SALESMAN' 중에서 가장 높은 급여보다 많이 받는 사원들
SELECT ename, sal
FROM emp
WHERE sal > ALL (SELECT sal FROM emp WHERE job = 'SALESMAN');
```
- `sal > ALL (...)` → `sal`이 서브쿼리 결과의 **모든 값보다 큰 경우** 참

---

## 4. 상관 서브쿼리 (Correlated Subquery)

서브쿼리가 **밖의 메인 쿼리 컬럼을 참조**하는 경우. `EXISTS`와 주로 함께 사용.

### EXISTS: 서브쿼리 결과가 한 행이라도 있으면 참

```sql
-- 부서별로 급여가 가장 높은 사원이 있는 부서 조회
SELECT d.dname
FROM dept d
WHERE EXISTS (
    SELECT * FROM emp e
    WHERE e.deptno = d.deptno
      AND e.sal = (SELECT MAX(sal) FROM emp WHERE deptno = d.deptno)
);
```

### NOT EXISTS: 서브쿼리 결과가 없을 때 참

```sql
-- 'RESEARCH' 부서에 배속된 적이 없는 사원들
SELECT e.ename
FROM emp e
WHERE NOT EXISTS (
    SELECT * FROM dept d
    WHERE d.deptno = e.deptno
      AND d.dname = 'RESEARCH'
);
```

---

## 5. 실습 문제

```sql
-- 1. 'KING' 사원과 같은 부서(DEPTNO=10)에 속한 사원들의 사원이름과 부서번호를 검색하라.
SELECT ename, deptno
FROM emp
WHERE deptno = 10;

-- 2. 'KING' 사원과 동일한 급여를 받는 사원들의 사원이름과 급여를 검색하라 (단일행 서브쿼리).
SELECT ename, sal
FROM emp
WHERE sal = (SELECT sal FROM emp WHERE ename = 'KING');

-- 3. '30' 부서의 평균 급여보다 많이 받는 사원들의 사원이름, 급여, 부서번호를 검색하라.
SELECT ename, sal, deptno
FROM emp
WHERE sal > (SELECT AVG(sal) FROM emp WHERE deptno = 30);

-- 4. 'SALESMAN' 직책을 가진 사원들 중 급여가 가장 높은 사람보다 많이 받는 사원들의
--    사원이름과 급여를 검색하라 (ANY).
SELECT ename, sal
FROM emp
WHERE sal > ANY (SELECT sal FROM emp WHERE job = 'SALESMAN');

-- 5. 'SALESMAN' 직책을 가진 사원들 중 급여가 가장 높은 사람보다 많이 받는 사원들을
--    검색하라 (ALL).
SELECT ename, sal
FROM emp
WHERE sal > ALL (SELECT sal FROM emp WHERE job = 'SALESMAN');

-- 6. 'DALLAS'에 위치한 부서에 속한 사원들의 사원이름과 부서명을 검색하라 (관계 서브쿼리).
SELECT e.ename, d.dname
FROM emp e
JOIN dept d ON e.deptno = d.deptno
WHERE d.loc = 'DALLAS';

-- 7. 부서번호가 20인 사원들 중 급여가 가장 높은 사원의 사원이름과 급여를 검색하라.
SELECT ename, sal
FROM emp
WHERE deptno = 20
  AND sal = (SELECT MAX(sal) FROM emp WHERE deptno = 20);

-- 8. emp 테이블에 부서번호가 할당되지 않은(sol NULL) 사원들의 사원이름을 검색하라
--    (NOT EXISTS 또는 IS NULL 사용).
SELECT ename
FROM emp e
WHERE e.deptno IS NULL;

-- 9. 'RESEARCH' 부서에 속한 사원들이 있는지 확인하고, 속한 사원이 있다면
--    그들의 사원이름을 검색하라 (EXISTS).
SELECT e.ename
FROM emp e
WHERE EXISTS (
    SELECT * FROM dept d
    WHERE d.deptno = e.deptno
      AND d.dname = 'RESEARCH'
);

-- 10. 평균 급여가 가장 높은 부서의 부서번호와 평균 급여를 검색하라 (인라인 뷰 포함).
SELECT deptno, avg_sal
FROM (
    SELECT deptno, AVG(sal) AS avg_sal
    FROM emp
    GROUP BY deptno
    ORDER BY avg_sal DESC
) WHERE rownum = 1;
```

---

## 6. 한 줄 요약

1. **단일행 서브쿼리** = `=` 등 비교 연산자 사용, 결과 1행
2. **다중행 서브쿼리** = `IN`/`ANY`/`ALL` 사용, 결과 여러 행
3. **상관 서브쿼리** = 바깥 쿼리 컬럼 참조, `EXISTS`와 자주 사용
4. **SELECT 절**에도 서브쿼리 가능 (스칼라 서브쿼리)
5. **FROM 절** 서브쿼리 = 인라인 뷰 (정렬·페이징 등 활용)

---

## [이전: Session 6 — 집계 함수 + GROUP BY](unit2_queries/session6.md) · [다음: unit3_advanced — Advanced Topics](../unit3_advanced/session1.md)