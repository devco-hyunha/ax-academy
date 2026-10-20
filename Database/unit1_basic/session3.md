# Session 3 — DML & DDL 변경 · DCL

> 단원: [unit1_basic — Basic Theory & DDL](#unit1-basic---basic-theory--ddl)  
> 이전: [Session 2 — DDL 실습](unit1_basic/session2.md) · 다음: [Session 1 — SELECT 기초](../unit2_queries/session1.md)  
> 전제: Session 2의 `student` / `subject` / `enrol` 테이블이 있어야 한다.

```sql
USE hh;
```

---

## 이번 세션 목표

| 목표        | 내용                                          |
| ----------- | --------------------------------------------- |
| 데이터 삽입 | `INSERT` (단건, 다중 행, `INSERT ... SELECT`) |
| 데이터 갱신 | `UPDATE`, 다중 테이블 갱신                    |
| 데이터 삭제 | `DELETE`, `TRUNCATE` 차이                     |
| 테이블 변경 | `ALTER TABLE` (컬럼 추가/수정/삭제)           |
| 계정·권한   | `CREATE USER`, `GRANT`, `REVOKE`              |

---

## 1. DML이란

**DML (Data Manipulation Language)** = 테이블 안의 **데이터(행)를 다루는 명령어**

| 분류 | 명령어   | 의미               |
| ---- | -------- | ------------------ |
| 조회 | `SELECT` | 행 읽기 (READ)     |
| 삽입 | `INSERT` | 행 넣기 (CREATE)   |
| 갱신 | `UPDATE` | 행 수정 (UPDATE)   |
| 삭제 | `DELETE` | 행 지우기 (DELETE) |

> **DDL vs DML 구분**
>
> - DDL: 구조(테이블)를 만든다 → `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
> - DML: 데이터(행)를 다룬다 → `INSERT`, `UPDATE`, `DELETE`, `SELECT`
> - DML은 대부분 **자동 커밋되지 않으므로** 명시적 `COMMIT`이 필요할 수 있음 (MySQL MyISAM 제외)

---

## 2. INSERT — 데이터 삽입

### 2-1. 전체 컬럼 삽입

```sql
INSERT INTO 테이블명 VALUES (값1, 값2, ...);
```

```sql
INSERT INTO subject VALUES ('115', '자료구조', '한지영', 2, '컴퓨터정보');
```

### 2-2. 특정 컬럼만 지정 (권장)

```sql
INSERT INTO 테이블명 (컬럼1, 컬럼2) VALUES (값1, 값2);
```

```sql
-- 지정하지 않은 컬럼은 NULL 또는 기본값이 들어간다
INSERT INTO student (stu_no, stu_name, stu_dept) VALUES (20150001, '홍길동', '컴퓨터정보');
```

### 2-3. 다중 행 삽입 (한 번에 여러 행)

```sql
INSERT INTO 테이블명 (컬럼...) VALUES
  (값...),
  (값...),
  (값...);
```

```sql
INSERT INTO subject (sub_no, sub_name, sub_prof, sub_grade, sub_dept) VALUES
  ('116', '알고리즘', '이재영', 3, '컴퓨터정보'),
  ('117', '운영체제', '강석현', 3, '컴퓨터정보'),
  ('118', '네트워크', '정순정', 2, '전기전자');
```

### 2-4. 조회 결과를 그대로 삽입 (`INSERT ... SELECT`)

```sql
INSERT INTO 테이블명 (컬럼...)
SELECT 조회문;
```

```sql
-- 2학년 학생만 따로 별도 테이블에 복사
CREATE TABLE student_2nd (
  stu_no CHAR(9),
  stu_name VARCHAR(12),
  stu_dept VARCHAR(20)
);

INSERT INTO student_2nd (stu_no, stu_name, stu_dept)
SELECT stu_no, stu_name, stu_dept
FROM student
WHERE stu_grade = 2;

SELECT * FROM student_2nd;
```

### 2-5. 기본값·현재 시각 채우기

```sql
INSERT INTO post (title, content, user_id)
VALUES ('첫 글', '안녕하세요', 1);
-- created_at은 DATETIME DEFAULT CURRENT_TIMESTAMP에 의해 자동 채움

INSERT INTO post (title, content, user_id, views)
VALUES ('조회수 지정', '본문', 1, 0);   -- DEFAULT 명시적으로 지정
```

---

## 3. UPDATE — 데이터 갱신

### 3-1. 기본 형식

```sql
UPDATE 테이블명
SET 컬럼1 = 값1, 컬럼2 = 값2
WHERE 조건;
```

```sql
-- 박희철 학생의 학과를 '컴퓨터정보'로 변경
UPDATE student
SET stu_dept = '컴퓨터정보'
WHERE stu_name = '박희철';
```

> ⚠️ **주의: `WHERE`를 빼면 모든 행이 갱신된다.**
>
> ```sql
> UPDATE student SET stu_grade = 1;   -- 전체 행이 1학년이 되어버림
> ```

### 3-2. 서브쿼리로 갱신

```sql
-- 과목명이 '자료구조'인 과목의 대상학년을 4로 변경
UPDATE subject
SET sub_grade = 4
WHERE sub_name = '자료구조';
```

### 3-3. 다른 테이블 값을 참조해 갱신 (MySQL 문법)

```sql
-- SCOTT 스키마 예: 30번 부서 사원의 부서명을 10번 부서명으로 변경하지 말고,
-- 자기 자신의 컬럼 기준으로 계산 갱신하는 예
UPDATE emp
SET sal = sal * 1.05
WHERE deptno = 30;
```

### 3-4. 조건부 갱신 (`CASE` 활용)

```sql
UPDATE emp
SET sal = CASE
    WHEN sal >= 3000 THEN sal + 300
    WHEN sal >= 2000 THEN sal + 500
    ELSE sal + 100
  END;
```

---

## 4. DELETE & TRUNCATE — 데이터 삭제

### 4-1. DELETE (행 단위 삭제)

```sql
DELETE FROM 테이블명 WHERE 조건;
```

```sql
-- 이름이 홍길동인 학생만 삭제
DELETE FROM student WHERE stu_name = '홍길동';

-- 조건 없이 삭제 = 모든 행 삭제 (테이블은 남는다)
DELETE FROM student;
```

### 4-2. TRUNCATE (테이블 비우기)

```sql
TRUNCATE TABLE 테이블명;
```

### 4-3. DELETE vs TRUNCATE 비교

| 구분                  | `DELETE`                                        | `TRUNCATE`                               |
| --------------------- | ----------------------------------------------- | ---------------------------------------- |
| 대상                  | `WHERE`로 선택한 행                             | 테이블 전체                              |
| DDL/DML               | DML                                             | **DDL** (자동 커밋됨)                    |
| `WHERE` 사용          | 가능                                            | 불가                                     |
| 롤백                  | 가능 (트랜잭션 내)                              | **불가**                                 |
| 인덱스·AUTO_INCREMENT | 인덱스는 유지, AUTO_INCREMENT는 일반적으로 유지 | **인덱스 재구성, AUTO_INCREMENT 초기화** |
| 성능                  | 느림 (한 행씩 로깅)                             | 빠름 (페이지 할당 해제만)                |

---

## 5. ALTER — 테이블 구조 변경

### 5-1. 컬럼 추가

```sql
ALTER TABLE student ADD stu_email VARCHAR(50);
```

### 5-2. 컬럼 타입 수정

```sql
ALTER TABLE student MODIFY stu_height DECIMAL(6,2);
```

### 5-3. 컬럼 이름 변경 (MySQL: CHANGE)

```sql
-- CHANGE는 새 이름 + 타입을 함께 써야 한다
ALTER TABLE student CHANGE stu_email email VARCHAR(50);
```

### 5-4. 컬럼 삭제

```sql
ALTER TABLE student DROP COLUMN stu_email;
```

### 5-5. 제약조건 추가/삭제

```sql
-- 뒤늦게 외래키 추가 (자식 → 부모 순서로 이미 생성되어 있어야 한다)
ALTER TABLE enrol
  ADD CONSTRAINT fk_enrol_student
  FOREIGN KEY (stu_no) REFERENCES student(stu_no);

ALTER TABLE enrol DROP FOREIGN KEY fk_enrol_student;
```

### 정리 표

| 작업           | 문법                                      |
| -------------- | ----------------------------------------- |
| 컬럼 추가      | `ALTER TABLE t ADD 컬럼 타입`             |
| 컬럼 타입 변경 | `ALTER TABLE t MODIFY 컬럼 타입`          |
| 컬럼 이름 변경 | `ALTER TABLE t CHANGE 옛이름 새이름 타입` |
| 컬럼 삭제      | `ALTER TABLE t DROP COLUMN 컬럼`          |
| 삭제(DDL)      | `DROP TABLE t` (구조까지 삭제)            |
| 비우기(DDL)    | `TRUNCATE TABLE t` (구조는 유지)          |

---

## 6. DCL — 계정과 권한 관리

**DCL (Data Control Language)** = **누가 무엇을 할 수 있는지**를 정하는 명령어

### 6-1. 사용자 생성

```sql
CREATE USER 'student'@'localhost' IDENTIFIED BY '1234';
```

### 6-2. 권한 부여 (`GRANT`)

```sql
-- 특정 DB의 모든 테이블에 대한 조회 권한
GRANT SELECT ON hh.* TO 'student'@'localhost';

-- 삽입·수정·삭제까지 포함
GRANT SELECT, INSERT, UPDATE, DELETE ON hh.* TO 'student'@'localhost';

-- 모든 권한 (루트 수준)
GRANT ALL PRIVILEGES ON hh.* TO 'student'@'localhost';

-- 적용 (MySQL 8은 보통 자동 반영되나 명시 가능)
FLUSH PRIVILEGES;
```

### 6-3. 권한 회수 (`REVOKE`)

```sql
REVOKE DELETE ON hh.* FROM 'student'@'localhost';
```

### 6-4. 권한 확인 · 사용자 삭제

```sql
SHOW GRANTS FOR 'student'@'localhost';

DROP USER 'student'@'localhost';
```

### 권한 종류

| 권한                      | 의미      |
| ------------------------- | --------- |
| `SELECT`                  | 조회      |
| `INSERT`                  | 삽입      |
| `UPDATE`                  | 갱신      |
| `DELETE`                  | 삭제      |
| `CREATE`, `DROP`, `ALTER` | DDL 작업  |
| `ALL PRIVILEGES`          | 전체 권한 |

---

## 7. 실습 문제

```sql
-- 1. student 테이블에 새 학생 (학번 20159999, 이름 '김철수', 학과 '전자공학')을 삽입하라.
INSERT INTO student (stu_no, stu_name, stu_dept) VALUES (20159999, '김철수', '전자공학');

-- 2. subject 테이블에 과목 3개를 한 번에 삽입하라.
INSERT INTO subject (sub_no, sub_name, sub_prof, sub_grade, sub_dept) VALUES
  ('119', '확률통계', '김유석', 2, '전기전자'),
  ('120', '머신러닝', '강종영', 3, '컴퓨터정보'),
  ('121', '로봇공학', '박민영', 3, '기계');

-- 3. '김철수' 학생의 학과를 '컴퓨터정보'로 변경하라.
UPDATE student SET stu_dept = '컴퓨터정보' WHERE stu_name = '김철수';

-- 4. 1학년 학생들의 학년을 2로 일괄 변경하라.
UPDATE student SET stu_grade = 2 WHERE stu_grade = 1;

-- 5. '김철수' 학생을 삭제하라.
DELETE FROM student WHERE stu_name = '김철수';

-- 6. student 테이블을 복제한 student_backup을 만들고, INSERT ... SELECT로 전체를 복사하라.
CREATE TABLE student_backup (
  stu_no CHAR(9),
  stu_name VARCHAR(12),
  stu_dept VARCHAR(20),
  stu_grade INT
);

INSERT INTO student_backup (stu_no, stu_name, stu_dept, stu_grade)
SELECT stu_no, stu_name, stu_dept, stu_grade FROM student;

SELECT * FROM student_backup;

-- 7. student_backup을 TRUNCATE로 비우고, DELETE로 비우는 두 경우의 결과를 비교하라.
TRUNCATE TABLE student_backup;
SELECT COUNT(*) FROM student_backup;   -- 0

-- 8. student 테이블에 이메일 컬럼을 추가하라.
ALTER TABLE student ADD stu_email VARCHAR(50);

-- 9. 'student'@'localhost' 계정을 생성하고 SELECT 권한만 부여한 뒤 확인하라.
CREATE USER 'student'@'localhost' IDENTIFIED BY '1234';
GRANT SELECT ON hh.* TO 'student'@'localhost';
SHOW GRANTS FOR 'student'@'localhost';

-- 10. 해당 계정의 INSERT 권한을 추가했다가 회수하라.
GRANT INSERT ON hh.* TO 'student'@'localhost';
REVOKE INSERT ON hh.* FROM 'student'@'localhost';
```

---

## 한 줄 요약

1. **DML** = `INSERT` / `UPDATE` / `DELETE` (데이터 다루기)
2. **UPDATE·DELETE는 반드시 `WHERE`**를 쓴다 (없으면 전체 행 대상)
3. **`INSERT ... SELECT`** = 조회 결과를 그대로 삽입 (테이블 복제에 유용)
4. **`TRUNCATE`** = 빠른 전체 비우기, DDL이라 **롤백 불가**
5. **`ALTER TABLE`** = 컬럼 추가/수정/이름변경/삭제
6. **DCL** = `GRANT`(부여) / `REVOKE`(회수)로 접근 권한 통제

---

[이전: Session 2 — DDL 실습](session2.md) · [다음: Session 1 — SELECT 기초](../unit2_queries/session1.md)
