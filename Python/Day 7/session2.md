# [Day 7 - Session 2] 파일 입출력 응용: 성적 누적 기록 및 평균 집계, 예외 처리

- **실습 파일**: `session2.py`
- **주요 내용**:
  - `with` 블록을 활용한 안전한 파일 입출력 자원 관리
  - 파일 추가 쓰기 모드(`'a'`)를 통한 지속적인 데이터 로깅
  - 파일 읽기(`'r'`) 및 줄 단위 파싱(`strip()`, `split()`)
  - 파일 부재 예외(`FileNotFoundError`) 안전 처리

---

## 1. 실습 코드 및 단계별 해설

### 1.1 데이터 누적 기록: `score1()`

```python
def score1(name, score):
  with open('./score1.txt', 'a', encoding='UTF-8') as f:
    f.write(f'{name}, {score}\n')

score1('홍길동', 100)
score1('김길동', 90)
```

- **설명**:
  - 파일 모드 `'a'`(Append)를 사용하여 기존 파일의 내용을 덮어쓰지 않고 파일 끝에 새로운 학생 성적 데이터를 누적하여 기록합니다.
  - `encoding='UTF-8'`을 명시하여 한글 깨짐 현상을 방지합니다.
  - `with open(...)` 문을 통해 파일 작업 완료 후 자동으로 스트림이 닫히도록(`close`) 보장합니다.

---

### 1.2 데이터 읽기 및 평균 계산: `average()`

```python
def average():
  sum = 0
  cnt = 0
  try:
    with open('./score1.txt', 'r', encoding='UTF-8') as f:
      lines = f.readlines()
      for i in lines:
        i = i.strip()
        name, score = i.split(',')
        if score: 
          sum += int(score.strip())
          cnt += 1
    return (sum / cnt)
  except FileNotFoundError:
    print('파일이 없습니다')

avg = average()
print(avg)  # 출력: 95.0
```

- **설명**:
  - `f.readlines()`: 파일 전체 내용을 각 행을 원소로 갖는 리스트 형태로 읽어옵니다.
  - `i.strip()`: 줄 끝의 개행 문자(`\n`) 및 양쪽 공백을 제거합니다.
  - `i.split(',')`: 쉼표를 기준으로 이름(`name`)과 점수(`score`)를 언패킹 분리합니다.
  - `sum += int(score.strip())`: 점수 문자열을 정수형(`int`)으로 변환하여 누적 합산하고, 카운터(`cnt`)를 1 증가시킵니다.
  - `try - except FileNotFoundError`: 해당 파일이 존재하지 않는 경우 프로그램이 비정상 종료되지 않고 안내 메시지를 출력하도록 방어 처리합니다.

---

## 2. 핵심 요약 및 비교

| 파일 모드 | 특징 | 사용 예시 |
| :--- | :--- | :--- |
| `'w'` (Write) | 기존 내용이 있으면 전부 지우고 새로 작성 | 초기화, 새로운 파일 생성 |
| `'a'` (Append) | 기존 내용을 유지하며 파일 끝에 내용 추가 | 로그 기록, 데이터 누적 (`score1.txt`) |
| `'r'` (Read) | 파일 읽기 전용 (파일이 없으면 `FileNotFoundError` 발생) | 데이터 조회, 통계 계산 |

- **안전한 데이터 처리 팁**: 빈 줄이나 형식에 맞지 않는 데이터가 섞여 있을 경우를 대비하여 `len(parts) == 2` 검증이나 `cnt == 0`일 때의 `ZeroDivisionError` 방어 처리를 추가하면 더욱 견고한 코드가 됩니다.
