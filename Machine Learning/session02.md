# 세션 02: Jupyter Notebook 설치 및 사용

Jupyter Notebook은 셀(Cell) 단위로 Python 코드를 실행하고, 실행 결과·시각화·설명을 한 문서에 함께 담는 도구입니다. 머신러닝 학습에서는 데이터 확인과 그래프 표시에 최적화되어 있어 가장 많이 사용됩니다.

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

4. (선택) Anaconda/Miniconda를 쓰는 경우: 설치 시 Jupyter가 포함되어 있어 `AnaPrompt`에서 `jupyter lab` 실행만 하면 됨

### 설치 확인

```powershell
python -m pip list | Select-String -Pattern "jupyter|ipykernel|notebook|pandas|matplotlib"
```

- `ipykernel`, `jupyterlab`, `notebook`이 보이면 커널 준비 완료
- `pandas`, `matplotlib`가 없으면 ModuleNotFoundError의 원인 → `pip install pandas matplotlib`으로 설치

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

### 503 / ModuleNotFoundError troubleshooting (실제 사례)

| 증상                                            | 원인                             | 조치                                                               |
| ----------------------------------------------- | -------------------------------- | ------------------------------------------------------------------ |
| `Server returned 503` (실행·설치 중)            | Jupyter 확장 마켓/서버 연결 문제 | 확장 설치 후 `Reload Window`, 네트워크 확인                        |
| `Jupyter: Restart Kernel` 메뉴 없음             | `ms-toolsai.jupyter` 확장 미설치 | 확장 설치 (VSIX 오프라인 설치 활용)                                |
| `ModuleNotFoundError: No module named 'pandas'` | 커널의 Python에 패키지 미설치    | 해당 커널 환경에 `pip install pandas matplotlib` 후 Restart Kernel |
| 셀은 되는데 출력이 안 남                        | 실행 기록이 셀에 저장 안 됨      | 셀 재실행 (`Ctrl+Enter`)                                           |

- pandas 3.x부터 `inplace=True`는 deprecation 경고 → 결과를 변수에 재대입하는 방식으로 사용

## 3. Notebook 기본 사용법

- **Code 셀**: Python 코드 작성 → `Ctrl + Enter`로 실행. 실행 결과가 셀 아래에 출력됨
- **Markdown 셀**: `Esc` 후 `M`으로 모드 전환 후 설명 작성 → `Ctrl + Enter`로 렌더링
- **단골 사용 순서**:
  1. 첫 셀: 라이브러리 임포트 (`import numpy as np` 등)
  2. 데이터 로드/확인 셀
  3. 전처리·시각화 셀
  4. 모델 학습·평가 셀

## 4. 셀 추가·실행 단축키 (mode/命令 모드 기준)

셀이 **편집 모드**(커널 커점)일 때 `Esc`를 누르면 **mode 모드**(테두리)로 전환되고, 아래 키가 동작합니다.

| 단축키                  | 동작                                                              |
| ----------------------- | ----------------------------------------------------------------- |
| `Esc` → `B`             | 현재 셀 **아래**에 새 셀 추가                                     |
| `Esc` → `A`             | 현재 셀 **위**에 새 셀 추가                                       |
| `Alt` + `Enter`         | 현재 셀 실행 + **아래에** 새 셀 자동 생성 (코이를 이어할 때 최고) |
| `Ctrl` + `Enter`        | 현재 셀만 실행                                                    |
| `Esc` → `M` / `Y` / `R` | 셀을 각각 Markdown / Code / Raw로 변경                            |
| `Esc` → `Enter`         | 편집 모드로 돌아감                                                |
| `Esc` → `DD`            | 현재 셀 삭제                                                      |
| `Esc` → `O`             | 셀 출력 열기/접기 토글                                            |
| `Tab`                   | 코드 자동완성, `Shift+Tab` = 함수 문서 확인                       |
| `Ctrl` + `S`            | 저장                                                              |

- 마우스로 추가도 가능: 상단 `+ New Cell` 버튼 (Code / Markdown 선택)

## 5. 실행 기준 폴더 (base directory)

- Jupyter는 **notebook 파일이 있는 폴더**를 기준으로 경로를 해석합니다.
- 예: notebook이 `Machine Learning/Jupyter/`에 있고 데이터가 `Machine Learning/data/train.csv`라면 → `pd.read_csv('../data/train.csv')`
- 절대경로가 항상 안전: `pd.read_csv(r'C:\AX Academy\study\Machine Learning\data\train.csv')`

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
