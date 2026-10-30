# 레슨 3. 설정 관리

## 이번 레슨에서 배울 내용

- 환경 변수와 `.env`
- `pydantic-settings` 사용
- 개발/운영 설정 분리

---

## 1. 설치

```bash
pip install pydantic-settings
```

---

## 2. Settings 클래스

```python
# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    app_name: str = "My FastAPI App"
    debug: bool = False
    database_url: str = "sqlite:///./app.db"
    secret_key: str = "change-me"


settings = Settings()
```

`.env` 예:

```env
APP_NAME=Learning API
DEBUG=true
DATABASE_URL=sqlite:///./dev.db
SECRET_KEY=dev-secret
```

환경 변수 이름은 필드명의 대문자 형태와 매칭됩니다.

---

## 3. 앱에서 사용

```python
from fastapi import FastAPI
from config import settings

app = FastAPI(title=settings.app_name)


@app.get("/info")
def info():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
    }
```

---

## 4. 의존성으로 주입

```python
from functools import lru_cache
from fastapi import Depends
from typing import Annotated


@lru_cache
def get_settings() -> Settings:
    return Settings()


SettingsDep = Annotated[Settings, Depends(get_settings)]


@app.get("/config-check")
def config_check(s: SettingsDep):
    return {"debug": s.debug}
```

`lru_cache`로 설정 객체를 한 번만 로드합니다.  
테스트 시 `get_settings.cache_clear()` 후 override 할 수 있습니다.

---

## 5. 보안 주의

- `.env`는 **절대 Git에 커밋하지 마세요** (`.gitignore`에 추가)
- `SECRET_KEY`, DB 비밀번호는 운영 시 시크릿 저장소/환경 변수로
- `debug=True`는 운영에서 금지

`.gitignore` 예:

```text
.env
.venv/
venv/
__pycache__/
```

---

## 정리

- 설정은 코드에 하드코딩하지 말고 Settings로 모으세요
- `.env` + 환경 변수로 환경을 전환합니다
- 비밀 값은 버전 관리에서 제외하세요

```mermaid
flowchart LR
    ENV["`.env` (APP_NAME, DEBUG, DATABASE_URL)"] --> S["Settings (BaseSettings)"]
    EV["환경 변수 (.env보다 우선)"] --> S
    S --> A["FastAPI 앱 / Depends(get_settings) 주입"]
```

---

## 연습 문제

1. `Settings`에 `api_prefix: str = "/api/v1"`을 추가하세요.
2. `.env`로 `DEBUG`를 바꿔 `/info` 응답이 바뀌는지 확인하세요.
3. `secret_key` 기본값을 운영에 쓰면 안 되는 이유를 설명해 보세요.
