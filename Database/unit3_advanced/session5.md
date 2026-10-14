# Session 5 — Redis

> 단원: [unit3_advanced — Advanced Topics](#unit3-advanced---advanced-topics)  
> 이전: [Session 4 — NoSQL](unit3_advanced/session4.md)

## 1. Redis 개요

- **Remote Dictionary Server**: 키-값(Key-Value) 데이터 저장소
- 고성능의 오픈소스 인메모리 데이터베이스
- 데이터는 **디스크가 아닌 메모리(RAM)에 저장**되어 초고속 성능 발휘
- 디스크 기반 DB보다 압도적으로 빠른 읽기/쓰기 성능

## 2. 데이터 구조

- **문자열(String)**: 기본 데이터형, 다양한 패턴의 문자열 저장
- **해시(Hash)**: 필드-값 매핑 형태, 복잡한 객체 저장
- **리스트(List)**: 문자열의 순서진 컬렉션, 양방향 큐 지원
- **집합(Set)**: 고유한 문자열 모음, 교집합/차집합 연산 지원
- **정렬된 집합(Sorted Set)**: 점수(Score)가 있는 멤버 Members, 순위 기반 조회

## 3. 주요 사용 사례

- 세션(Session) 관리: 빠른 조회로 웹 세션 관리
- 캐시(Caching): 자주 액세스하는 데이터 캐시
- 카운터(Counter): 조회수, 좋아요 수 등 숫자 증가 연산
- 리더보드(Leaderboard): 점수 기반 순위 매기기
- 실시간 랭킹 서비스에 최적화

## 3. 주요 명령어

- `SET key value`: 키-값 저장
- `GET key`: 키에 해당하는 값 조회
- `DEL key`: 키 삭제
- `EXPIRE key seconds`: 키의 생명주기 설정
- `KEYS pattern`: 패턴에 매칭되는 키 조회
- `TTL key`: 남은 생명주기 조회

## 4. 정리

- Redis: 키-값(Key-Value) 데이터 저장소
- 디스크보다 메모리(RAM) 접근이 빠른 초고속 성능
- 다양한 데이터 구조(String, List, Set, Hash, Sorted Set) 지원
- 세션 관리, 캐시, 카운터, 리더보드 등 다양한 사용 사례 제공

## 이번 세션 목표

| 목표         | 내용                                       |
| ------------ | ------------------------------------------ |
| 테이블 정의  | user, post, category, hashtag, 연결 테이블 |
| PK / FK 설정 | 식별 키와 참조 키 위치                     |
| 관계 구현    | 1:N은 FK, M:N은 연결 테이블                |
| DDL 작성     | CREATE TABLE 문장으로 스키마화             |

---

## 1. 사용자 테이블 (user)

| id(pk) | login_id | 이메일      | 비밀번호 | 나이 | 자기소개 | 이름   |
| ------ | -------- | ----------- | -------- | ---- | -------- | ------ |
| 1      | yang     | a@naver.com | 123      | 12   | hi       | 양종현 |
| 2      | hyun     | b@naver.com | 123      | 55   | hello    | 김현준 |
| 3      | min      | c@naver.com | 123      | 12   | hi       | 김민준 |

```sql
CREATE TABLE user (
    id          INT PRIMARY KEY AUTO_INCREMENT,   -- pk
    login_id    VARCHAR(20) NOT NULL UNIQUE,      -- 로그인 아이디
    email       VARCHAR(50) NOT NULL UNIQUE,
    password    VARCHAR(20) NOT NULL,
    age         INT,
    intro       VARCHAR(100),                     -- 자기소개
    name        VARCHAR(20) NOT NULL
);
```

- 로그인 = `login_id` + `password`로 조회
- `id`는 다른 테이블이 참조하는 **PK**

---

## 2. 게시글 테이블 (post)

| id(pk) | 제목  | 내용  | 작성시간 | 수정시간 | 조회수 | 작성자 id(fk) | 카테고리 id(fk) |
| ------ | ----- | ----- | -------- | -------- | ------ | ------------- | --------------- |
| 1      | 제목1 | 내용1 | 26.10.11 | 26.10.12 | 400    | 1             | 1               |
| 2      | 제목2 | 내용2 | 26.08.03 | 26.09.02 | 2      | 1             | 1               |
| 3      | 제목3 | 내용3 | 26.08.21 | 26.08.22 | 400    | 2             | 2               |

```sql
CREATE TABLE post (
    id          INT PRIMARY KEY AUTO_INCREMENT,   -- pk
    title       VARCHAR(50) NOT NULL,
    content     TEXT,
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,   -- 작성시간
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP
                ON UPDATE CURRENT_TIMESTAMP,          -- 수정시간
    views       INT DEFAULT 0,                        -- 조회수
    user_id     INT NOT NULL,                         -- 작성자 fk
    category_id INT,                                  -- 카테고리 fk
    CONSTRAINT fk_post_user FOREIGN KEY (user_id)
        REFERENCES user(id),
    CONSTRAINT fk_post_category FOREIGN KEY (category_id)
        REFERENCES category(id)
);
```

### 관계 확인

**사용자와 게시글의 관계 (1:N)** ⇒ N쪽에 FK (게시글)

- 한 사용자는 게시글을 여러 개 작성할 수 있다.
- 한 게시글의 작성자는 딱 1명이다.

**게시글과 카테고리 관계 (N:1)** ⇒ N쪽에 FK (게시글)

- 게시글 1개는 카테고리 한 개를 가진다.
- 하나의 카테고리는 여러 게시글에 의해 설정될 수 있다.

---

## 3. 카테고리 테이블 (category)

| id(pk) | 카테고리명 |
| ------ | ---------- |
| 1      | 일기       |
| 2      | 홍보       |

```sql
CREATE TABLE category (
    id   INT PRIMARY KEY AUTO_INCREMENT,  -- pk
    name VARCHAR(20) NOT NULL
);
```

---

## 4. 해시태그 테이블 (hashtag)

| id(pk) | 해시태그명 |
| ------ | ---------- |
| 1      | 맛집       |
| 2      | 여행       |
| 3      | 공부       |
| 4      | 취업       |
| 5      | 운동       |

```sql
CREATE TABLE hashtag (
    id   INT PRIMARY KEY AUTO_INCREMENT,  -- pk
    name VARCHAR(20) NOT NULL UNIQUE
);
```

### 게시글과 해시태그의 관계 (M:N) ⇒ 연결 테이블 필요

- 게시글에 여러 개 해시태그를 달 수 있다.
- 한 해시태그를 여러 게시글에 달 수 있다.

```sql
CREATE TABLE post_hashtag (
    post_id    INT NOT NULL,
    hashtag_id INT NOT NULL,
    PRIMARY KEY (post_id, hashtag_id),   -- 복합 PK
    CONSTRAINT fk_ph_post FOREIGN KEY (post_id)
        REFERENCES post(id),
    CONSTRAINT fk_ph_hashtag FOREIGN KEY (hashtag_id)
        REFERENCES hashtag(id)
);
```

- M:N 관계는 **연결 테이블(새로운 테이블)**로 구현
- 복합 PK로 같은 조합 중복 방지

---

## 5. 좋아요 테이블 (post_like)

- 사용자가 게시글에 좋아요를 누를 수 있다.
- 특정 게시글에 어떤 사용자들이 좋아요를 눌렀는지 조회 가능해야 한다.
- 사용자 ↔ 게시글 **M:N** ⇒ 연결 테이블

```sql
CREATE TABLE post_like (
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    PRIMARY KEY (user_id, post_id),
    CONSTRAINT fk_like_user FOREIGN KEY (user_id)
        REFERENCES user(id),
    CONSTRAINT fk_like_post FOREIGN KEY (post_id)
        REFERENCES post(id)
);
```

---

## 6. 팔로우 테이블 (follow)

- 특정 사용자가 다른 사용자를 팔로우할 수 있다.
- 각 사용자의 팔로우 수를 조회할 수 있어야 한다.
- 사용자 ↔ 사용자 **M:N (자기참조)** ⇒ 연결 테이블

```sql
CREATE TABLE follow (
    user_id    INT NOT NULL,   -- 팔로우하는 사람
    target_id  INT NOT NULL,   -- 팔로우당하는 사람
    PRIMARY KEY (user_id, target_id),
    CONSTRAINT fk_follow_user FOREIGN KEY (user_id)
        REFERENCES user(id),
    CONSTRAINT fk_follow_target FOREIGN KEY (target_id)
        REFERENCES user(id)
);
```

### 팔로우 수 조회

```sql
-- 어떤 사용자의 팔로워 수
SELECT target_id AS 사용자, COUNT(*) AS 팔로우수
FROM follow
GROUP BY target_id;

-- 특정 사용자가 팔로우한 수
SELECT user_id AS 사용자, COUNT(*) AS 팔로잉수
FROM follow
GROUP BY user_id;
```

---

## 7. ER 관계 요약

```mermaid
erDiagram
    user ||--o{ post : "1:N 작성"
    category ||--o{ post : "1:N 포함"
    post }--o{ post_hashtag : "M:N"
    hashtag }--o{ post_hashtag : "M:N"
    user }--o{ post_like : "M:N"
    post }--o{ post_like : "M:N"
    user }--o{ follow : "M:N 팔로우"
    user }--o{ follow : "M:N 대상"
```

| 관계                 | 종류         | 구현                     |
| -------------------- | ------------ | ------------------------ |
| user – post          | 1:N          | post.user_id FK          |
| post – category      | N:1          | post.category_id FK      |
| post – hashtag       | M:N          | post_hashtag 연결 테이블 |
| user – post (좋아요) | M:N          | post_like 연결 테이블    |
| user – user (팔로우) | M:N 자기참조 | follow 연결 테이블       |

---

## 8. 실습 쿼리

```sql
-- 1. 게시글과 작성자 이름을 함께 조회
SELECT p.title, u.name AS 작성자, p.created_at, p.views
FROM post p
JOIN user u ON p.user_id = u.id;

-- 2. 특정 해시태그('맛집')를 가진 모든 게시글 조회
SELECT p.title
FROM post p
JOIN post_hashtag ph ON p.id = ph.post_id
JOIN hashtag h ON ph.hashtag_id = h.id
WHERE h.name = '맛집';

-- 3. 특정 게시글에 좋아요를 누른 사용자 조회
SELECT u.name
FROM user u
JOIN post_like pl ON u.id = pl.user_id
WHERE pl.post_id = 1;

-- 4. 각 사용자의 팔로우 수 (팔로워 수)
SELECT u.name, COUNT(f.target_id) AS 팔로우수
FROM user u
LEFT JOIN follow f ON u.id = f.target_id
GROUP BY u.id, u.name;

-- 5. 게시글에 달린 해시태그 목록
SELECT p.title, GROUP_CONCAT(h.name) AS 해시태그
FROM post p
JOIN post_hashtag ph ON p.id = ph.post_id
JOIN hashtag h ON ph.hashtag_id = h.id
GROUP BY p.id, p.title;
```

---

## 한 줄 요약

1. **user** = 회원가입 정보 + 로그인(id/password) 컬럼
2. **post** = 제목·내용·작성/수정시간·조회수 + 작성자 FK·카테고리 FK
3. **1:N / N:1** = N쪽(post)에 FK
4. **M:N** = 연결 테이블 (post_hashtag, post_like, follow)
5. 연결 테이블은 **복합 PK**로 중복 방지
6. 조회 요구사항은 JOIN으로 구현

---

## [이전: Session 5 — DB 모델링](unit3_advanced/session5.md)

## [마지막 세션]
