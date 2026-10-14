# Session 5 — JOIN 실습 (emp / dept / salgrade)

> 단원: [unit2_queries — SQL Querying](#unit2-queries---sql-querying)  
> 이전: [Session 4 — SCOTT 스키마](unit2_queries/session4.md) · 다음: [Session 6 — 집계 함수 + GROUP BY](unit2_queries/session6.md)

MySQL에서 `emp`, `dept`, `salgrade` 테이블을 사용해 다양한 JOIN 형태를 실습한다.

---

## 이번 세션 목표

| 목표 | 내용 |
| ---- | ---- |
| INNER JOIN | 매칭되는 행만 조회 |
| LEFT OUTER JOIN | 왼쪽에 모든 행, 오른쪽에 매칭되는 행 |
| RIGHT OUTER JOIN | 오른쪽에 모든 행, 왼쪽에 매칭되는 행 |
| CROSS JOIN | 모든 경우의 수 조합 |
| SELF JOIN | 같은 테이블을 자기 참조해 조인 |

---

## 1. JOIN 기본 개념

### 조인의 종류

| 조인 유형 | 설명 |
|----------|------|
| **등가 조인 (Equi Join)** | 두 테이블에서 공통 컬럼의 값이 일치하는 행을 연결 |
| **자체 조인 (Self Join)** | 하나의 테이블을 두 개처럼 사용하여 자기 자신과 조인 |
| **외부 조인 (Outer Join)** | 한쪽 테이블의 모든 행을 포함하면서 다른 테이블의 관련 행을 가져오는 조인 |
| **교차 조인 (Cross Join)** | 모든 경우의 수를 조합 (카테시안 곱) |

### 등가 조인의 문법 (4가지)

```sql
-- 1. NATURAL JOIN: 공통 컬럼 이름을 자동으로 인식
SELECT * FROM emp NATURAL JOIN dept;

-- 2. JOIN USING: 공통 컬럼을 명시적으로 지정
SELECT * FROM emp JOIN USING (deptno);

-- 3. JOIN ON: 조인 조건을 직접 작성
SELECT * FROM emp e JOIN dept d ON e.deptno = d.deptno;

-- 4. WHERE절 조인 (오래된 문법)
SELECT * FROM emp e, dept d WHERE e.deptno = d.deptno;
```

### INNER JOIN (내부 조인)

```sql
SELECT 컬럼들
FROM 테이블1 t1
INNER JOIN 테이블2 t2 ON t1.컬럼 = t2.컬럼;
```

- **조인 조건**을 만족하는 행만 결과에 포함
- 양쪽 테이블에 모두 매칭되는 행이 있어야 함

### LEFT OUTER JOIN (왼쪽 외부 조인)

```sql
SELECT 컬럼들
FROM 테이블1 t1
LEFT [OUTER] JOIN 테이블2 t2 ON t1.컬럼 = t2.컬럼;
```

- **왼쪽 테이블(t1)의 모든 행**을 결과에 포함
- 오른쪽에 매칭되는 행이 없으면 `NULL`로 채움

### RIGHT OUTER JOIN (오른쪽 외부 조인)

```sql
SELECT 컬럼들
FROM 테이블1 t1
RIGHT [OUTER] JOIN 테이블2 t2 ON t1.컬럼 = t2.컬럼;
```

- **오른쪽 테이블(t2)의 모든 행**을 결과에 포함
- 왼쪽에 매칭되는 행이 없으면 `NULL`로 채움

### CROSS JOIN (교차 조인)

```sql
SELECT 컬럼들
FROM 테이블1 t1
CROSS JOIN 테이블2 t2;
```

- **카테시안 곱**: 테이블1의 행 수 × 테이블2의 행 수 결과 생성
- 조인 조건이 없어 모든 경우의 수를 조합

### SELF JOIN (자기 조인)

```sql
SELECT 컬럼들
FROM 테이블 t1
JOIN 테이블 t2 ON t1.컬럼 = t2.컬럼;
```

- 같은 테이블을 별칭(`t1`, `t2`)으로 두고 조인
- 예: 사원과 그 사원의 매니저 정보를 같은 `emp` 테이블에서 조회

---

## 2. 실습 예제

### 2.1 INNER JOIN: 부서명과 사원명 조회

```sql
SELECT e.ename, d.dname
FROM emp e
INNER JOIN dept d ON e.deptno = d.deptno;
```

### 2.2 LEFT OUTER JOIN: 모든 사원과 소속 부서 (없는 부서도 포함)

```sql
SELECT e.ename, d.dname
FROM emp e
LEFT JOIN dept d ON e.deptno = d.deptno;
```

### 2.3 SELF JOIN: 사원과 그 사원의 매니저 이름 조회

```sql
SELECT e.ename AS 사원명, m.ename AS 매니저명
FROM emp e
LEFT JOIN emp m ON e.mgr = m.empno;
```

### 2.4 CROSS JOIN: 부서 수 × 사원 수 (예시)

```sql
SELECT *
FROM dept CROSS JOIN emp;
```

---

## 3. 실습 문제

```sql
-- 1. 사원번호, 사원이름, 부서이름, 직책을 검색하라 (INNER JOIN)
SELECT e.empno, e.ename, d.dname, e.job
FROM emp e
JOIN dept d ON e.deptno = d.deptno;

-- 2. 모든 사원과 소속 부서번호, 부서이름을 검색하라 (LEFT JOIN)
SELECT e.empno, e.ename, d.deptno, d.dname
FROM emp e
LEFT JOIN dept d ON e.deptno = d.deptno;

-- 3. 'KING' 사원과 같은 매니저를 관리하는 사원들의 사원이름을 검색하라 (SELF JOIN)
SELECT e.ename
FROM emp e
JOIN emp m ON e.mgr = m.empno
WHERE m.ename = 'KING';

-- 4. 부서배치가 되지 않은 사원들의 이름과 부서번호를 검색하라 (LEFT JOIN + IS NULL)
SELECT e.ename, e.deptno
FROM emp e
LEFT JOIN dept d ON e.deptno = d.deptno
WHERE d.deptno IS NULL;

-- 5. 급여가 3000 이상인 사원들의 사원이름과 등급을 검색하라 (JOIN + salgrade)
SELECT e.ename, s.grade
FROM emp e
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE e.sal >= 3000;

-- 6. 'RESEARCH' 부서 소속 사원들의 사원이름과 직무를 검색하라
SELECT e.ename, e.job
FROM emp e
JOIN dept d ON e.deptno = d.deptno
WHERE d.dname = 'RESEARCH';

-- 7. 'SALESMAN'이며, 급여가 1500 이상 3000 이하인 사원들의
--    사원이름, 급여, 등급을 검색하라 (복합 조건 + JOIN)
SELECT e.ename, e.sal, s.grade
FROM emp e
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE e.job = 'SALESMAN'
  AND e.sal BETWEEN 1500 AND 3000;
```

---

## 4. 한 줄 요약

1. **INNER JOIN** = 매칭되는 행만 반환
2. **LEFT [OUTER] JOIN** = 왼족 모든 행 + 오른족 매칭(NULL 가능)
3. **RIGHT [OUTER] JOIN** = 오른족 모든 행 + 왼족 매칭(NULL 가능)
4. **CROSS JOIN** = 카테시안 곱 (행 수 곱셈)
5. **SELF JOIN** = 같은 테이블 내부 조인 (별칭 필수)

---

## [이전: Session 4 — SCOTT 스키마](unit2_queries/session4.md) · [다음: Session 6 — 집계 함수 + GROUP BY](unit2_queries/session6.md)