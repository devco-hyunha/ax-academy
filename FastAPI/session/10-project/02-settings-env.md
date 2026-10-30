# 레슨 2. .env · Settings · Alembic

## 이번 레슨에서 배울 내용

- `requirements.txt`와 초기 패키지 설치
- `.env` 파일과 Settings 클래스
- Alembic으로 테이블 구조를 관리하는 방법

---

## 1. 초기 설치

```bash
pip install alembic sqlalchemy pymysql asyncmy cryptography passlib
pip install python-dotenv pydantic-settings

pip freeze > requirements.txt   # 현재 환경의 패키지와 버전을 파일로 저장
alembic init alembic            # Alembic 초기화
```

| 패키지 | 역할 |
|--------|------|
| alembic | DB 마이그레이션 (테이블 구조 변경 자동화) |
| sqlalchemy | ORM (파이썬 객체로 DB 다루기) |
| pymysql | MySQL 드라이버 (동기 방식) |
| asyncmy | MySQL 드라이버 (비동기 방식, FastAPI와 잘 맞음) |
| cryptography | 암호화 (토큰, 비밀번호) |
| passlib | 비밀번호 해싱 (bcrypt) |
| python-dotenv | `.env`를 환경 변수로 로드 |
| pydantic-settings | `.env` 값을 검증된 설정 객체로 변환 |

`requirements.txt`는 다른 환경에서 동일한 패키지를 설치할 수 있게 해 줍니다.

---

## 2. Settings 클래스

`BaseSettings`를 상속받은 Settings 클래스는 환경 변수나 설정 파일에서 자동으로 값을 로드합니다.

```python
# app/core/settings.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="allow")

    DB_USER: str
    DB_PASSWORD: str
    JWT_SECRET: str

    populate_by_name = True  # 환경 변수 이름을 클래스 속성명에 매핑


settings = Settings()
```

| 옵션 | 의미 |
|------|------|
| `case_sensitive = True` | 환경 변수 이름을 대소문자 구분 |
| `extra = "allow"` | 추가 값이 있어도 예외를 발생시키지 않음 |
| `populate_by_name = True` | 환경 변수 이름을 클래스 속성명에 매핑 |

`.env`에 DB 정보, JWT 정보를 저장합니다.

```env
DB_USER=root
DB_PASSWORD=1234
JWT_SECRET=dev-secret
```

---

## 3. database.py

SQLAlchemy로 비동기(async) 및 동기(sync) 엔진과 SessionLocal을 설정합니다.

```python
# app/db/database.py
from app.core.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.database_url)
SessionLocal = sessionmaker(engine, class_=AsyncSession)
```

---

## 4. main.py

FastAPI 인스턴스를 생성하고, CORS 미들웨어를 설정하며, lifespan 동안 테이블을 생성합니다.

```python
# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.database import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(...)   # lifespan 동안 테이블 생성
    yield


app = FastAPI(lifespan=lifespan)
```

---

## 5. Alembic 환경 설정

`alembic/env.py`는 마이그레이션에 필요한 환경(DB 연결 URL, 타겟 메타데이터)을 설정합니다.

- `app.core.settings`에서 DB URL을 가져옴
- `app.db.database.Base`, `app.db.models`의 모델을 `target_metadata`로 설정

```mermaid
flowchart LR
    A["모델 변경"] --> B["alembic revision --autogenerate"]
    B --> C["alembic upgrade head"]
    C --> DB[(DB에 적용)]
```

`create_all`은 학습용으로, 실서비스 스키마 변경은 Alembic으로 관리합니다.
