# Session 2 — WHERE 조건

> 단원: [unit2_queries — SQL Querying](#unit2-queries---sql-querying)  
> 이전: [Session 1 — SELECT 기초](unit2_queries/session1.md) · 다음: [Session 3 — 문자열 함수·ORDER BY](unit2_queries/session3.md)  
> 전제: Session 1의 `student` / `subject` / `enrol` 데이터

```sql
USE hh;
```

---

## 이번 세션 목표

| 목표 | 내용 |
| ---- | ---- |
| 비교 | `=`, `<>`, `!=`, `>`, `>=`, `<`, `<=` |
| 논리 | `AND`, `OR`, `NOT` |
| 범위·목록 | `BETWEEN`, `IN` |
| 패턴 | `LIKE` (`%`, `_`) |
| NULL | `IS NULL` / `IS NOT NULL` |
| 행 수 제한 | `LIMIT` (참고) |

---

## 1. WHERE 기본

```sql
SELECT 컬럼들
FROM 테이블명
WHERE 조건;
```

조건이 참인 **행만** 남긴다. (Session 3의 처리 순서: `FROM → WHERE → SELECT`)

### 비교 연산자

| 연산자 | 의미 |
| ------ | ---- |
| `=` | 같음 |
| `<>` / `!=` | 다름 (둘 다 MySQL에서 동일) |
| `>`, `>=`, `<`, `<=` | 크기 비교 |

### 논리 연산자

| 연산자 | 의미 |
| ------ | ---- |
| `AND` | 둘 다 참 |
| `OR` | 하나라도 참 |
| `NOT` | 조건 부정 |

### BETWEEN / IN / LIKE

| 구문 | 의미 | 예 |
| ---- | ---- | -- |
| `BETWEEN a AND b` | `a` 이상 `b` 이하 (양끝 포함) | `stu_weight BETWEEN 60 AND 70` |
| `IN (v1, v2, ...)` | 목록 중 하나 | `stu_dept IN ('기계', '컴퓨터정보')` |
| `LIKE '패턴'` | 문자열 패턴 | `stu_name LIKE '김%'` |

| 와일드카드 | 의미 |
| ---------- | ---- |
| `%` | 0글자 이상 |
| `_` | 정확히 1글자 |

### (추가) NULL 비교

`NULL`은 “값이 없음”이라 `=` / `<>`로 비교하면 결과가 항상 알 수 없음(행이 안 나옴)이다.

```sql
-- 잘못된 예
SELECT * FROM student WHERE stu_height = NULL;   -- 결과 없음

-- 올바른 예
SELECT * FROM student WHERE stu_height IS NULL;
SELECT * FROM student WHERE stu_height IS NOT NULL;
```

---

## 2. 예제

```sql
-- 앞에서부터 5행
SELECT * FROM student LIMIT 5;

-- 범위
SELECT * FROM student WHERE stu_weight BETWEEN 60 AND 70;
SELECT * FROM student WHERE stu_no BETWEEN '20140001' AND '20149999';

-- 목록
SELECT * FROM student WHERE stu_dept IN ('컴퓨터정보', '기계');

-- 패턴
SELECT stu_no, stu_name, stu_dept FROM student WHERE stu_name LIKE '김%';
SELECT * FROM student WHERE stu_no LIKE '2014%';
```

---

## 3. 실습 문제

```sql
-- 1. 컴퓨터정보 학생들을 검색하라.
SELECT * FROM student WHERE stu_dept = '컴퓨터정보';

-- 2. 기계과 학생들을 검색하라.
SELECT * FROM student WHERE stu_dept = '기계';

-- 3. 전기전자과 학생들을 검색하라.
SELECT * FROM student WHERE stu_dept = '전기전자';

-- 4. 신장이 170이상인 학생들을 검색하라.
SELECT * FROM student WHERE stu_height >= 170;

-- 5. 체중이 65이상인 학생들을 검색하라.
SELECT * FROM student WHERE stu_weight >= 65;

-- 6. 기계 학생들의 학번, 이름을 검색하라.
SELECT stu_no, stu_name FROM student WHERE stu_dept = '기계';

-- 7. 컴퓨터정보 학생들의 학번, 이름을 검색하라.
SELECT stu_no, stu_name FROM student WHERE stu_dept = '컴퓨터정보';

-- 8. 남학생의 이름을 검색하라.
SELECT stu_name FROM student WHERE stu_gender = 'M';

-- 9. 전기전자과 이외 학생들의 모든 정보를 검색하라.
SELECT * FROM student WHERE stu_dept <> '전기전자';

-- 10. 점수가 80점 이상인 수강 정보를 검색하라.
SELECT * FROM enrol WHERE enr_grade >= 80;

-- 11. '김인중'학생의 모든 정보를 검색하라.
SELECT * FROM student WHERE stu_name = '김인중';

-- 12. '기계'과 이고 2학년인 학생들의 학번, 이름을 검색하라.
SELECT stu_no, stu_name FROM student WHERE stu_dept = '기계' AND stu_grade = 2;

-- 13. 성별이 여학생이며, 체중이 60이하인 학생을 모두 검색하라.
SELECT * FROM student WHERE stu_gender = 'F' AND stu_weight <= 60;

-- 14. '컴퓨터정보'외에 1학년 학생들의 이름을 검색하라.
SELECT stu_name FROM student WHERE stu_dept != '컴퓨터정보' AND stu_grade = 1;

-- 15. 학과 중 '기계'이외의 학과를 검색하라. (중복제거)
SELECT DISTINCT stu_dept FROM student WHERE stu_dept != '기계';

-- 16. 컴퓨터정보과 2학년 A반 학생의 학번과 이름을 검색하라.
SELECT stu_no, stu_name FROM student
WHERE stu_dept = '컴퓨터정보' AND stu_grade = 2 AND stu_class = 'A';

-- 17. 신장이 160이상이며 170이하인 학생의 학번과 이름을 검색하라.
SELECT stu_no, stu_name FROM student WHERE stu_height BETWEEN 160 AND 170;

-- 18. 키가 NULL인 학생의 학번과 이름을 검색하라.
SELECT stu_no, stu_name FROM student WHERE stu_height IS NULL;

-- 19. 키가 NULL이 아닌 학생의 학번, 이름, 키를 검색하라.
SELECT stu_no, stu_name, stu_height FROM student WHERE stu_height IS NOT NULL;
```

### 수정·참고 메모

| 번호 | 메모 |
| ---- | ---- |
| 11 | 원본 오타 `sub_name` → **`stu_name`** |
| 17 | 원본 `BETWEEN 160, 170` → **`BETWEEN 160 AND 170`** |
| 9·14·15 | `<>`와 `!=`는 MySQL에서 동일 |
| 18·19 | (추가) `NULL`은 `IS NULL` / `IS NOT NULL` |

---

## 한 줄 요약

1. **WHERE** = 행 필터
2. **BETWEEN / IN / LIKE** = 범위·목록·패턴
3. **AND / OR** = 조건 결합
4. **NULL** = `=` 금지, **`IS NULL` / `IS NOT NULL`**
5. `<>` ≈ `!=`

---

[이전: Session 1 — SELECT 기초](unit2_queries/session1.md) · [다음: Session 3 — 문자열 함수·ORDER BY](unit2_queries/session3.md)
