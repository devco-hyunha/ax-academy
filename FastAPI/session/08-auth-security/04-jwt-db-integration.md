# 레슨 4. JWT + DB 실전 통합

## 이번 레슨에서 배울 내용

- JWT 토큰 발급·검증 유틸
- 회원가입 + 로그인 + 보호된 API를 DB와 연결
- OAuth2PasswordRequestForm으로 로그인 폼 처리

---

## 1. JWT 토큰 구조

클라이언트가 서버에 로그인 요청을 보내면 서버가 도장(서명)을 찍은 문서를 발급해 주고, 클라이언트가 그 문서(토큰)를 들고 오면 서버가 도장(서명)을 확인합니다.

```text
Header  = { "alg": "HS256", "typ": "JWT" }
Payload = { "username": "lee", "exp": 만료시간 }
Signature = HS256(Header + Payload, SECRET_KEY)
토큰 = Header.Payload.Signature
```

```python
import datetime
import jwt

SECRET_KEY = "secret_key"


def create_jwt(data: dict):
    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
    data["exp"] = exp
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")
```

`sub`(subject)은 토큰의 주인을 나타냅니다.

---

## 2. 토큰 검증

```python
@app.get("/verify")
def verify(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"valid": True, "username": payload.get("username")}
    # 401: Unauthorized — 인증 실패
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="토큰 만료됨")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰")
```

```mermaid
flowchart TD
    T[토큰] --> D["jwt.decode(token, SECRET_KEY)"]
    D --> S{서명·만료 검증}
    S -->|만료| E1["401: 토큰 만료됨"]
    S -->|유효하지 않음| E2["401: 유효하지 않은 토큰"]
    S -->|통과| OK["username 반환"]
```

---

## 3. OAuth2PasswordRequestForm / OAuth2PasswordBearer

```python
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

# 사용자가 /token에서 토큰을 발급받고, API 요청 시 Authorization 헤더에
# Bearer 토큰을 넣어서 인증하는 구조
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login(f_data: OAuth2PasswordRequestForm = Depends()):
    user = user_db.get(f_data.username)
    if not user or user["password"] != f_data.password:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰")
    access_token = create_jwt(data={"sub": user["username"]}, expire=timedelta(minutes=60))
    return {"access_token": access_token, "type": "bearer"}


# Depends(oauth_scheme): Authorization: Bearer 헤더에서 토큰 문자열만 뽑아준다
@app.get("/verify")
def verify(token: str = Depends(oauth_scheme)):
    username = verify_token(token)
    return {"msg": "valid token", "username": username}
```

- `OAuth2PasswordRequestForm` — username, password form 입력을 받음
- `OAuth2PasswordBearer(tokenUrl="token")` — 헤더에서 토큰 문자열만 추출

---

## 4. JWT + DB 통합

User와 Book 테이블을 DB로 관리하는 실전 구성입니다.

```python
DATABASE_CONN = "mysql+mysqlconnector://root:1234@127.0.0.1:3306/jw1"
engine = create_engine(DATABASE_CONN, poolclass=QueuePool)
Base = declarative_base()

# ORM 모델
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String(40), nullable=False)
    author = Column(String(40), nullable=False)
    page = Column(Integer, nullable=False)

Base.metadata.create_all(bind=engine)

# Pydantic 모델
class UserCreate(BaseModel):
    username: str = Field(..., min_length=2, max_length=20)
    password: str = Field(..., min_length=4)
    email: EmailStr

# 회원가입 — 이미 있는 사용자인지 검사
@app.post("/users")
async def create_user(user: UserCreate):
    with Session(engine) as db:
        if db.query(User).filter(User.username == user.username).first():
            raise HTTPException(status_code=400, detail="이미 존재하는 사용자")
        new_user = User(username=user.username, password=user.password, email=user.email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"id": new_user.id, "username": new_user.username}

# 사용자 검색 (Query 파라미터)
@app.get("/users/search")
async def search_user(username: str = Query(...)):
    with Session(engine) as db:
        users = db.query(User).filter(User.username.contains(username)).all()
        return [{"id": i.id, "username": i.username, "email": i.email} for i in users]

# JWT 토큰 발급
@app.post("/token")
async def login_access(username: str = Form(...), password: str = Form(...)):
    with Session(engine) as db:
        user = db.query(User).filter(User.username == username).first()
        if not user or user.password != password:
            raise HTTPException(status_code=401, detail="아이디 또는 비밀번호에서 오류")
        token = create_jwt(username)
        return {"access_token": token, "token_type": "bearer"}

# JWT가 검증된 사람만 책 조회 가능
@app.get("/security/book/{book_id}")
async def security_book(book_id: int, token: str = Depends(oauth2_scheme)):
    username = verify_token(token)  # 검증 확인됨
    with Session(engine) as db:
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise HTTPException(status_code=404, detail="책 없음")
        return {"book_id": book.id}
```

```mermaid
flowchart TD
    P["POST /token (username, password)"] --> A{DB에서 사용자 확인}
    A -->|없거나 불일치| F["401"]
    A -->|일치| T["create_jwt → access_token 발급"]
    T --> C["클라이언트가 Bearer로 API 요청"]
    C --> G["Depends(oauth2_scheme) → verify_token"]
    G -->|통과| B["보호된 리소스 조회"]
    G -->|실패| F2["401 반환"]
```

## 연습 문제

1. `/token`을 DB 사용자 테이블과 연결해 보세요.
2. `/users/search`가 부분 검색을 반환하도록 Query 파라미터를 추가하세요.
3. `Depends(oauth2_scheme)`를 사용하는 보호 라우터를 만드세요.
</contents>
