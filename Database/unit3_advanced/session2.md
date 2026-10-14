# Session 2 — 데이터 무결성(integrity) 보장

> 단원: [unit3_advanced — Advanced Topics](#unit3-advanced---advanced-topics)  
> 이전: [Session 1 — RDB 특징](unit3_advanced/session1.md) · 다음: [Session 3 — 정규화](unit3_advanced/session3.md)

## 1. 데이터 무결성(Data Integrity)이란

- **데이터의 정확성과 일관성을 유지**하기 위해 제공하는 제약 조건
- 트랜잭션 실패로 인한 데이터 손실 방지, 비즈니스 규칙 준수 보장

## 2. 무결성 제약 조건의 종류

### 1) 개체 무결성(Entity Integrity)
- **기본키(PK)** 설정 필수
- 기본키는 **절대 NULL이거나 중복되면 안 된다**
- 튜블(행)을 uniquely 식별하는 역할
- `PRIMARY KEY`_constraint 적용

### 2) 참조 무결성(Referential Integrity)
- **외래키(FK)** 제약 조건
- 외래키는 **참조하는 테이블에 존재하는 값이어야 한다**
- orphan record(참조하지 않는 행) 방지
- `FOREIGN KEY`_constraint 적용
- 부모 테이블 삭제 시 자식 테이블 처리 옵션: CASCADE, SET NULL, RESTRICT 등

### 3) 도메인 무결성(Domain Integrity)
- 각 **컬럼의 값**은 미리 정의된 데이터 타입, 범위 따라야 함
- `NOT NULL`, `UNIQUE`, `CHECK` 제약 조건 적용
- 예: 나이 컬럼은 0 이상, 이메일 형식 검사, 가격은 음수 불가 등

## 3. 정리

1. 무결성: 데이터 정확성과 일관성 유지 위해 제공하는 제약 조건
2. 개체 무결성: 기본키가 NULL 또는 중복되지 않음 (PRIMARY KEY)
3. 참조 무결성: 외래키가 참조 테이블에 존재해야 함 (FOREIGN KEY)
4. 도메인 무결성: 컬럼 값은 데이터 타입, 범위 제한 (NOT NULL, CHECK, UNIQUE)

---

## 이번 세션 목표

| 목표 | 내용 |
| ---- | ---- |
| 대표 숫자 함수 | `ABS`, `MOD`, `ROUND`, `CEIL`, `FLOOR` |
| 숫자 형태 변환 | `TRUNC`, `SIGN` (MySQL 기준 주요 함수) |
| 고급 함수 | `SIN`, `COS`, `TAN`, `BIT_COUNT`, 해시 함수 |
| 실전 적용 | 산술 연산과 함수 조합 |

---

## 1. 주요 숫자 함수

| 함수 | 의미 | 예 |
| ---- | ---- | ---- |
| `ABS(num)` | 절댓값 (음수 → 양수 변환) | `ABS(-10)` → `10` |
| `MOD(m, n)` | 나머지 연산 (`m % n`) | `MOD(17, 5)` → `2` |
| `ROUND(num, d)` | 소수점 `d`자리에서 반올림 | `ROUND(3.14159, 2)` → `3.14` |
| `CEIL(num)` | 올림 (가장 가까운 큰 정수) | `CEIL(3.2)` → `4` |
| `FLOOR(num)` | 내림 (가장 가까운 작은 정수) | `FLOOR(3.9)` → `3` |
| `SIGN(num)` | 부호 반환: `1`(양수), `-1`(음수), `0`(0) | `SIGN(-5)` → `-1` |
| `POWER(b, e)` | 제곱 (`b`의 `e`제) | `POWER(2, 10)` → `1024` |
| `SQRT(n)` | 제곱근 | `SQRT(16)` → `4` |
| `SIN(n)` | 사인 (라디안) | `SIN(PI()/2)` → `1` |
| `COS(n)` | 코사인 (라디안) | `COS(0)` → `1` |
| `TAN(n)` | 탄젠트 (라디안) | `TAN(PI()/4)` → `1` |
| `BIT_COUNT(n)` | 비트 인구수 (1의 개수) | `BIT_COUNT(15)` → `4` (이진수 1111) |
| `MD5(expr)` | MD5 해시 함수 | `MD5('hello')` → `5d41402abc4b2a76b9719d911017c592` |
| `SHA1(expr)` | SHA1 해시 함수 | `SHA1('hello')` → `aaf4c6cddc93f3f9846d89635f5e7c9e4f89a1b1` |

### (참고) 기타 함수

| 함수 | 의미 | 비고 |
| ---- | ---- | ---- |
| `SIGN(num)` | 부호 반환: `1`(양수), `-1`(음수), `0`(0) | `SIGN(-5)` → `-1` |
| `POWER(b, e)` | 제곱 (`b`의 `e`제) | `POWER(2, 10)` → `1024` |
| `SQRT(n)` | 제곱근 | `SQRT(16)` → `4` |

---

## 2. 실습 예제

### 2.1 기본 산술 + 함수 조합

```sql
-- 사원의 급여에 10% 인상 후 반올림한 값
SELECT ename, sal, ROUND(sal * 1.1, 2) AS "인상 후 급여"
FROM emp;
```

### 2.2 나머지 연산 및 부호 확인

```sql
-- 사원 번호가 홀수인지 확인 (MOD 사용)
SELECT empno, ename
FROM emp
WHERE MOD(empno, 2) = 1;

-- 급여가 0보다 큰 사원 수 확인 (SIGN 사용)
SELECT COUNT(*) AS 양수사원수
FROM emp
WHERE SAL > 0;
```

### 2.3 제곱 및 제곱근

```sql
-- 2의 8제곱
SELECT POWER(2, 8) FROM dual;

-- 144의 제곱근
SELECT SQRT(144) FROM dual;
```

---

## 3. 실습 문제

```sql
-- 1. 절댓값을 구하는 함수 ABS를 사용하여 -100의 결과를 검색하라.
SELECT ABS(-100);

-- 2. 17을 5로 나눈 나머지를 구하는 MOD 함수를 검색하라.
SELECT MOD(17, 5) FROM dual;

-- 3. 소수점 둘째 자리까지 반올림하는 ROUND 함수를 사용하여
--    3.141592를 검색하라.
SELECT ROUND(3.141592, 2) FROM dual;

-- 4. 3.7을 올림(Ceil)하는 값을 검색하라.
SELECT CEIL(3.7) FROM dual;

-- 5. 3.2를 내림(Floor)하는 값을 검색하라.
SELECT FLOOR(3.2) FROM dual;

-- 7. 사원들의 급여 평균의 소수점 셋째 자리까지 반올림한 값을 검색하라.
SELECT ROUND(AVG(sal), 3) FROM emp;

-- 8. 사원의 급여를 10% 인사한 후 소수점 둘째 자리에서 반올림한 값을 검색하라.
SELECT ename, ROUND(sal * 1.1, 2) AS "인상후급여" FROM emp;

-- 9. 원주율을 검색하라. (PI 함수 사용)
SELECT PI() FROM dual;

-- 10. 사원의 사원번호의 비트 인구수(1의 개수)를 검색하라.
SELECT empno, BIT_COUNT(empno) FROM emp;

-- 11. 사원명의 MD5 해시 값을 검색하라.
SELECT ename, MD5(ename) FROM emp;

-- 12. 사원명의 SHA1 해시 값을 검색하라.
SELECT ename, SHA1(ename) FROM emp;

-- 13. 사원번호가 홀수인 사원들의 사원번호와 사원번호를 검색하라.
SELECT empno, ename
FROM emp
WHERE MOD(empno, 2) = 1;

-- 61. 학생의 학번, 이름, 신장을 검색하라. (신장은 첫번째 자리에서 반올림함)
SELECT stu_no, stu_name, ROUND(stu_height, 0) FROM student;

-- 62. 학생의 학번, 이름, 신장을 검색하라. (신장은 두번째 자리에서 절삭함)
SELECT stu_no, stu_name, TRUNC(stu_height, 1) FROM student;

-- 63. 체중을 30으로 나눈 나머지를 검색하라.
SELECT MOD(stu_weight, 30) FROM student;
```

---

## 4. 한 줄 요약

1. **ABS** = 절댓값, **MOD** = 나머지 연산
2. **ROUND** = 반올림, **CEIL** = 올림, **FLOOR** = 내림
3. **SIGN** = 숫자의 부호 확인 (`1`, `-1`, `0`)
4. **POWER**, **SQRT** = 제곱 및 제곱근 연산
5. **SIN**, **COS**, **TAN** = 삼각함수 (라디안)
6. **BIT_COUNT** = 비트 인구수 (1의 개수)
7. **MD5**, **SHA1** = 해시 함수
8. 숫자 함수는 `SELECT` 절에서 주로 사용하며, `WHERE` 절에서도 필터링 가능

---

## [이전: Session 1 — 뷰 · 인덱스 · 트랜잭션](unit3_advanced/session1.md) · [다음: Session 3 — 날짜 함수](unit3_advanced/session3.md)