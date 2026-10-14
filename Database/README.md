# Database — DB 실습 및 학습일지

## 📁 단원별 구조

### unit1_basic — Basic Theory & DDL
- [Session 1](unit1_basic/session1.md) — 데이터베이스 기초 이론
- [Session 2](unit1_basic/session2.md) — DDL 실습

### unit2_queries — SQL Querying
- [Session 1](unit2_queries/session1.md) — SELECT 기초
- [Session 2](unit2_queries/session2.md) — WHERE 조건
- [Session 3](unit2_queries/session3.md) — 문자열 함수 + ORDER BY
- [Session 4](unit2_queries/session4.md) — SCOTT 스키마 (dept/emp/salgrade)
- [Session 5](unit2_queries/session5.md) — JOIN 실습 (emp/dept/salgrade)
- [Session 6](unit2_queries/session6.md) — 집계 함수 + GROUP BY
- [Session 7](unit2_queries/session7.md) — 서브쿼리 (Subquery)

### unit3_advanced — Advanced Topics
- [Session 1](unit3_advanced/session1.md) — RDB 특징
- [Session 2](unit3_advanced/session2.md) — 데이터 무결성(integrity) 보장
- [Session 3](unit3_advanced/session3.md) — 정규화(Normalization)
- [Session 4](unit3_advanced/session4.md) — NoSQL
- [Session 5](unit3_advanced/session5.md) — Redis

### 📝 Review
- [Review](review.md) — SQL 질의어 종합 복습 (실행 순서, 서브쿼리, 조인)

---

## unit1_basic — Basic Theory & DDL

| 세션 | 제목 | 주요 내용 |
|------|------|----------|
| [Session 1](unit1_basic/session1.md) | **데이터베이스 기초 이론** | DB의 목적, 스키마, 3계층 구조, RDBMS 기본 구조, 키 개념 |
| [Session 2](unit1_basic/session2.md) | **DDL 실습 (student / subject / enrol)** | 테이블 생성(PK, 복합키), 데이터 삽입, 구조 확인 |

## unit2_queries — SQL Querying

| 세션 | 제목 | 주요 내용 |
|------|------|----------|
| [Session 1](unit2_queries/session1.md) | **SELECT 기초** | 컬럼 선택, DISTINCT, 별칭, 표현식, SQL 실행 순서 |
| [Session 2](unit2_queries/session2.md) | **WHERE 조건** | 비교 연산자, 논리 연산자, BETWEEN, IN, LIKE, NULL 처리 |
| [Session 3](unit2_queries/session3.md) | **문자열 함수 + ORDER BY** | LENGTH, INSTR, LPAD, RPAD, REPLACE, TRIM, CONCAT, 정렬 |
| [Session 4](unit2_queries/session4.md) | **SCOTT 스키마 (dept / emp / salgrade)** | 자기참조 FK, 사원/부서/급여 테이블, 데이터 삽입 순서 |
| [Session 5](unit2_queries/session5.md) | **JOIN 실습 (emp / dept / salgrade)** | 등가조인(NATURAL/USING/ON), INNER, LEFT/RIGHT OUTER, SELF, CROSS JOIN |
| [Session 6](unit2_queries/session6.md) | **집계 함수 + GROUP BY** | COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING, ROLLUP/CUBE |
| [Session 7](unit2_queries/session7.md) | **서브쿼리 (Subquery)** | 단일행, 다중행(IN, ANY/SOME, ALL), 상관서브쿼리, EXISTS/NOT EXISTS |

## unit3_advanced — Advanced Topics

| 세션 | 제목 | 주요 내용 |
|------|------|----------|
| [Session 1](unit3_advanced/session1.md) | **RDB 특징** | 관계형 모델, 2차원 테이블, 데이터 무결성, 스키마 정의 |
| [Session 2](unit3_advanced/session2.md) | **데이터 무결성** | 개체 무결성(PK), 참조 무결성(FK), 도메인 무결성(NOT NULL, CHECK, UNIQUE) |
| [Session 3](unit3_advanced/session3.md) | **정규화** | 1NF → 2NF → 3NF → BCNF, 이상현상 제거, 장단점 |
| [Session 4](unit3_advanced/session4.md) | **NoSQL** | RDB 한계 극복, 키-값/문서/열/그래프 저장소, RDB vs NoSQL 비교 |
| [Session 5](unit3_advanced/session5.md) | **Redis** | Remote Dictionary Server, 인메모리 저장, 데이터 구조(String, Hash, List, Set, Sorted Set), 사용 사례 |

## 📝 Review — SQL 질의어 종합 복습

| 파일 | 제목 | 주요 내용 |
|------|------|----------|
| [review.md](review.md) | **SQL 질의어 복습** | 실행 순서(FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY), 서브쿼리, 조인 종류 |

---

## 📂 폴더 구조

```
Database/
├── unit1_basic/          # Basic Theory & DDL (2 sessions)
│   ├── session1.md       # DB 기초 이론
│   └── session2.md       # DDL 실습
├── unit2_queries/        # SQL Querying (7 sessions)
│   ├── session1.md       # SELECT 기초
│   ├── session2.md       # WHERE 조건
│   ├── session3.md       # 문자열 함수
│   ├── session4.md       # SCOTT 스키마
│   ├── session5.md       # JOIN 실습
│   ├── session6.md       # 집계 함수
│   └── session7.md       # 서브쿼리
├── unit3_advanced/       # Advanced Topics (5 sessions)
│   ├── session1.md       # RDB 특징
│   ├── session2.md       # 데이터 무결성
│   ├── session3.md       # 정규화
│   ├── session4.md       # NoSQL
│   └── session5.md       # Redis
├── review.md             # SQL 질의어 종합 복습
└── README.md             # 이 파일
```

---

각 세션은 Markdown 파일을 통해 상세한 실습 내용과 SQL 예제 및 요약 내용을 확인하실 수 있습니다.
