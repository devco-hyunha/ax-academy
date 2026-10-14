# Session 1 — RDB 특징

> 단원: [unit3_advanced — Advanced Topics](#unit3-advanced---advanced-topics)  
> 이전: [Session 7 — 서브쿼리](../unit2_queries/session7.md) · 다음: [Session 2 — 데이터 무결성](unit3_advanced/session2.md)

## 1. RDB의 특징

- **관계형 데이터 모델**에 기초를 둔 데이터베이스
- 모든 데이터를 **2차원 테이블**로 표현
- 서로 다른 테이블이 **관계를 맺고 모여있는 집합체**
- 데이터 **중복 없음** -> 가장 효율적이고 유연한 데이터 접근 방법
- **데이터 무결성** 보장
- **스키마**가 명확하게 정의되어 있음 (외부, 내부, 개념 스키마)

## 2. RDB vs NoSQL 비교

- RDB: 고정된 테이블 스키마, ACID 트랜잭션 지원, 복잡한 조인 지원
- NoSQL: 유연한 스키마, 수평 확장성, 대량 데이터 처리 용이, 트랜잭션 지원 제한

---

## 3. 정리

1. RDB는 관계형 데이터 모델에 기반한 데이터베이스
2. 2차원 테이블로 데이터 표현, 테이블 간 관계 형성
3. 데이터 중복 최소화, 무결성 보장
4. 명확한 스키마 구조 (외부/내부/개념 스키마)
5. NoSQL은 RDB의 한계를 극복하기 위한 대안적 형태

---

## 이번 세션 목표

| 목표 | 내용 |
| ---- | ---- |
| 뷰 (VIEW) | 가상 테이블, 보안 및 간소화 |
| 인덱스 (INDEX) | 검색 성능 향상을 위한 자료구조 |
| 트랜잭션 (TRANSACTION) | COMMIT, ROLLBACK, 제약 조건 |
| 트랜잭션 격리 수준 | READ COMMITTED, REPEATABLE READ 등 |

---

## 1. 뷰 (VIEW)

### 정의

- **가상 테이블**: 실제 데이터를 저장하지 않고, `SELECT` 문의 결과로 정의된 객체
- **보안**: 특정 컬럼/행만 노출하여 보안성 확보
- **복잡성 단순화**: 복잡한 JOIN·서브쿼리를 뷰로 정의해 reuse 가능

### 생성

```sql
CREATE [OR REPLACE] VIEW 뷰명
AS SELECT 쿼리문;
```

### 활용 예시: 부서명과 사원명만 포함하는 뷰

```sql
CREATE VIEW emp_dept_view
AS SELECT e.empno, e.ename, d.dname
   FROM emp e
   JOIN dept d ON e.deptno = d.deptno;
```

### 뷰 사용

```sql
SELECT * FROM emp_dept_view WHERE dname = 'ACCOUNTING';
```

### 뷰의 장점

- 테이블 구조 변경 시 뷰 정의만 수정하면 애플리케이션 영향 최소화
- 민감한 컬럼(급여 등) 제외하고 노출 가능
- 복잡한 조인을 미리 정의해두어 쿼리 작성이 간단해짐

### 뷰 삭제

```sql
DROP VIEW emp_dept_view;
```

---

## 2. 인덱스 (INDEX)

### 정의

- 테이블 검색 성능을 향상시키기 위해 **데이터 구조**(B-tree 등)에 인덱스를 생성한 것
- `WHERE`, `JOIN`, `ORDER BY` 절이 컬럼에 자주 사용될 때 성능 개선
- **덮는 인덱스**(Covering Index): SELECT 컬럼이 인덱스에만 있으면 테이블 접근 생략

### 생성

```sql
CREATE [UNIQUE] INDEX 인덱스명
ON 테이블명 (컬럼1 [ASC | DESC], 컬럼2 [ASC | DESC]);
```

### 예시: `empno`에 대한 고유 인덱스 (기본 PK는 이미 인덱스 생성됨)

```sql
CREATE INDEX idx_emp_empno ON emp (empno);
```

### 인덱스 삭제

```sql
DROP INDEX idx_emp_empno ON emp;
-- MySQL 문법:
DROP INDEX idx_emp_empno ON emp;
```

### 주의사항

- INSERT/UPDATE/DELETE 성능은 인덱스 유지 overhead 때문에 약간 감소할 수 있음
- 컬럼당 한 번만 인덱스 가능 (복합 인덱스 가능)
- 카디날리티가 낮은 컬럼(성별 등)에 인덱스 효과가 제한적임

---

## 3. 트랜잭션 (TRANSACTION)

### 정의

- **하나의 논리적 작업**을 구성하는 `UNIT OF WORK`
- **ACID 특성**:
  - **Atomicity** (원자성): 모두 성공하거나 모두 실패
  - **Consistency** (일관성): 트랜스션 전후 데이터가 규칙을 위배하지 않음
  - **Isolation** (격리성): 동시에 실행되는 트랜잭션이 서로 간섭하지 않음
  - **Durability** (지속성): 커밋된 데이터는 장애가 있어도 영구적으로 유지

### 제어 명령어

| 명령어 | 의미 |
| ------ | ---- |
| `START TRANSACTION` / `BEGIN` | 트랜잭션 시작 |
| `COMMIT` | 현재 트랜잭션의 변경 사항을 영구적으로 저장 |
| `ROLLBACK` | 트랜잭션 시작 전으로 상태를 되돌림 (미확인 변경 사항 취소) |
| `SAVEPOINT` | 트랜잭션 내에서 저장점 생성 후 부분 롤백 가능 |
| `SET TRANSACTION` | 트랜잭션 격리 수준 설정 |

### 자동 커밋(MySQL 기본값)

- MySQL은 `START TRANSACTION` 이전 문장은 **자동 커밋** 모드
- 명시적 트랜잭션을 원하면 `START TRANSACTION`을 먼저 실행

### 예시: 돈 이체 트랜잭션 (A→B 계좌 이체)

```sql
START TRANSACTION;

-- A 계좌에서 금액 차감
UPDATE account SET balance = balance - 10000 WHERE id = 'A';

-- B 계좌에 금액 추가
UPDATE account SET balance = balance + 10000 WHERE id = 'B';

-- 모든 일이 잘되면 커밋
COMMIT;

-- 어떤 실수가 있으면 전체 롤백
-- ROLLBACK;
```

---

## 4. 트랜잭션 격리 수준 (Isolation Level)

격리 수준에 따라 읽기 현상(Non-repeatable read, Phantom read) 행동이 달라짐

| 격리 수준 | 읽기 비특이성 | 설명 |
| -------- | ----------- | ---- |
| `READ UNCOMMITTED` | 발생 가능 | 커밋되지 않은 데이터도 읽을 수 있음 (Dirty read) |
| `READ COMMITTED` | **일반 기본값** | 새로운 SELECT는 항상 최신 데이터 조회 |
| `REPEATABLE READ` | **MySQL 기본값** | 트랜잭션 동안 동일한 SELECT 결과 반복 가능 |
| `SERIALIZABLE` | 발생 안 함 | 가장 엄격함, 모든 트랜잭션을 직렬화 실행 |

### MySQL에서 격리 수준 설정

```sql
-- 세션 전체에 적용
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- 현재 트랜잭션에만 적용
START TRANSACTION;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

---

## 5. 실습 문제

```sql
-- 1. emp_dept_view를 생성하고, 'ACCOUNTING' 부서 사원들만 조회하는 SELECT 문
CREATE VIEW emp_dept_view
AS SELECT e.empno, e.ename, d.dname, e.job
   FROM emp e
   JOIN dept d ON e.deptno = d.deptno;

SELECT * FROM emp_dept_view WHERE dname = 'ACCOUNTING';

-- 2. 인덱스 활용: emp 테이블에서 empno로 사원 한 명을 정확히 조회하는 query
-- (인덱스 존재 가정하에 설명하며, 실제 실행 계획은 EXPLAIN으로 확인)
SELECT * FROM emp WHERE empno = 7788;

-- 3. 트랜잭션: '10번' 부서 사원들의 급여를 10% 인상하는 트랜잭션
START TRANSACTION;

UPDATE emp
SET sal = sal * 1.1
WHERE deptno = 10;

-- 인상 후 확인 (COMMIT 전이라도 데이터 확인 가능)
SELECT empno, ename, sal FROM emp WHERE deptno = 10;

-- 모든 변경을 확정
COMMIT;

-- 실수 시 전체 취소 (ROLLBACK)
-- ROLLBACK;

-- 4. 트랜잭션 격리 수준 설정 확인
-- MySQL 기본값(REPEATABLE READ) 확인용 세션 설정
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- 5. SAVEPOINT를 활용한 부분 롤백 예제
START TRANSACTION;

INSERT INTO emp VALUES (9999, 'TEST', 'CLERK', NULL, '2024-01-01', 1000, NULL, 20);

SAVEPOINT sp1;

-- 여기서 어떤 문제가 생겨 sp1 이전으로 롤백하고 싶다면
ROLLBACK TO sp1;

-- sp1 이후의 변경 사항은 유지하고 전체 커밋
COMMIT;
```

---

## 6. 한 줄 요약

1. **VIEW** = 가상 테이블 (보안·복잡성 단순화)
2. **INDEX** = 검색 성능 향상 (INSERT/UPDATE overhead 존재)
3. **트랜잭션** = `START TRANSACTION` → 작업 → `COMMIT`/`ROLLBACK`
4. **격리 수준** = READ COMMITTED(기본) / REPEATABLE READ / SERIALIZABLE
5. **SAVEPOINT** = 트랜잭션 내 부분 롤백 지점 생성

---

## [이전: Session 9 — 서브쿼리](unit2_queries/session7.md) · [다음: Session 2 — 숫자 함수](unit3_advanced/session2.md)