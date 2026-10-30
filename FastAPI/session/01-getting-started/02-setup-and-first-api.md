# 레슨 2. 환경 설정과 첫 API

## 이번 레슨에서 배울 내용

- 가상환경과 패키지 설치
- 최소 Hello World API 작성
- 서버 실행과 요청 확인

---

## 1. 환경 준비

격리된 Python 환경이 필요합니다. **Miniconda** 또는 **venv** 중 하나를 사용하세요.

### 방법 A. Miniconda

```bash
# 환경 생성 (최초 1회)
conda create -n fastapi python=3.12 -y

# 환경 활성화
conda activate fastapi

# FastAPI 설치
pip install "fastapi[standard]"
```

| 명령                            | 설명           |
| ------------------------------- | -------------- |
| `conda activate fastapi`        | 환경 켜기      |
| `conda deactivate`              | 환경 끄기      |
| `conda env list`                | 환경 목록 확인 |
| `conda remove -n fastapi --all` | 환경 삭제      |

### 방법 B. venv

```bash
# 프로젝트 폴더에서
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
# source venv/bin/activate

pip install "fastapi[standard]"
```

### 설치 확인

`fastapi[standard]`를 설치하면 uvicorn, 개발용 CLI 등이 함께 포함됩니다.

```bash
python -c "import fastapi; print(fastapi.__version__)"
```

> Miniconda와 venv의 차이는 “환경을 만드는 도구”뿐입니다. FastAPI 코드·실행 결과는 같습니다.

---

## 2. 첫 번째 앱 만들기

`main.py` 파일을 만들고 아래 코드를 작성합니다.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
```

핵심 구조:

1. `FastAPI()` 인스턴스 생성 → `app`
2. `@app.get("/경로")` 데코레이터로 라우트 등록
3. 함수의 return 값이 자동으로 JSON 응답이 됨

---

## 3. 서버 실행

```bash
fastapi dev main.py
```

또는:

```bash
uvicorn main:app --reload
```

- `main` = 파일 이름 (`main.py`)
- `app` = FastAPI 인스턴스 변수명
- `--reload` = 코드 변경 시 자동 재시작 (개발용)

브라우저에서 http://127.0.0.1:8000 을 열어 보세요.

```json
{ "message": "Hello, FastAPI!" }
```

---

## 4. HTTP 메서드 맛보기

```python
from fastapi import FastAPI

app = FastAPI()

items = {"1": {"name": "노트북"}}


@app.get("/items/{item_id}")
def get_item(item_id: str):
    return items.get(item_id, {"error": "not found"})


@app.post("/items")
def create_item(name: str):
    new_id = str(len(items) + 1)
    items[new_id] = {"name": name}
    return {"id": new_id, "name": name}
```

| 메서드 | 용도      | 데코레이터    |
| ------ | --------- | ------------- |
| GET    | 조회      | `@app.get`    |
| POST   | 생성      | `@app.post`   |
| PUT    | 전체 수정 | `@app.put`    |
| PATCH  | 부분 수정 | `@app.patch`  |
| DELETE | 삭제      | `@app.delete` |

---

## 5. curl로 확인하기

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
```

Windows PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/
```

---

## 정리

- 가상환경 → `pip install "fastapi[standard]"` → `main.py` → `fastapi dev`
- `@app.get("/")`처럼 데코레이터로 엔드포인트를 정의합니다
- return dict → JSON 응답으로 자동 변환됩니다

```mermaid
flowchart LR
    V[가상환경 activate] --> P["pip install 'fastapi[standard]'"]
    P --> M["main.py 작성"]
    M --> U["fastapi dev main.py"]
    U --> D["http://127.0.0.1:8000 + /docs"]
```


---

## 연습 문제

1. `/hello/{name}` 경로로 GET 요청 시 `{"greeting": "안녕하세요, {name}님"}`을 반환하는 엔드포인트를 만드세요.
2. `/sum?a=3&b=5`처럼 쿼리로 두 수를 받아 합을 반환하는 GET 엔드포인트를 만드세요.
3. 서버를 `--reload` 없이 실행하는 명령어를 적어 보세요.

<details>
<summary>힌트 / 정답 예시</summary>

```python
@app.get("/hello/{name}")
def hello(name: str):
    return {"greeting": f"안녕하세요, {name}님"}


@app.get("/sum")
def calc_sum(a: int, b: int):
    return {"result": a + b}
```

실행: `uvicorn main:app` (또는 `fastapi run main.py`)

</details>
