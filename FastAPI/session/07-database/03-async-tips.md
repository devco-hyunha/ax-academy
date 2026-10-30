# 레슨 3. 비동기 DB와 팁

## 이번 레슨에서 배울 내용

- 동기 vs 비동기 세션
- 마이그레이션(Alembic) 개념
- 실무에서 자주 하는 실수

---

## 1. 언제 async인가?

| 상황                           | 추천               |
| ------------------------------ | ------------------ |
| 학습 / 내부 도구 / 트래픽 낮음 | 동기 세션으로 충분 |
| 높은 동시성, 외부 I/O 많음     | 비동기 세션 검토   |

비동기는 “무조건 빠름”이 아니라, **대기 시간 동안 다른 요청을 처리**하는 모델입니다.

---

## 2. 비동기 맛보기 (SQLAlchemy 2.0 스타일)

```bash
pip install sqlalchemy[asyncio] aiosqlite
```

```python
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine("sqlite+aiosqlite:///./app.db")
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
```

엔드포인트도 `async def`로 맞춥니다.

```python
@app.get("/items")
async def list_items(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Item))
    return result.scalars().all()
```

학습 초기에는 동기 SQLModel CRUD를 먼저 완성하는 것을 권장합니다.

---

## 3. Alembic (마이그레이션)

`create_all`은 프로토타입에 적합합니다.  
스키마가 바뀌는 실서비스에서는 **Alembic**으로 버전 관리합니다.

```bash
pip install alembic
alembic init migrations
```

개념만 기억하세요.

1. 모델 변경
2. revision 생성 (autogenerate)
3. `alembic upgrade head`로 적용

---

## 4. 자주 하는 실수

1. **세션을 전역 하나로 공유** → 요청마다 새 세션
2. **commit 후 refresh 누락** → id가 비어 보임
3. **N+1 쿼리** → 관계 로딩 전략 검토
4. **스키마에 비밀번호 포함** → Read 모델 분리
5. **SQLite + 멀티스레드** → `check_same_thread=False` 등 옵션 확인

```python
engine = create_engine(
    "sqlite:///./app.db",
    connect_args={"check_same_thread": False},
)
```

---

## 정리

- 동기 CRUD를 탄탄히 한 뒤 async로 확장하세요
- 운영 스키마 변경은 Alembic
- 세션 생명주기와 응답 모델 분리가 품질을 가릅니다

```mermaid
flowchart LR
    M["모델 변경"] --> R["revision 생성 (autogenerate)"]
    R --> U["alembic upgrade head"]
    U --> DB[(스키마 적용)]
```

---

## 연습 문제

1. 동기 `get_session`과 비동기 `get_async_session`의 차이를 적어 보세요.
2. `create_all`만으로 부족한 이유를 설명해 보세요.
3. Hero 목록에 `limit` 최대 100 제한을 의존성/Query로 넣으세요.
