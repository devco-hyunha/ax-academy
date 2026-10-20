# Session 6 — 절차형 SQL: 저장 프로시저 & 함수

> 단원: [unit3_advanced — Advanced Topics](#unit3-advanced---advanced-topics)  
> 이전: [Session 5 — Redis](session5.md) · 다음: [Session 7 — 트리거 & 이벤트](session7.md)  
> DBMS: **MySQL 8** 기준 (Oracle PL/SQL 차이는 마지막 절 참고)

---

## 이번 세션 목표

| 목표            | 내용                                            |
| --------------- | ----------------------------------------------- |
| 절차형 SQL 이해 | SQL vs PL/SQL, `DECLARE` → `BEGIN` → `END` 구조 |
| 저장 프로시저   | `CREATE PROCEDURE`, `IN/OUT/INOUT`, `CALL`      |
| 제어 흐름       | `IF`, `CASE`, `WHILE`, `LOOP`, `LEAVE`          |
| 커서 & 예외     | `CURSOR`, `DECLARE ... HANDLER`                 |
| 저장 함수       | `CREATE FUNCTION`, `RETURNS`, `RETURN`          |

---

## 1. 절차형 SQL (Procedural SQL)이란

- 일반 SQL은 **"무엇을 뽑을까"만 선언**하는 **선언적 언어**
- 절차형 SQL은 여기에 **변수·조건분기·반복·예외처리**를 더한 **절차형 언어**
- DB 안에 쿼리를 프로그램처럼 저장해 두고 필요할 때 호출

| 구분      | 일반 SQL             | 절차형 SQL                 |
| --------- | -------------------- | -------------------------- |
| 성격      | 선언적 (What)        | 절차적 (How)               |
| 변수      | 없음                 | `DECLARE`로 선언           |
| 조건/반복 | `CASE`, `WHERE`뿐    | `IF`, `LOOP`, `WHILE`      |
| 재사용    | 매번 쿼리 전체 작성  | `CALL` 한 번으로 실행      |
| 네트워크  | 클라이언트↔서버 왕복 | 서버 내부에서 한 번에 처리 |

### 대표적인 절차형 객체

| 객체          | 이름        | 특징                                             |
| ------------- | ----------- | ------------------------------------------------ |
| 저장 프로시저 | `PROCEDURE` | `CALL`로 호출, 반환값 없음 (OUT 파라미터로 출력) |
| 저장 함수     | `FUNCTION`  | `SELECT` 절에서 사용 가능, **반드시 반환값**     |
| 트리거        | `TRIGGER`   | 이벤트 발생 시 자동 실행 (Session 7)             |

### `DECLARE` → `BEGIN` → `END` 블록 구조 (핵심!)

MySQL의 루틴 본문은 항상 이 형태다.

```sql
DECLARE 변수명 타입 [DEFAULT 기본값];   -- 1) 선언부: 변수·커서·핸들러 선언
BEGIN                                     -- 2) 실행부: 실제 로직
  -- SQL 문장, IF, LOOP ...
END                                       -- 3) 종료부
```

```text
DECLARE  … 변수 선언     ← BEGIN 앞 (한 줄씩)
BEGIN    … 본문 시작
  IF … THEN … END IF;
  LOOP … END LOOP;
  SELECT … ;
END      … 본문 끝
```

> ⚠️ `DECLARE`는 **`BEGIN` 바로 앞 선언부**에만 올 수 있고, `BEGIN` 안쪽에서는 쓸 수 없다.

---

## 2. 저장 프로시저 (Stored Procedure)

### 2-1. `DELIMITER`가 필요한 이유

MySQL 클라이어nt는 **`;`로 문장 끝을 판단**한다. 그런데 프로시저 본문에는 `;`이 여러 개 들어가므로,

문장 구분자를 `$$` 등으로 **일시적으로 바꿔준 뒤** 원래대로 되돌린다.

```sql
DELIMITER $$            -- 구분자를 ; 에서 $$로 변경
CREATE PROCEDURE ...
BEGIN
  ...;                  -- ; 를 써도 문장이 끊기지 않음
END $$                  -- 여기서 끝
DELIMITER ;             -- 구분자 원위치
```

### 2-2. 최소 구조

```sql
DELIMITER $$
CREATE PROCEDURE sp_greet()
BEGIN
  SELECT '안녕하세요' AS 인사;
END $$
DELIMITER ;

CALL sp_greet();
```

### 2-3. 파라미터 — `IN` / `OUT` / `INOUT`

| 키워드        | 의미                   | 프로시저 밖에서               |
| ------------- | ---------------------- | ----------------------------- |
| `IN` (기본값) | 값을 **받아** 사용     | 값을 전달                     |
| `OUT`         | 값을 **밖으로 내보냄** | 변수를 전달 → 실행 후 확인    |
| `INOUT`       | 값 **주고받음**        | 변수 전달 → 실행 후 값이 바뀜 |

```sql
DELIMITER $$
CREATE PROCEDURE sp_raise_salary(
  IN  p_empno INT,        -- 입력: 사번
  IN  p_rate  DOUBLE,     -- 입력: 인상률
  OUT p_new   INT         -- 출력: 인상 후 급여
)
BEGIN
  UPDATE emp
  SET sal = ROUND(sal * p_rate)
  WHERE empno = p_empno;

  SELECT sal INTO p_new
  FROM emp
  WHERE empno = p_empno;
END $$
DELIMITER ;
```

호출 — `OUT`은 **변수**를 넘긴다.

```sql
SET @result = 0;                                   -- 세션 변수
CALL sp_raise_salary(7369, 1.1, @result);          -- SMITH를 10% 인상
SELECT @result;                                    -- 인상 후 급여 확인
```

### 2-4. `SELECT ... INTO 변수`

```sql
SELECT 컬럼 INTO 변수
FROM 테이블
WHERE 조건;

-- 여러 변수에 한번에
SELECT COUNT(*), AVG(sal) INTO @cnt, @avg
FROM emp;
```

---

## 3. 제어 흐름 (조건 · 반복)

### 3-1. `IF ... THEN ... ELSE ... END IF`

```sql
DELIMITER $$
CREATE PROCEDURE sp_grade(IN p_score INT)
BEGIN
  IF p_score >= 90 THEN
    SELECT 'A학점' AS 등급;
  ELSEIF p_score >= 80 THEN
    SELECT 'B학점' AS 등급;
  ELSEIF p_score >= 70 THEN
    SELECT 'C학점' AS 등급;
  ELSE
    SELECT 'F학점' AS 등급;
  END IF;
END $$
DELIMITER ;

CALL sp_grade(85);   -- B학점
```

### 3-2. `CASE ... WHEN ... END CASE`

```sql
CASE p_deptno
  WHEN 10 THEN SELECT '관리부';
  WHEN 20 THEN SELECT '영업부';
  ELSE SELECT '기타';
END CASE;
```

### 3-3. 반복문 — `WHILE` / `LOOP` / `REPEAT`

```sql
-- WHILE: 조건이 참인 동안
DELIMITER $$
CREATE PROCEDURE sp_while_demo(IN p_max INT)
BEGIN
  DECLARE v_i INT DEFAULT 1;
  WHILE v_i <= p_max DO
    SELECT v_i AS 숫자;
    SET v_i = v_i + 1;
  END WHILE;
END $$
DELIMITER ;
```

```sql
-- LOOP + LEAVE ( break 역할 )
DELIMITER $$
CREATE PROCEDURE sp_loop_demo()
BEGIN
  DECLARE v_i INT DEFAULT 1;
  loop_main: LOOP
    IF v_i > 5 THEN
      LEAVE loop_main;      -- 루프 탈출
    END IF;
    SET v_i = v_i + 1;
  END LOOP loop_main;
  SELECT v_i AS 최종값;     -- 6
END $$
DELIMITER ;
```

```sql
-- REPEAT: 조건 만족 전까지 반복 (do-while 형태)
REPEAT
  SET v_i = v_i + 1;
  UNTIL v_i > 5
END REPEAT;
```

### 3-4. 반복문 비교

| 구문                              | 조건 위치           | 형태             |
| --------------------------------- | ------------------- | ---------------- |
| `WHILE ... DO ... END WHILE`      | 진입 시 조건 확인   | while            |
| `REPEAT ... UNTIL ... END REPEAT` | 한 번 실행 후 확인  | do-while         |
| `LOOP ... END LOOP`               | `LEAVE`로 직접 탈출 | 무한루프 + break |

---

## 4. 커서(CURSOR) & 예외 처리(HANDLER)

### 4-1. 커서란

- `SELECT`로 여러 행이 나온 결과를 **한 행씩 순차적으로 읽는 자료 구조**
- 반복문과 짝을 이루어야 한다 (안 그러면 1행에서만 멈춤)

### 4-2. 커서 사용 4단계

```text
1. DECLARE 커서명 CURSOR FOR 조회문;   -- 선언
2. DECLARE CONTINUE HANDLER FOR NOT FOUND ...;  -- 끝 감지
3. OPEN 커서명;                        -- 열기
4. 루프 { FETCH 커서명 INTO 변수; ... }  -- 한 행씩 읽기
   CLOSE 커서명;                       -- 닫기
```

### 4-3. 전체 예시 — 부서별 사원 급여 인상

```sql
DELIMITER $$
CREATE PROCEDURE sp_dept_raise(
  IN p_deptno INT,
  IN p_rate   DOUBLE
)
BEGIN
  DECLARE v_empno INT;
  DECLARE v_sal   INT;
  DECLARE v_done  INT DEFAULT 0;

  -- 1) 커서 선언
  DECLARE cur_emp CURSOR FOR
    SELECT empno, sal FROM emp WHERE deptno = p_deptno;

  -- 2) 더 이상 행이 없으면 v_done = 1 로 변경 후 루프 탈출
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = 1;

  -- 3) 열기
  OPEN cur_emp;

  -- 4) 반복 조회
  read_loop: LOOP
    FETCH cur_emp INTO v_empno, v_sal;
    IF v_done = 1 THEN
      LEAVE read_loop;
    END IF;

    UPDATE emp
    SET sal = ROUND(v_sal * p_rate)
    WHERE empno = v_empno;
  END LOOP read_loop;

  CLOSE cur_emp;

  SELECT CONCAT(p_deptno, '번 부서 인상 완료') AS 결과;
END $$
DELIMITER ;

CALL sp_dept_raise(10, 1.05);
```

### 4-4. 예외 핸들러 (예외 처리)

```sql
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION     -- 오류 발생 시
BEGIN
  ROLLBACK;                                    -- 복구
  SET @err = '작업 실패';
END;

DECLARE CONTINUE HANDLER FOR NOT FOUND        -- 행 없음
SET v_done = 1;

DECLARE EXIT HANDLER FOR SQLEXCEPTION         -- EXIT = 즉시 중단
BEGIN
  ROLLBACK;
  RESIGNAL;                                    -- 오류를 상위로 재전파
END;
```

| 핸들러 타입    | 의미                                   |
| -------------- | -------------------------------------- |
| `CONTINUE`     | 처리 후 **계속 진행**                  |
| `EXIT`         | **즉시 종료** (실행부에서 빠져나감)    |
| `NOT FOUND`    | `SELECT INTO` / `FETCH`가 행을 못 찾음 |
| `SQLEXCEPTION` | 일반 SQL 오류                          |
| `SQLWARNING`   | 경고 (경미한 오류)                     |

---

## 5. 저장 함수 (Stored Function)

프로시저와 달리 **`SELECT` 절 안에서 직접 호출**할 수 있고 **반드시 반환값**이 있어야 한다.

```sql
DELIMITER $$
CREATE FUNCTION fn_annual_sal(p_sal INT, p_comm INT)
RETURNS INT                              -- 반환 타입
DETERMINISTIC                            -- 같은 입력 → 같은 출력 (MySQL 요구 선언)
BEGIN
  DECLARE v_annual INT;
  SET v_annual = (p_sal + IFNULL(p_comm, 0)) * 12;
  RETURN v_annual;                       -- 반환은 RETURN
END $$
DELIMITER ;

-- 함수는 SELECT에서 그대로 사용 가능
SELECT ename, sal, fn_annual_sal(sal, IFNULL(comm, 0)) AS 연봉
FROM emp;
```

---

## 6. 프로시저 vs 함수 비교

| 구분             | `PROCEDURE`           | `FUNCTION`                             |
| ---------------- | --------------------- | -------------------------------------- |
| 호출             | `CALL sp_name(...)`   | `SELECT fn_name(...)`, SQL식 안에서    |
| 반환값           | 없음 (`OUT`으로 출력) | **필수** (`RETURN`)                    |
| `SELECT` 절 사용 | 불가                  | **가능**                               |
| DML 실행         | 가능                  | 기본적으로 **불가** (속성에 따라 제한) |
| 주 용도          | 갱신·복잡한 처리 흐름 | 계산 결과를 쿼리에 조인                |
| 반환 선언        | `OUT` 파라미터        | `RETURNS 타입`                         |

---

## 7. 관리 문장

```sql
-- 조회
SHOW PROCEDURE STATUS;
SHOW FUNCTION STATUS;
SHOW CREATE PROCEDURE sp_dept_raise;

-- 삭제
DROP PROCEDURE IF EXISTS sp_dept_raise;
DROP FUNCTION  IF EXISTS fn_annual_sal;

-- 목록 조회 (information_schema)
SELECT ROUTINE_NAME, ROUTINE_TYPE
FROM information_schema.ROUTINES
WHERE ROUTINE_SCHEMA = 'hh';
```

---

## 8. Oracle PL/SQL과의 차이

| 항목           | MySQL                               | Oracle                                       |
| -------------- | ----------------------------------- | -------------------------------------------- |
| 선언·실행 블록 | `BEGIN ... END` (선언은 `BEGIN` 앞) | `DECLARE ... BEGIN ... END`                  |
| 문장 구분자    | `DELIMITER` 변경 필요               | `/`로 구분                                   |
| 호출           | `CALL sp(...)`                      | `EXECUTE sp(...)` 또는 `BEGIN sp(...); END;` |
| 반복           | `WHILE` / `LOOP` / `REPEAT`         | `FOR ... LOOP` 중심                          |
| 함수 선언      | `RETURNS 타입` + `RETURN`           | `RETURN 타입` + `RETURN`                     |
| 변수 기본값    | `DEFAULT`                           | `:=`                                         |

```sql
-- Oracle 스타일 예시 (참고)
CREATE OR REPLACE PROCEDURE raise_salary(p_empno IN NUMBER) IS
  v_sal NUMBER;
BEGIN
  SELECT sal INTO v_sal FROM emp WHERE empno = p_empno;
  UPDATE emp SET sal = sal * 1.1 WHERE empno = p_empno;
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE('사원 없음');
END;
/
```

---

## 9. 실습 문제

```sql
-- 1. 사번을 입력하면 이름과 급여를 출력하는 프로시저 sp_emp_info를 작성하라.
DELIMITER $$
CREATE PROCEDURE sp_emp_info(IN p_empno INT)
BEGIN
  SELECT ename, sal, job
  FROM emp
  WHERE empno = p_empno;
END $$
DELIMITER ;
CALL sp_emp_info(7369);

-- 2. 부서번호를 입력하면 해당 부서의 사원 수를 OUT 변수로 돌려주는 sp_count_emp를 작성하라.
DELIMITER $$
CREATE PROCEDURE sp_count_emp(IN p_deptno INT, OUT p_cnt INT)
BEGIN
  SELECT COUNT(*) INTO p_cnt
  FROM emp
  WHERE deptno = p_deptno;
END $$
DELIMITER ;
SET @cnt = 0;
CALL sp_count_emp(30, @cnt);
SELECT @cnt;

-- 3. 점수를 입력하면 학점을 출력하는 sp_grade를 IF 문으로 작성하라 (90/A, 80/B, 70/C, 그 외 F).
DELIMITER $$
CREATE PROCEDURE sp_grade(IN p_score INT)
BEGIN
  IF p_score >= 90 THEN SELECT 'A' AS 학점;
  ELSEIF p_score >= 80 THEN SELECT 'B' AS 학점;
  ELSEIF p_score >= 70 THEN SELECT 'C' AS 학점;
  ELSE SELECT 'F' AS 학점;
  END IF;
END $$
DELIMITER ;
CALL sp_grade(85);

-- 4. 1부터 N까지 합을 구하는 sp_sum을 WHILE 문으로 작성하라.
DELIMITER $$
CREATE PROCEDURE sp_sum(IN p_n INT)
BEGIN
  DECLARE v_i INT DEFAULT 1;
  DECLARE v_total INT DEFAULT 0;
  WHILE v_i <= p_n DO
    SET v_total = v_total + v_i;
    SET v_i = v_i + 1;
  END WHILE;
  SELECT v_total AS '1부터 N까지의 합';
END $$
DELIMITER ;
CALL sp_sum(100);   -- 5050

-- 5. 커서를 사용해 모든 사원의 이름을 한 행씩 출력하는 sp_list_emp를 작성하라.
DELIMITER $$
CREATE PROCEDURE sp_list_emp()
BEGIN
  DECLARE v_ename VARCHAR(10);
  DECLARE v_done INT DEFAULT 0;
  DECLARE cur_emp CURSOR FOR SELECT ename FROM emp;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = 1;

  OPEN cur_emp;
  list_loop: LOOP
    FETCH cur_emp INTO v_ename;
    IF v_done = 1 THEN LEAVE list_loop; END IF;
    SELECT v_ename AS 사원명;
  END LOOP list_loop;
  CLOSE cur_emp;
END $$
DELIMITER ;
CALL sp_list_emp();

-- 6. 부서번호와 인상률을 입력받아 해당 부서 전체 급여를 인상하는 sp_dept_raise를 작성하라.
-- (4번 예제의 sp_dept_raise를 그대로 사용)
CALL sp_dept_raise(20, 1.10);

-- 7. 급여와 커미션을 입력하면 연봉을 돌려주는 함수 fn_annual을 작성하고 SELECT에서 호출하라.
DELIMITER $$
CREATE FUNCTION fn_annual(p_sal INT, p_comm INT)
RETURNS INT
DETERMINISTIC
BEGIN
  RETURN (p_sal + IFNULL(p_comm, 0)) * 12;
END $$
DELIMITER ;
SELECT ename, fn_annual(sal, IFNULL(comm, 0)) AS 연봉 FROM emp;

-- 8. sp_count_emp의 결과를 확인하는 쿼리를 작성하라.
SET @total = 0;
CALL sp_count_emp(10, @total);
SELECT @total AS '10번 부서 사원 수';

-- 9. 생성한 프로시저 목록을 조회하라.
SHOW PROCEDURE STATUS WHERE Db = 'hh';

-- 10. sp_grade를 삭제하라.
DROP PROCEDURE IF EXISTS sp_grade;
```

---

## 한 줄 요약

1. **절차형 SQL** = SQL에 변수·조건·반복·예외를 더한 서버 측 프로그래밍
2. 기본 블록 = **`DECLARE`(선언) → `BEGIN`(실행) → `END`(종료)**
3. MySQL은 본문 내 `;` 때문에 **`DELIMITER` 변경 필수**
4. **`IN`/`OUT`/`INOUT`** = 입력 / 출력 / 입출력 파라미터
5. **`SELECT ... INTO 변수`**, **`CALL`**로 프로시저 호출
6. **커서** = 여러 행을 한 행씩 (`FETCH`), 끝이면 `NOT FOUND` 핸들러로 탈출
7. **함수는 `RETURNS` + `RETURN`**, `SELECT` 절에서 직접 사용 가능

---

[이전: Session 5 — Redis](session5.md) · [다음: Session 7 — 트리거 & 이벤트](session7.md)
