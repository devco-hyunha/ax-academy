# Session 8 — 날짜/시간 함수 (Date & Time Functions)

> 단원: [unit2_queries — SQL Querying](#unit2-queries---sql-querying)  
> 이전: [Session 7 — 서브쿼리](session7.md) · 다음: [Session 1 — RDB 특징](../unit3_advanced/session1.md)  
> 전제: Session 4의 `emp` 테이블(`hiredate` 컬럼)이 있어야 한다.

```sql
USE hh;
```

---

## 이번 세션 목표

| 목표      | 내용                                                |
| --------- | --------------------------------------------------- |
| 현재 시각 | `NOW`, `CURDATE`, `CURTIME`                         |
| 날짜 추출 | `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `DAYNAME` |
| 날짜 연산 | `DATE_ADD`, `DATE_SUB`, `DATEDIFF`                  |
| 형식 변환 | `DATE_FORMAT`, `STR_TO_DATE`                        |
| 실전 필터 | 임금 지급일·근속 연수 계산                          |

---

## 1. 현재 날짜/시각 조회

| 함수                         | 반환                     | 예                              |
| ---------------------------- | ------------------------ | ------------------------------- |
| `NOW()` / `SYSDATE()`        | 날짜 + 시각 (`DATETIME`) | `NOW()` → `2026-10-16 14:30:00` |
| `CURDATE()` / `CURRENT_DATE` | 날짜만 (`DATE`)          | `CURDATE()` → `2026-10-16`      |
| `CURTIME()` / `CURRENT_TIME` | 시각만 (`TIME`)          | `CURTIME()` → `14:30:00`        |
| `UTC_DATE()`, `UTC_TIME()`   | UTC 기준 날짜/시각       |                                 |

```sql
SELECT NOW(), CURDATE(), CURTIME();
```

> `NOW()`는 **쿼리 시작 시각**이 고정되고, `SYSDATE()`는 **실행 시각**이 갱신된다.
> (대부분의 실습에서는 `NOW()`와 동일)

---

## 2. 날짜/시각 요소 추출

| 함수                       | 반환              | 예 (`'2026-10-16 14:30:00'` 기준) |
| -------------------------- | ----------------- | --------------------------------- |
| `YEAR(d)`                  | 연도              | `2026`                            |
| `MONTH(d)`                 | 월 (숫자)         | `10`                              |
| `DAY(d)` / `DAYOFMONTH(d)` | 일                | `16`                              |
| `HOUR(t)`                  | 시                | `14`                              |
| `MINUTE(t)`                | 분                | `30`                              |
| `SECOND(t)`                | 초                | `0`                               |
| `MONTHNAME(d)`             | 월 이름           | `October`                         |
| `DAYNAME(d)`               | 요일 이름         | `Friday`                          |
| `DAYOFWEEK(d)`             | 요일 (1=일요일)   | `6`                               |
| `QUARTER(d)`               | 분기              | `4`                               |
| `WEEK(d)`                  | 주차              | `41`                              |
| `DATE(d)`                  | 날짜 부분만 추출  | `2026-10-16`                      |
| `TIME(t)`                  | 시각 부분만 추출  | `14:30:00`                        |
| `LAST_DAY(d)`              | 그 달의 마지막 날 | `2026-10-31`                      |

```sql
-- emp: 입사 연도별로 사원 수 집계
SELECT YEAR(hiredate) AS 입사연도, COUNT(*) AS 인원
FROM emp
GROUP BY YEAR(hiredate)
ORDER BY 입사연도;
```

```sql
SELECT NOW(),
  YEAR(NOW()), MONTH(NOW()), DAY(NOW()),
  DAYNAME(NOW()), DAYOFWEEK(NOW()), LAST_DAY(NOW());
```

---

## 3. 날짜 연산

### 3-1. `DATE_ADD` / `DATE_SUB` — 날짜 더하기·빼기

```sql
DATE_ADD(날짜, INTERVAL 값 단위)
DATE_SUB(날짜, INTERVAL 값 단위)
```

단위: `DAY`, `MONTH`, `YEAR`, `HOUR`, `MINUTE`, `SECOND`, `WEEK` ...

```sql
SELECT DATE_ADD('2026-10-16', INTERVAL 100 DAY);    -- 2027-01-24
SELECT DATE_SUB('2026-10-16', INTERVAL 1 MONTH);    -- 2026-09-16
SELECT DATE_ADD(NOW(), INTERVAL 3 HOUR);            -- 3시간 후

-- 출고 후 7일 반납 예정일 계산
SELECT DATE_ADD('2026-10-16', INTERVAL 7 DAY) AS 반납일;
```

### 3-2. 산술 연산자 방식 (MySQL 단축)

```sql
SELECT NOW() + INTERVAL 1 DAY;
SELECT hiredate - INTERVAL 1 YEAR FROM emp;
```

### 3-3. `DATEDIFF` — 두 날짜 사이 일수

```sql
DATEDIFF(끝날짜, 시작날짜)
```

```sql
-- 오늘 기준 근속 일수
SELECT ename, hiredate, DATEDIFF(CURDATE(), hiredate) AS 근속일수
FROM emp;

-- 오늘부터 며칠 남았는지
SELECT DATEDIFF('2026-12-31', CURDATE()) AS 남은일수;
```

### 3-4. `TIMESTAMPDIFF` — 월·년 단위 차이

```sql
TIMESTAMPDIFF(UNIT, 시작, 끝)
```

```sql
-- 근속 연수 (월 단위 차이를 12로 나눔)
SELECT ename,
  TIMESTAMPDIFF(MONTH, hiredate, CURDATE()) AS 근속월수,
  TIMESTAMPDIFF(YEAR, hiredate, CURDATE()) AS 근속연수
FROM emp;
```

### 3-5. `TIMESTAMPADD` — 시각 단위 가감

```sql
SELECT TIMESTAMPADD(HOUR, 2, NOW());   -- 2시간 후
```

---

## 4. 날짜 형식 변환

### 4-1. `DATE_FORMAT` — 날짜 → 문자열

```sql
DATE_FORMAT(날짜, '포맷')
```

| 지시자 | 의미         | 예       |
| ------ | ------------ | -------- |
| `%Y`   | 4자리 연도   | `2026`   |
| `%y`   | 2자리 연도   | `26`     |
| `%m`   | 2자리 월     | `10`     |
| `%d`   | 2자리 일     | `16`     |
| `%H`   | 24시제 시    | `14`     |
| `%i`   | 분           | `30`     |
| `%s`   | 초           | `00`     |
| `%p`   | AM/PM        | `PM`     |
| `%W`   | 요일 이름    | `Friday` |
| `%b`   | 축약 월 이름 | `Oct`    |

```sql
SELECT ename,
  DATE_FORMAT(hiredate, '%Y년 %m월 %d일') AS 입사일자,
  DATE_FORMAT(hiredate, '%Y-%m-%d %H:%i') AS 상세시각,
  DATE_FORMAT(NOW(), '%Y%m%d') AS 파일명용
FROM emp;
```

### 4-2. `STR_TO_DATE` — 문자열 → 날짜

```sql
STR_TO_DATE(문자열, '포맷')
```

```sql
SELECT STR_TO_DATE('2026/10/16', '%Y/%m/%d');   -- 2026-10-16 (DATE)
SELECT STR_TO_DATE('16-Oct-2026', '%d-%b-%Y');  -- 2026-10-16
```

### 4-3. `CAST`로 타입 변환

```sql
SELECT CAST('2026-10-16' AS DATE);
SELECT DATE('2026-10-16 14:30:00');
SELECT TIME('2026-10-16 14:30:00');
```

---

## 5. 실전 패턴

### 5-1. 이번 달 / 이번 주 데이터 조회

```sql
-- 이번 달 입사한 사원
SELECT ename, hiredate
FROM emp
WHERE YEAR(hiredate) = YEAR(NOW())
  AND MONTH(hiredate) = MONTH(NOW());

-- 월 경계를 한 줄로 잡는 법 (1일 ~ 마지막 날)
SELECT *
FROM 테이블
WHERE 날짜컬럼 >= DATE_FORMAT(NOW(), '%Y-%m-01')
  AND 날짜컬럼 <  DATE_ADD(DATE_FORMAT(NOW(), '%Y-%m-01'), INTERVAL 1 MONTH);
```

### 5-2. 나이 계산

```sql
SELECT name, birth,
  TIMESTAMPDIFF(YEAR, birth, CURDATE()) AS 만나이
FROM 학생테이블;
```

### 5-3. 요일별 매출 집계

```sql
SELECT DAYNAME(주문일) AS 요일, COUNT(*) AS 주문수
FROM orders
GROUP BY DAYOFWEEK(주문일), DAYNAME(주문일)
ORDER BY DAYOFWEEK(주문일);
```

---

## 6. 실습 문제

```sql
-- 1. 오늘 날짜와 현재 시각을 각각 검색하라.
SELECT CURDATE() AS 오늘, NOW() AS 현재시각;

-- 2. 사원들의 입사 연도와 입사 월을 검색하라.
SELECT ename, YEAR(hiredate) AS 입사연도, MONTH(hiredate) AS 입사월 FROM emp;

-- 3. 입사일이 어떤 요일인지 요일 이름으로 검색하라.
SELECT ename, hiredate, DAYNAME(hiredate) AS 입사요일 FROM emp;

-- 4. 오늘부터 100일 후의 날짜를 검색하라.
SELECT DATE_ADD(CURDATE(), INTERVAL 100 DAY) AS 백일후;

-- 5. 오늘부터 1개월 전의 날짜를 검색하라.
SELECT DATE_SUB(CURDATE(), INTERVAL 1 MONTH) AS 한달전;

-- 6. 사원의 입사일로부터 오늘까지의 근속 일수를 검색하라.
SELECT ename, hiredate, DATEDIFF(CURDATE(), hiredate) AS 근속일수 FROM emp;

-- 7. 사원의 입사일로부터 오늘까지의 근속 연수를 검색하라.
SELECT ename, TIMESTAMPDIFF(YEAR, hiredate, CURDATE()) AS 근속연수 FROM emp;

-- 8. 입사일을 '2026년 10월 16일' 형식으로 표시하라.
SELECT ename, DATE_FORMAT(hiredate, '%Y년 %m월 %d일') AS 입사일자 FROM emp;

-- 9. 입사일을 '20261016' 형식(숫자 8자리)으로 검색하라.
SELECT ename, DATE_FORMAT(hiredate, '%Y%m%d') AS 입사일자8 FROM emp;

-- 10. 문자열 '2026/10/16'을 DATE 타입으로 변환하라.
SELECT STR_TO_DATE('2026/10/16', '%Y/%m/%d');

-- 11. 이번 달에 입사한 사원을 검색하라.
SELECT ename, hiredate
FROM emp
WHERE YEAR(hiredate) = YEAR(NOW())
  AND MONTH(hiredate) = MONTH(NOW());

-- 12. 입사일이 6월인 사원의 입사일에서 3개월을 뺀 날짜를 검색하라.
SELECT ename, DATE_SUB(hiredate, INTERVAL 3 MONTH) AS 삼개월전 FROM emp;

-- 13. 오늘 기준 다음 달 같은 날의 날짜를 검색하라.
SELECT DATE_ADD(CURDATE(), INTERVAL 1 MONTH) AS 다음달;

-- 14. 각 사원의 입사일이 속한 분기를 검색하라.
SELECT ename, QUARTER(hiredate) AS 입사분기 FROM emp;

-- 15. 입사월의 마지막 날짜를 검색하라.
SELECT ename, LAST_DAY(hiredate) AS 해당월마지막날 FROM emp;
```

---

## 한 줄 요약

1. **`NOW()` / `CURDATE()` / `CURTIME()`** = 현재 시각·날짜·시각
2. **`YEAR` / `MONTH` / `DAY` / `DAYNAME`** = 요소 추출
3. **`DATE_ADD` / `DATE_SUB`** = `INTERVAL` 단위로 날짜 가감
4. **`DATEDIFF`** = 일수 차이, **`TIMESTAMPDIFF`** = 월·년 단위 차이
5. **`DATE_FORMAT`** = 날짜 → 문자열, **`STR_TO_DATE`** = 문자열 → 날짜
6. **경계 조건**은 `BETWEEN`보다 `>= 시작 AND < 다음달 시작` 패턴이 안전하다

---

[이전: Session 7 — 서브쿼리](session7.md) · [다음: Session 1 — RDB 특징](../unit3_advanced/session1.md)
