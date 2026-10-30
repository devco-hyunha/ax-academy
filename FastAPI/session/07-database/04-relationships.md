# 레슨 4. ORM 관계 매핑

## 이번 레슨에서 배울 내용

- 1:N 관계 (`User.posts ↔ Post.owner`)
- cascade 옵션의 의미
- 조 join 조회

---

## 1. 관계 다이어그램

```mermaid
erDiagram
    USER ||--o{ POST : "1:N (cascade=all,delete-orphan)"
    USER {
        int user_id PK
        str username
        str email
    }
    POST {
        int post_id PK
        str title
        int user_id FK
    }
```

- `User.posts` ↔ `Post.owner` (`back_populates`)로 쌍방 관계
- 부모(`User`) 삭제 시 자식(`Post`)도 함께 삭제 (`cascade="all, delete-orphan"`)

---

## 2. 관계 매핑 코드

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, create_engine

DATABASE_CONN = "mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw1"
engine = create_engine(DATABASE_CONN)

# Base는 sqlalchemy에서 가져오는 게 아니라 직접 만드는 클래스
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    # Mapped[타입] + mapped_column
    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)

    # 하나의 사용자는 여러 게시글 작성 가능
    # User 클래스에서 posts로 Post 객체 참조
    # cascade="all, delete-orphan": user에게 한 작업(삭제, 저장) -> Post에도 적용
    # all: 모든 변경사항(DML) 자식에게 전파
    # cascade: 부모쪽에 걸었음 -> User를 지우면 Post도 지워짐
    # posts: 사용자의 글 리스트
    posts: Mapped[list["Post"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )


class Post(Base):
    __tablename__ = "post"
    post_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(500), nullable=False)

    # 하나의 게시글은 한 명의 사용자가 작성
    # Post 객체에서 owner로 User 객체 참조
    # owner: 게시글의 작성자 객체
    # User.posts <=> Post.owner 짝 지정 (post.owner = user)
    owner: Mapped["User"] = relationship(back_populates="posts")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)


Base.metadata.create_all(bind=engine)
```

핵심:

- `Base`는 sqlalchemy에서 가져오는 게 아니라 직접 만드는 클래스입니다
- `Mapped[list["Post"]] = relationship(back_populates="owner", cascade="all, delete-orphan")`
- `cascade`는 부모(User)에 걸면 자식(Post)에 전파 — User를 지우면 Post도 지워집니다

---

## 3. 조 join 조회 (Author–Book)

```python
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select, SQLAlchemyError
from sqlalchemy.orm import Session, declarative_base, mapped_column, Mapped, relationship, sessionmaker

app = FastAPI()

DATABASE_CONN = "mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw"

# 엔진 생성
# poolclass=QueuePool: 매번 DB연결 안하고 미리 연결 만들어서 재사용 (성능 up)
engine = create_engine(DATABASE_CONN)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    # author가 쓴 Book 객체들의 리스트 = relationship("연결할클래스명")
    # back_populates: Book 클래스에서 반대 관계를 연결하는 필드명
    # author.books 로 책 리스트 가져올 수 있음
    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    author: Mapped["Author"] = relationship("Author", back_populates="books")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    stmt = select(Book, Author).join(Author)
    result = db.execute(stmt).all()
    for i, j in result:
        print(i.title, j.name)
```

`select(Book, Author).join(Author)`로 한 번에 조 join 조회가 가능합니다.

---

## 연습 문제

1. Student와 Course 테이블의 1:N 관계매핑을 구현하세요.
2. Student 삭제 시 Course도 삭제되도록 cascade를 지정하세요.
3. 조 join으로 학생 이름 + 과목 제목을 조회하세요.
</contents>
