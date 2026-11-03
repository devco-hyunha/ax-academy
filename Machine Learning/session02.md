# 세션 02: Jupyter Notebook 설치 및 사용

Jupyter Notebook은 셀(Cell) 단위로 Python 코드를 실행하고, 실행 결과·시각화·설명을 한 문서에 함께 담는 도구입니다. 머신러닝 학습에서는 데이터 확인과 그래프 표시에 최적화되어 있어 가장 많이 사용됩니다.

> **이 세션이 하는 일 (쉬운 말)**  
> 오늘은 “머신 러닝 코드를 어디에 쓰고 어떻게 돌릴까?”를 해결합니다.  
> **Jupyter**라는 연습장을 설치하고, Cursor/VS Code에서도 같은 방식으로 셀을 실행하는 법을 익힙니다.  
> 단축키와 자주 나는 오류(503, 패키지 없음)까지 같이 정리합니다.

---

## 1. 설치 (Windows PowerShell 기준)

1. Python 설치 — [python.org](https://www.python.org/downloads/)에서 설치할 때 "Add Python to PATH" 체크
2. PowerShell을 열고 Jupyter 설치:
   ```powershell
   pip install jupyterlab
   pip install numpy pandas matplotlib scikit-learn
   ```
3. 실행:

   ```powershell
   cd "c:\AX Academy\study\Machine Learning"
   jupyter lab
   ```

   - 브라우저에 JupyterLab이 열리고, 좌측 파일 목록에서 `.ipynb` 파일 생성 → 더블클릭으로 열기

4. (선택) Anaconda/Miniconda를 쓰는 경우: 설치 시 Jupyter가 포함되어 있어 `Anaconda Prompt`에서 `jupyter lab` 실행만 하면 됨

### 설치 확인

```powershell
python -m pip list | Select-String -Pattern "jupyter|ipykernel|notebook|pandas|matplotlib"
```

- `ipykernel`, `jupyterlab`, `notebook`이 보이면 커널 준비 완료
- `pandas`, `matplotlib`가 없으면 ModuleNotFoundError의 원인 → `pip install pandas matplotlib`으로 설치

> **쉽게 이해하기**  
> **Jupyter**는 한 장에 **설명 + 코드 + 결과(그래프)** 를 같이 적어 두는 디지털 연습장입니다.  
> 파일 확장자는 `.ipynb` (notebook)입니다.
>
> 설치를 세 덩어리로 나누면 이해가 쉽습니다.
>
> 1. **Python**: 코드를 실행하는 엔진. PATH에 넣어야 터미널에서 `python`, `pip`가 됩니다.
> 2. **JupyterLab + 라이브러리**: 연습장 프로그램과, ML에 자주 쓰는 도구(`numpy`, `pandas` 등)
> 3. **실행**: `jupyter lab` → 브라우저가 열리고, 거기서 새 노트북을 만듭니다.
>
> **Anaconda**를 쓰면 Python·Jupyter가 묶음으로 들어오는 경우가 많습니다.  
> 그때는 **Anaconda Prompt**(아나콘다용 검은 창)를 열고 `jupyter lab`만 치면 됩니다.
>
> **커널(kernel)** = 노트북 뒤에서 실제로 Python을 돌리는 “엔진”.  
> 패키지가 안 보이면, 대개 **그 커널이 쓰는 Python**에 패키지가 없는 것입니다.

---

## 2. 에디터(Cursor/VS Code)에서 실행하는 방법 — 터미널 불필요

브라우저로 `jupyter lab`을 띄우지 않고, 에디터 안에서 셀을 실행할 수 있습니다. 에디터가 자체 Jupyter 서버를 띄우고 실행하는 방식입니다.

### 필수 확장: Jupyter 확장 (`ms-toolsai.jupyter`)

- 이 확장이 없으면 셀 실행도, `Jupyter: Restart Kernel` 명령도 존재하지 않습니다.
- 설치 방법 (둘 중 하나로):
  1. 확장 패널( 좌측 사각형 아이콘 `Ctrl+Shift+X`) → "Jupyter" 검색 → 설치
  2. 마켓 서버 문제가 있을 때의 오프라인 설치:
     - VSIX를 받아 설치: `cursor --install-extension "경로\jupyter.vsix"`
     - Open VSX( https://open-vsx.org )에서 `ms-toolsai.jupyter` VSIX 다운로드 → 위 명령으로 설치

### 실행 순서

1. `.ipynb` 파일 열기 → 우측 상단 **Select Kernel** → 설치한 Python(예: `2. Python 3.14.8 (miniconda)`) 선택
2. 셀 실행: `Ctrl + Enter` (현재 셀), `F5` (전체 실행)
3. 커널 재시작: `Ctrl+Shift+P` → `Jupyter: Restart Kernel`
4. 서버 문제가 반복되면: `Ctrl+Shift+P` → `Developer: Reload Window` (서버까지 재기동)

### 503 / ModuleNotFoundError 문제 해결 (실제 사례)

| 증상                                            | 원인                             | 조치                                                               |
| ----------------------------------------------- | -------------------------------- | ------------------------------------------------------------------ |
| `Server returned 503` (실행·설치 중)            | Jupyter 확장 마켓/서버 연결 문제 | 확장 설치 후 `Reload Window`, 네트워크 확인                        |
| `Jupyter: Restart Kernel` 메뉴 없음             | `ms-toolsai.jupyter` 확장 미설치 | 확장 설치 (VSIX 오프라인 설치 활용)                                |
| `ModuleNotFoundError: No module named 'pandas'` | 커널의 Python에 패키지 미설치    | 해당 커널 환경에 `pip install pandas matplotlib` 후 Restart Kernel |
| 셀은 되는데 출력이 안 남                        | 실행 기록이 셀에 저장 안 됨      | 셀 재실행 (`Ctrl+Enter`)                                           |

- pandas 3.x부터 `inplace=True`는 deprecation 경고 → 결과를 변수에 재대입하는 방식으로 사용

> **쉽게 이해하기**  
> Cursor나 VS Code에서도 `.ipynb`를 열면, 브라우저 Jupyter와 **같은 셀 실행**이 가능합니다.  
> 다만 **Jupyter 확장**이 반드시 필요합니다. 확장이 “에디터 ↔ Python 커널” 연결 담당입니다.
>
> 자주 하는 실수와 대응:
>
> - **커널을 안 고름**: 우측 상단 Select Kernel에서, 패키지 설치한 Python을 고릅니다.
> - **커널 재시작**: 변수·상태가 꼬였을 때 “엔진을 껐다 켜기”.  
>   `Ctrl+Shift+P` → `Jupyter: Restart Kernel`
> - **503 오류**: 확장/서버 쪽 연결 문제인 경우가 많습니다. 확장 설치 후 창 다시 로드.
> - **ModuleNotFoundError**: “그 커널의 Python”에 패키지가 없음 → 그 환경에 `pip install` 후 커널 재시작.
>
> `inplace=True`는 예전 습관인데, 새 pandas에서는 경고가 납니다.  
> `df = df.fillna(0)`처럼 **결과를 다시 변수에 넣는** 쪽이 안전합니다.

---

## 3. Notebook 기본 사용법

- **Code 셀**: Python 코드 작성 → `Ctrl + Enter`로 실행. 실행 결과가 셀 아래에 출력됨
- **Markdown 셀**: `Esc` 후 `M`으로 모드 전환 후 설명 작성 → `Ctrl + Enter`로 렌더링
- **단골 사용 순서**:
  1. 첫 셀: 라이브러리 임포트 (`import numpy as np` 등)
  2. 데이터 로드/확인 셀
  3. 전처리·시각화 셀
  4. 모델 학습·평가 셀

> **쉽게 이해하기**  
> 노트북은 **칸(셀)** 을 쌓아 올린 문서입니다.
>
> - **Code 셀**: 실행되는 파이썬. 결과가 바로 아래에 붙습니다.
> - **Markdown 셀**: 사람용 설명·제목. 실행하면 예쁜 문서로 보입니다.
>
> 실습할 때 흔히 쓰는 칸 배치:
>
> 1. 도구 가져오기 (`import …`)
> 2. 데이터 읽기·눈으로 확인
> 3. 손질·그림 그리기
> 4. 모델 학습·점수 보기
>
> 위에서 아래로 **이야기책처럼** 읽히게 쓰면, 나중에 본인도 다시 이해하기 쉽습니다.

---

## 4. 셀 추가·실행 단축키 (모드(mode) 기준)

셀이 **편집 모드**(커서가 셀 안에 있을 때)일 때 `Esc`를 누르면 **명령 모드**(테두리가 강조됨)로 전환되고, 아래 키가 동작합니다.

| 단축키                  | 동작                                                              |
| ----------------------- | ----------------------------------------------------------------- |
| `Esc` → `B`             | 현재 셀 **아래**에 새 셀 추가                                     |
| `Esc` → `A`             | 현재 셀 **위**에 새 셀 추가                                       |
| `Alt` + `Enter`         | 현재 셀 실행 + **아래에** 새 셀 자동 생성 (코드를 이어 갈 때 최고) |
| `Ctrl` + `Enter`        | 현재 셀만 실행                                                    |
| `Esc` → `M` / `Y` / `R` | 셀을 각각 Markdown / Code / Raw로 변경                            |
| `Esc` → `Enter`         | 편집 모드로 돌아감                                                |
| `Esc` → `DD`            | 현재 셀 삭제                                                      |
| `Esc` → `O`             | 셀 출력 열기/접기 토글                                            |
| `Tab`                   | 코드 자동완성, `Shift+Tab` = 함수 문서 확인                       |
| `Ctrl` + `S`            | 저장                                                              |

- 마우스로 추가도 가능: 상단 `+ New Cell` 버튼 (Code / Markdown 선택)

> **쉽게 이해하기**  
> Jupyter에는 두 가지 **모드(mode)** 가 있습니다. (중국어·중복 표기는 쓰지 않습니다.)
>
> - **편집 모드**: 셀 안에서 글자를 치는 상태. 커서가 깜빡입니다.  
>   이 상태에서는 `B`, `A` 같은 단축키가 “글자 입력”으로 먹혀 버립니다.
> - **명령 모드**: `Esc`를 눌러 셀 “밖”으로 나온 상태. 테두리가 강조됩니다.  
>   이제 `B`(아래 셀 추가), `A`(위 셀 추가), `DD`(삭제)가 동작합니다.
>
> **코드를 이어 갈 때** 가장 편한 키: `Alt + Enter`  
> → 지금 셀 실행 + 바로 아래 새 셀 생성.
>
> `Esc` → `M` = Markdown, `Esc` → `Y` = Code 로 셀 종류를 바꿉니다.

---

## 5. 실행 기준 폴더 (base directory)

- Jupyter는 **notebook 파일이 있는 폴더**를 기준으로 경로를 해석합니다.
- 예: notebook이 `Machine Learning/Jupyter/`에 있고 데이터가 `Machine Learning/data/train.csv`라면 → `pd.read_csv('../data/train.csv')`
- 절대경로가 항상 안전: `pd.read_csv(r'C:\AX Academy\study\Machine Learning\data\train.csv')`

> **쉽게 이해하기**  
> `pd.read_csv('data/train.csv')`처럼 **상대 경로**를 쓰면,  
> “지금 노트북이 있는 폴더”를 출발점으로 파일을 찾습니다.  
> 노트북 위치를 옮기면 같은 코드가 깨질 수 있습니다.
>
> - `../` = 한 단계 위 폴더
> - 헷갈리면 **절대 경로**(드라이브부터 전체 경로)가 안전합니다.  
>   Windows에서는 `r'C:\...'`처럼 `r`을 붙이면 역슬래시 이스케이프를 덜 걱정해도 됩니다.

---

## 6. 첫 셀에 넣는 연습 템플릿

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(np.__version__)   # numpy 버전 확인
print(pd.__version__)   # pandas 버전 확인
plt.plot([1, 2, 3, 4], [2, 4, 6, 8], marker='o', color='red')
plt.title("Jupyter 실행 테스트")
plt.show()
```

> 셀을 실행하면 버전 출력과 그래프가 셀 아래에 나타남. 위가 잘되면 세션 노트의 코드를 셀 단위로 하나씩 실행하며 따라가면 됩니다

> **쉽게 이해하기**  
> 이 셀은 “설치가 진짜 됐는지” 확인하는 **헬스 체크**입니다.  
> 버전 숫자가 찍히고 빨간 점 그래프가 나오면,  
> NumPy·Pandas·그림 그리기까지 **같은 커널**에서 준비된 것입니다.  
> 그다음부터는 세션 노트의 코드를 **한 셀씩** 옮겨 실행하면 됩니다.

---

## 복습 체크 (스스로)

1. Jupyter 노트북(`.ipynb`)의 장점을 한 문장으로 말해 보세요.
2. 편집 모드와 명령 모드의 차이는 무엇인가요? 어떻게 전환하나요?
3. Cursor에서 셀이 안 돌아가면 가장 먼저 확인할 것은 무엇인가요?
4. `ModuleNotFoundError: pandas`가 나면 보통 무엇을 해야 하나요?
5. `Alt + Enter`와 `Ctrl + Enter`의 차이는 무엇인가요?

<details>
<summary>답 보기</summary>

1. 코드·결과·설명을 한 문서에 셀 단위로 담아, 데이터 확인·그래프에 편리하다.
2. 편집 모드 = 셀 안 타이핑. 명령 모드 = Esc로 나와 단축키로 셀을 조작. Esc ↔ Enter로 전환.
3. Jupyter 확장(`ms-toolsai.jupyter`) 설치 여부와 Select Kernel(올바른 Python) 선택.
4. 그 커널의 Python 환경에 `pip install pandas` 후 Restart Kernel.
5. Ctrl+Enter = 현재 셀만 실행. Alt+Enter = 실행 + 아래 새 셀 생성(이어서 쓰기 좋음).

</details>
