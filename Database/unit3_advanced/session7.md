# Session 7 — 트리거(TRIGGER) & 이벤트(EVENT)

> 단원: [unit3_advanced — Advanced Topics](#unit3-advanced---advanced-topics)  
> 이전: [Session 6 — 절차형 SQL (프로시저 · 함수)](session6.md) · 다음: [Review — SQL 질의어 종합 복습](../review.md)  
> DBMS: **MySQL 8** 기준 · 선행 학습: Session 6의 `BEGIN`~`END`, `DECLARE`

---

## 이번 세션 목표

| 목표        | 내용                                    |
| ----------- | --------------------------------------- |
| 트리거 이해 | 자동 실행 원리, `BEFORE` / `AFTER`      |
| 트리거 작성 | `CREATE TRIGGER`, `NEW` / `OLD` 참조    |
| 실전 적용   | 감사 로그, 재고 자동 감소, 값 자동 보정 |
| 트리거 관리 | `SHOW`, `DROP`, 장단점·주의사항         |
| 이벤트      | `CREATE EVENT`로 예약 작업 실행         |

---

## 1. 트리거(TRIGGER)란

- **특정 DML 이벤트(`INSERT`, `UPDATE`, `DELETE`)가 발생하면 자동으로 실행**되는 절차형 블록
- 이름 그대로 "방아쇠" — 개발자가 직접 호출하지 않아도 DB가 대신 실행
- Session 6의 프로시저와 본문 구조(`DECLARE` → `BEGIN` → `END`)가 **동일**하고,
  **호출 시점이 다를 뿐**(호출 → 자동 실행)

| 구분        | 프로시저                      | 트리거                       |
| ----------- | ----------------------------- | ---------------------------- |
| 실행 시점   | 개발자가 `CALL`로 명시적 호출 | DML 발생 시 **자동 실행**    |
| 호출        | 가능                          | **호출 불가** (자동)         |
| `NEW`/`OLD` | 없음                          | **사용 가능** (변경 전후 값) |
| 반환        | `OUT` 파라미터                | 없음 (실행 결과만)           |

### 실행 시점 구분

| 키워드          | 의미                                    |
| --------------- | --------------------------------------- |
| `BEFORE INSERT` | 삽입 **전** 실행 → 값 보정, 검증        |
| `AFTER INSERT`  | 삽입 **후** 실행 → 로그 기록, 연동 갱신 |
| `BEFORE UPDATE` | 갱신 **전** 실행                        |
| `AFTER UPDATE`  | 갱신 **후** 실행                        |
| `BEFORE DELETE` | 삭제 **전** 실행 → 삭제 차단 검증       |
| `AFTER DELETE`  | 삭제 **후** 실행 → 로그 기록            |

---

## 2. `NEW`와 `OLD` (트리거 전용 참조 값)

| 이벤트   | `NEW`            | `OLD`          |
| -------- | ---------------- | -------------- |
| `INSERT` | 삽입될 **새 행** | — (없음)       |
| `UPDATE` | 갱신 **후** 값   | 갱신 **전** 값 |
| `DELETE` | — (없음)         | 삭제될 **행**  |

```sql
-- UPDATE 트리거에서 급여 변경 전후를 비교
IF NEW.sal <> OLD.sal THEN
  -- 급여가 실제로 바뀐 경우
END IF;
```

---

## 3. 트리거 작성 문법

```sql
DELIMITER $$
CREATE TRIGGER 트리거명
{BEFORE | AFTER} {INSERT | UPDATE | DELETE}
ON 테이블명
FOR EACH ROW          -- MySQL은 행 단위만 지원 (ROW 단위)
BEGIN
  -- 절차형 SQL 본문
END $$
DELIMITER ;
```

> MySQL은 **트리거가 테이블당 트리거 종류별 최대 1개씩**만 정의 가능하며,
> `BEFORE` 트리거는 `NEW` 값 변경이 가능하고, `AFTER` 트리거는 변경이 불가능하다.

---

## 4. 실전 예제

### 4-1. 감사 로그 — `AFTER UPDATE`

급여가 바뀐 기록을 별도 테이블에 남긴다.

```sql
-- 로그 테이블
CREATE TABLE emp_audit (
  id         INT PRIMARY KEY AUTO_INCREMENT,
  empno      INT,
  old_sal    INT,
  new_sal    INT,
  changed_at DATETIME DEFAULT NOW()
);

-- 트리거
DELIMITER $$
CREATE TRIGGER trg_emp_sal_audit
AFTER UPDATE ON emp
FOR EACH ROW
BEGIN
  IF NEW.sal <> OLD.sal THEN
    INSERT INTO emp_audit (empno, old_sal, new_sal)
    VALUES (OLD.empno, OLD.sal, NEW.sal);
  END IF;
END $$
DELIMITER ;

-- 동작 확인
UPDATE emp SET sal = sal + 100 WHERE empno = 7369;
SELECT * FROM emp_audit;
-- SMITH의 급여 변동 내역이 자동 기록됨
```

### 4-2. 값 자동 보정 — `BEFORE INSERT`

음수 급여가 들어가지 않도록 삽입 전에 막는다.

```sql
DELIMITER $$
CREATE TRIGGER trg_emp_sal_check
BEFORE INSERT ON emp
FOR EACH ROW
BEGIN
  IF NEW.sal < 0 THEN
    SET NEW.sal = 0;                     -- NEW 값 변경 가능 (BEFORE 전용)
  END IF;
END $$
DELIMITER ;
```

### 4-3. 재고 자동 감소 — `AFTER INSERT`

주문이 들어오면 상품 재고를 자동으로 깎는다.

```sql
CREATE TABLE product (
  id    INT PRIMARY KEY AUTO_INCREMENT,
  name  VARCHAR(50),
  stock INT NOT NULL DEFAULT 0
);

CREATE TABLE orders (
  id      INT PRIMARY KEY AUTO_INCREMENT,
  prod_id INT,
  qty     INT,
  FOREIGN KEY (prod_id) REFERENCES product(id)
);

DELIMITER $$
CREATE TRIGGER trg_stock_decrease
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE product
  SET stock = stock - NEW.qty
  WHERE id = NEW.prod_id;
END $$
DELIMITER ;
```

### 4-4. 삭제 차단 — `BEFORE DELETE`

특정 조건의 행은 삭제하지 못하게 한다.

```sql
DELIMITER $$
CREATE TRIGGER trg_emp_delete_block
BEFORE DELETE ON emp
FOR EACH ROW
BEGIN
  IF OLD.job = 'PRESIDENT' THEN
    SIGNAL SQLSTATE '45000'              -- 사용자 정의 오류 발동
    SET MESSAGE_TEXT = '대표 사원은 삭제할 수 없습니다.';
  END IF;
END $$
DELIMITER ;

-- DELETE FROM emp WHERE empno = 7839;  → 오류 발생 후 중단
```

### 4-5. `BEFORE UPDATE` — 변경 시각 자동 기록

```sql
DELIMITER $$
CREATE TRIGGER trg_post_updated_at
BEFORE UPDATE ON post
FOR EACH ROW
BEGIN
  SET NEW.updated_at = NOW();            -- 수정 시각 자동 갱신
END $$
DELIMITER ;
```

---

## 5. 트리거 관리

```sql
-- 목록 조회
SHOW TRIGGERS;

-- 특정 테이블 트리거만 조회
SHOW TRIGGERS LIKE 'emp';

-- 생성 코드 확인
SHOW CREATE TRIGGER trg_emp_sal_audit;

-- 삭제
DROP TRIGGER IF EXISTS trg_emp_sal_audit;

-- 목록 조회 (information_schema)
SELECT TRIGGER_NAME, EVENT_MANIPULATION, EVENT_OBJECT_TABLE
FROM information_schema.TRIGGERS
WHERE TRIGGER_SCHEMA = 'hh';
```

---

## 6. 트리거의 장단점 · 주의사항

| 장점                                                    | 단점/주의                                                |
| ------------------------------------------------------- | -------------------------------------------------------- |
| 비즈니스 규칙을 **DB 수준에서 강제** (앱이 달라도 동일) | **누가 실행했는지 파악 어려움** (암묵적 실행)            |
| 로그·감사 자동화, 무결성 유지                           | 다른 DML을 유발하면 **체인 실행** → 성능·디버깅 난이도 ↑ |
| 애플리케이션 중복 코드 제거                             | 디버깅이 어렵고, 예상치 못한 트리거가 병목 초래          |
| 트랜잭션 안에서 함께 커밋/롤백                          | 대량 갱신 시 트리거도 함께 실행되어 **속도 저하**        |

> **설계 원칙**: 로그 기록·값 보정·연동 갱신처럼 **DB가 보장해야 할 규칙**에만 쓰고,
> 복잡한 비즈니스 흐름은 프로시저나 애플리케이션 레벨에서 처리하는 것이 좋다.

---

## 7. 이벤트(EVENT) — 예약 실행

트리거가 **DML에 반응**한다면, 이벤트는 **정해진 시각에 자동 실행**된다.
(스케줄러 — 야간 집계, 만료 데이터 정리 등)

```sql
-- 이벤트 스케줄러 활성화 (한 번)
SET GLOBAL event_scheduler = ON;

-- 매일 자정에 오래된 로그 삭제
DELIMITER $$
CREATE EVENT evt_cleanup_log
ON SCHEDULE EVERY 1 DAY
STARTS '2026-10-17 00:00:00'
DO
BEGIN
  DELETE FROM emp_audit WHERE changed_at < NOW() - INTERVAL 1 YEAR;
END $$
DELIMITER ;
```

```sql
-- 관리
SHOW EVENTS;
DROP EVENT IF EXISTS evt_cleanup_log;
```

| 구분      | 트리거            | 이벤트                        |
| --------- | ----------------- | ----------------------------- |
| 실행 조건 | DML 발생 시       | **시각 기준** (즉시/1회/주기) |
| 예시      | 주문 시 재고 감소 | 매일 자정 로그 정리           |

---

## 8. 실습 문제

```sql
-- 1. emp 테이블에 삭제가 발생하면 로그를 남기는 emp_delete_log(empno, deleted_at) 테이블과
--    AFTER DELETE 트리거 trg_emp_delete를 작성하라.
CREATE TABLE emp_delete_log (
  id         INT PRIMARY KEY AUTO_INCREMENT,
  empno      INT,
  ename      VARCHAR(10),
  deleted_at DATETIME DEFAULT NOW()
);

DELIMITER $$
CREATE TRIGGER trg_emp_delete
AFTER DELETE ON emp
FOR EACH ROW
BEGIN
  INSERT INTO emp_delete_log (empno, ename)
  VALUES (OLD.empno, OLD.ename);
END $$
DELIMITER ;

DELETE FROM emp WHERE empno = 9999;
SELECT * FROM emp_delete_log;

-- 2. 급여가 1000 미만으로 입력되면 1000으로 조정하는 BEFORE INSERT 트리거를 작성하라.
DELIMITER $$
CREATE TRIGGER trg_sal_min
BEFORE INSERT ON emp
FOR EACH ROW
BEGIN
  IF NEW.sal < 1000 THEN
    SET NEW.sal = 1000;
  END IF;
END $$
DELIMITER ;

-- 3. 게시글(post)이 삭제되면 조회수 로그를 남기는 AFTER DELETE 트리거를 작성하라.
DELIMITER $$
CREATE TRIGGER trg_post_delete
AFTER DELETE ON post
FOR EACH ROW
BEGIN
  INSERT INTO emp_delete_log (empno, ename)
  VALUES (OLD.id, CONCAT('POST:', OLD.title));
END $$
DELIMITER ;

-- 4. 생성된 트리거 목록을 조회하라.
SHOW TRIGGERS;

-- 5. trg_sal_min 트리거를 삭제하라.
DROP TRIGGER IF EXISTS trg_sal_min;

-- 6. 1년 이상 된 emp_audit 로그를 매일 정리하는 이벤트 evt_audit_cleanup을 작성하라.
DELIMITER $$
CREATE EVENT evt_audit_cleanup
ON SCHEDULE EVERY 1 DAY
DO
BEGIN
  DELETE FROM emp_audit WHERE changed_at < NOW() - INTERVAL 1 YEAR;
END $$
DELIMITER ;

-- 7. emp_sal_audit 트리거를 사용해 emp의 특정 사원 급여를 인상하고,
--    로그에 자동 기록되었는지 확인하는 쿼리를 작성하라.
UPDATE emp SET sal = sal + 500 WHERE empno = 7499;
SELECT * FROM emp_audit WHERE empno = 7499;

-- 8. 트리거 생성문을 확인하는 SQL을 작성하라.
SHOW CREATE TRIGGER trg_emp_sal_audit;
```

---

## 한 줄 요약

1. **트리거** = `INSERT`/`UPDATE`/`DELETE` 시 **자동 실행**되는 `BEGIN`~`END` 블록
2. **`BEFORE`** = 값 보정·검증 (`NEW` 수정 가능), **`AFTER`** = 로그·연동 갱신
3. **`NEW`** = 변경 후 값, **`OLD`** = 변경 전 값
4. 본문 구조는 프로시저와 동일 — **`DECLARE` → `BEGIN` → `END`**
5. **`SIGNAL`**로 트리거 내에서 오류 발생 가능
6. **이벤트**는 시각 기준 예약 실행, 트리거는 이벤트 기준 자동 실행

---

[이전: Session 6 — 절차형 SQL (프로시저 · 함수)](session6.md) · [다음: Review — SQL 질의어 종합 복습](../review.md)
