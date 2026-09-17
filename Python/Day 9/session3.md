# [Day 9 - Session 3] CSV 데이터 처리 및 os 모듈 파일 시스템 제어

- **실습 파일**: `session3.py`
- **주요 내용**:
  - `csv` 모듈을 통한 표 형식 데이터 읽기 (`csv.reader` vs `csv.DictReader`)
  - `os.path`를 이용한 경로 유효성 검사 및 타입 판별 (`exists`, `isfile`, `isdir`)
  - 플랫폼 독립적 경로 추출 및 조합 (`dirname`, `basename`, `join`)
  - 디렉터리 순회(`os.listdir`) 및 파일 메타데이터(용량, `getsize`) 확인

---

## 1. 실습 코드 및 단계별 해설

### 1.1 CSV 파일 처리 (`csv.reader` vs `csv.DictReader`)

```python
import csv

weather1_path = 'C:/AX Academy/study/resource/weather1.csv'

# 1. csv.reader: 행(Row)을 리스트(List) 형태로 읽어옴
with open(weather1_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # 예: ['날짜', '지점', '평균기온'], ['2023-01-01', '108', '-1.5']

print('-' * 50)

# 2. csv.DictReader: 첫 번째 행(헤더)을 키(Key)로 삼아 각 행을 딕셔너리로 읽어옴
with open(weather1_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        for key, value in row.items():
            print(key, value)
```

- **`csv.reader`**: 각 행을 문자열 리스트로 반환하므로 인덱스 번호(`row[0]`, `row[1]`)로 접근합니다.
- **`csv.DictReader`**: 첫 줄의 헤더를 키로 매핑한 딕셔너리를 반환하므로 컬럼명(`row['날짜']`, `row['평균기온']`)으로 직관적으로 데이터에 접근할 수 있어 유지보수에 유리합니다.

---

### 1.2 `os.path`를 활용한 파일 및 경로 정보 검사

```python
import os

file_path = "C:/test2/a.txt"

# 1. 경로 존재 여부 확인
print(os.path.exists(file_path))  # True / False

# 2. 파일 및 디렉터리 여부 판별
print("파일 여부:", os.path.isfile(file_path))       # 파일이면 True
print("디렉토리 여부:", os.path.isdir(file_path))   # 폴더라면 True

# 3. 디렉터리 명과 파일 명 분리
dir_name = os.path.dirname(file_path)   # "C:/test2"
base_name = os.path.basename(file_path) # "a.txt"
print("디렉토리:", dir_name)
print("파일명:", base_name)

# 4. OS 독립적 경로 합성 (join)
# Windows의 역슬래시(\)나 POSIX의 슬래시(/)를 환경에 맞게 자동 처리
new_path = os.path.join(dir_name, "backup", "report_a.txt")
print("합친 경로:", new_path)  # "C:/test2/backup/report_a.txt"
```

- **`os.path.join()`**: 운영체제별 경로 구분자(Windows `\`, Linux/macOS `/`)를 자동으로 조합하여 하드코딩으로 인한 크로스 플랫폼 버그를 방지합니다.

---

### 1.3 디렉터리 내 파일 목록 순회 및 파일 크기 확인

```python
# 특정 디렉터리 내의 파일 목록 순회
target_dir = "."  # 현재 작업 디렉터리

for item in os.listdir(target_dir):
    full_path = os.path.join(target_dir, item)
    # 파일인 경우에만 크기 측정
    if os.path.isfile(full_path):
        size = os.path.getsize(full_path)  # 파일 크기를 바이트(Byte) 단위로 반환
        print(f"파일명: {item}, 크기: {size} bytes")
```

- **`os.listdir(dir)`**: 지정한 폴더 내의 모든 하위 파일 및 폴더 목록을 리스트로 반환합니다.
- **`os.path.getsize(path)`**: 파일의 물리적 크기를 바이트 단위의 정수로 반환합니다.

---

## 2. 핵심 요약 (Quick Reference)

| 모듈 / 함수 | 설명 |
| :--- | :--- |
| `csv.reader(f)` | 행 단위로 문자열 리스트 반환 |
| `csv.DictReader(f)` | 헤더를 Key로 갖는 사전 객체 반환 |
| `os.path.exists(path)` | 경로 존재 여부 반환 |
| `os.path.isfile(path)` / `isdir(path)` | 일반 파일 / 디렉터리 판별 |
| `os.path.dirname(path)` / `basename(path)` | 디렉터리 경로 / 파일 이름 분리 |
| `os.path.join(path1, path2, ...)` | OS 표준에 맞춘 안전한 경로 결합 |
| `os.listdir(path)` | 디렉터리 내의 모든 항목 이름 목록 반환 |
| `os.path.getsize(path)` | 파일의 바이트 단위 크기 반환 |
