# FastAPI 학습 커리큘럼

FastAPI를 처음부터 체계적으로 익히기 위한 단원별 학습 가이드입니다.

---

## 학습 목표

이 커리큘럼을 마치면 다음을 할 수 있습니다.

- FastAPI로 REST API를 설계하고 구현하기
- Pydantic으로 요청/응답 데이터 검증하기
- 의존성 주입, 라우터, 미들웨어로 프로젝트를 구조화하기
- DB 연동, 인증, 테스트를 포함한 실무형 API 만들기

---

## 권장 선수 지식

| 항목   | 수준                                    |
| ------ | --------------------------------------- |
| Python | 함수, 클래스, 타입 힌트 기초            |
| HTTP   | GET/POST/PUT/DELETE, JSON, 상태 코드    |
| 터미널 | 가상환경(venv/Miniconda) 및 패키지 설치 |

---

## 커리큘럼 목차

### [01. FastAPI 시작하기](./01-getting-started/)

1. [FastAPI란 무엇인가](./01-getting-started/01-what-is-fastapi.md)
2. [환경 설정과 첫 API](./01-getting-started/02-setup-and-first-api.md)
3. [자동 문서화 활용하기](./01-getting-started/03-auto-docs.md)

### [02. 경로·쿼리 매개변수](./02-path-query/)

1. [Path Parameters](./02-path-query/01-path-parameters.md)
2. [Query Parameters](./02-path-query/02-query-parameters.md)
3. [검증과 메타데이터](./02-path-query/03-validation-metadata.md)

### [03. 요청 본문과 Pydantic](./03-request-body/)

1. [Pydantic 모델 기초](./03-request-body/01-pydantic-basics.md)
2. [Request Body 다루기](./03-request-body/02-request-body.md)
3. [중첩 모델과 고급 검증](./03-request-body/03-nested-validation.md)

### [04. 응답 모델과 에러 처리](./04-response-errors/)

1. [Response Model](./04-response-errors/01-response-model.md)
2. [Status Codes](./04-response-errors/02-status-codes.md)
3. [에러 처리](./04-response-errors/03-error-handling.md)

### [05. 의존성 주입](./05-dependencies/)

1. [Depends 기초](./05-dependencies/01-depends-basics.md)
2. [실용 의존성 패턴](./05-dependencies/02-practical-patterns.md)
3. [체이닝과 클래스 의존성](./05-dependencies/03-chaining-classes.md)

### [06. 라우터와 프로젝트 구조](./06-routers-structure/)

1. [APIRouter](./06-routers-structure/01-api-router.md)
2. [프로젝트 구조화](./06-routers-structure/02-project-structure.md)
3. [설정 관리](./06-routers-structure/03-settings.md)

### [07. 데이터베이스 연동](./07-database/)

1. [SQLAlchemy / SQLModel 기초](./07-database/01-orm-basics.md)
2. [CRUD API 구현](./07-database/02-crud-api.md)
3. [비동기 DB와 팁](./07-database/03-async-tips.md)

### [08. 인증과 보안](./08-auth-security/)

1. [비밀번호 해싱과 회원가입](./08-auth-security/01-password-hashing.md)
2. [OAuth2와 JWT](./08-auth-security/02-oauth2-jwt.md)
3. [CORS와 미들웨어](./08-auth-security/03-cors-middleware.md)

### [09. 테스트와 배포](./09-testing-deploy/)

1. [API 테스트](./09-testing-deploy/01-testing.md)
2. [Docker 배포](./09-testing-deploy/02-docker.md)
3. [프로덕션 체크리스트](./09-testing-deploy/03-production-checklist.md)

---

## 학습 방법

1. 단원 README에서 목표를 확인합니다.
2. 레슨을 순서대로 읽고, 예제 코드를 직접 실행합니다.
3. 레슨 끝의 **연습 문제**를 풀어 봅니다.
4. 단원 마무리의 **체크리스트**로 복습합니다.

---

## 공통 환경 설정

venv 또는 Miniconda 중 하나만 사용하시면 됩니다. FastAPI 동작은 동일합니다.

### A. Miniconda (권장 — 이 프로젝트에서 사용 중)

```bash
# 환경 생성 (최초 1회)
conda create -n fastapi python=3.12 -y

# 환경 활성화
conda activate fastapi

# 필수 패키지
pip install "fastapi[standard]"
```

비활성화: `conda deactivate`  
환경 목록: `conda env list`

### B. venv

```bash
# 가상환경 생성 (Windows)
python -m venv venv
venv\Scripts\activate

# macOS / Linux
# source venv/bin/activate

# 필수 패키지
pip install "fastapi[standard]"
```

### 서버 실행

```bash
fastapi dev main.py
# 또는
uvicorn main:app --reload
```

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

> Miniconda를 쓰는 경우에도 FastAPI 패키지는 `pip install`로 설치하는 것을 권장합니다.
