# 레슨 1. FastAPI란 무엇인가

## 이번 레슨에서 배울 내용

- FastAPI의 정의와 핵심 철학
- 왜 FastAPI를 선택하는지
- ASGI와 비동기(async)의 개념

---

## 1. FastAPI 소개

**FastAPI**는 Python으로 현대적인 웹 API를 빠르게 만들기 위한 프레임워크입니다.  
Starlette(웹 파트)와 Pydantic(데이터 검증) 위에 구축되어 있습니다.


핵심 키워드:

```mermaid
flowchart LR
    C[클라이언트 요청] --> U[uvicorn (ASGI 서버)]
    U --> F[FastAPI 앱]
    F --> P[Pydantic 검증]
    P --> R[JSON 응답]
```

| 키워드 | 의미 |
|--------|------|
| 빠름 | Node.js, Go에 견줄 성능 (Starlette + uvicorn) |
| 생산성 | 적은 코드로 많은 기능 |
| 타입 기반 | Python 타입 힌트로 검증·문서·에디터 지원 |
| 표준 기반 | OpenAPI, JSON Schema 준수 |

---

## 2. 다른 프레임워크와의 비교

| 항목 | FastAPI | Flask | Django |
|------|---------|-------|--------|
| 타입 힌트 | 강력 (Pydantic) | 약함 | 보통 |
| 자동 문서 | 기본 제공 | 확장 필요 | 확장 필요 |
| 비동기 | 네이티브 | 제한적 | 최근 지원 확대 |
| 학습 곡선 | 중간 | 낮음 | 높음 |
| 적합한 용도 | API / 마이크로서비스 | 소규모 API | 풀스택 웹 |

API 서버를 만드는 목적이라면 FastAPI가 특히 잘 맞습니다.

---

## 3. ASGI와 비동기

- **WSGI**: 전통적인 동기 웹 인터페이스 (Flask, Django 기본)
- **ASGI**: 비동기·웹소켓을 지원하는 현대적 인터페이스

FastAPI는 ASGI 앱이므로 `uvicorn` 같은 ASGI 서버로 실행합니다.

```python
# 동기 엔드포인트도 가능
@app.get("/sync")
def sync_hello():
    return {"msg": "hello"}

# 비동기 엔드포인트 (I/O 대기 시 유리)
@app.get("/async")
async def async_hello():
    return {"msg": "hello"}
```

처음에는 동기/`async`를 섞어 써도 됩니다.  
DB·외부 API 호출처럼 **기다리는 작업**이 많을 때 `async`의 이점이 커집니다.

---

## 4. FastAPI가 잘하는 일

1. REST API / JSON API
2. 마이크로서비스 백엔드
3. ML 모델 서빙 (추론 API)
4. OpenAPI 기반 클라이언트 자동 생성

---

## 정리

- FastAPI = **빠른 + 타입 안전한 + 문서가 자동으로 나오는** Python API 프레임워크
- ASGI 기반으로 비동기 처리에 강합니다
- API 중심 백엔드에 특히 적합합니다

---

## 연습 문제

1. FastAPI의 데이터 검증을 담당하는 라이브러리 이름은 무엇인가요?
2. FastAPI 앱을 실행할 때 주로 쓰는 ASGI 서버는 무엇인가요?
3. Flask와 비교했을 때 FastAPI의 장점 두 가지를 적어 보세요.

<details>
<summary>정답 보기</summary>

1. Pydantic  
2. uvicorn  
3. 예: 자동 OpenAPI 문서, 타입 힌트 기반 검증, 높은 성능, 비동기 지원 등

</details>
