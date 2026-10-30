# 레슨 6. Raw SQL로 DB 다루기

## 이번 레슨에서 배울 내용

- create_engine 연결 흐름
- Connection Pooling
- text() + bindparams로 INSERT/SELECT

---

## 1. DB 연결 흐름

엔진 생성 → DB 연결 → SQL 작성 → 실행 → 결과 조회 → 연결 종료

1. 클라이언트가 DB Connection 요청

```text
mysql+pymysql://사용자명:패스워드@주소:포트/DB명
conn = engine.connect()
```

2. DB가 요청 허용
3. Connection으로 SQL 요청
4. DB가 Cursor 생성 후 결과 반환 준비
5. 클라이언트가 fetch

```python
rows = result.fetchall()
print(rows)
result.close()
```

6. 결과 전송
7. Connection 종료

```python
conn.close()
```

```mermaid
sequenceDiagram
    participant C as 클라이언트
    participant D as DB
    C->>D: Connection 요청
    D->>D: 요청 허용
    C->>D: SQL 요청
    D->>C: Cursor 반환
    C->>D: fetch
    C->>D: Connection 종료
```

---

## 2. Connection Pooling

요청마다 Connection을 만들고 끊으면 DB 자원 소모가 큽니다.
미리 Pool에 Connection을 두어, SQL 수행 후 **종료하지 않고 Pool에 반환**하는 방식이 Connection Pooling입니다.

```python
from sqlalchemy.pool import QueuePool
engine = create_engine(DATABASE_CONN, poolclass=QueuePool)
```

커넥션 풀을 설정하지 않으면 세션이 계속 생겨 메모리를 불필요하게 차지합니다.

---

## 3. create_engine 실행 예

```python
from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError

# db유형+드라이버명://사용자명:비번@localhost:포트번호/db명
DATABASE_CONN = "mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw"

# engine은 sqlalchemy에서 DB 연결 객체를 생성하는 함수
# poolclass=QueuePool: 매번 DB연결 객체 생성 안하고 미리 만들어 재사용 (성능 up)
engine = create_engine(DATABASE_CONN, poolclass=QueuePool)

try:
    conn = engine.connect()
    query = "select stu_no, stu_name from student"
    stmt = text(query)
    result = conn.execute(stmt)
    print(result)
    rows = result.fetchall()
    print(rows)
except SQLAlchemyError as e:
    print(e)
finally:
    conn.close()
```

- `text(query)`가 문자열 SQL을 실행 가능한 SQL 문 객체로 감싸 줍니다
- `conn.close()`는 연결을 종료하는 것이 아니라 **Pool에 반환**합니다

---

## 4. bindparams로 안전하게 INSERT

```python
from datetime import datetime

def insert_article(title, author, content=None):
    with get_conn() as conn:
        if not content:
            content = "비어있다"

        ch_query = "select COUNT(*) from articles where title=:title and author=:author"
        result = conn.execute(text(ch_query).bindparams(title=title, author=author))
        cnt = result.scalar()

        if cnt > 0:
            print("이미 있는 제목과 작성자")
            return

        insert_sql = """
            insert into articles (title, author, content, published_at)
            values (:title, :author, :content, :published_at)
        """
        stmt = text(insert_sql).bindparams(
            title=title,
            author=author,
            content=content,
            published_at=datetime.now(),
        )
        conn.execute(stmt)
        conn.commit()
```

- `:title` 같은 named parameter를 `bindparams()`로 안전하게 채웁니다
- SQL 문자열에 변수를 직접 넣는 것은 SQL injection 위험이 있습니다

---

## 5. articles 테이블 만들기

테이블명: articles

| 컬럼 | 타입 |
|------|------|
| id | 정수, 기본키, 자동 증가 |
| title | 문자열(100), null 불가 |
| author | 문자열(50), null 불가 |
| content | TEXT, null 가능 |
| published_at | DATETIME, 기본값 현재 시각 |

---

## 연습 문제

1. `articles`에 INSERT하는 함수를 `bindparams`로 작성하세요.
2. title+author가 같은 레코드가 이미 있는지 `scalar()`로 검사하세요.
3. 조건에 맞는 rows를 `fetchall()`로 조회하세요.
</contents>
