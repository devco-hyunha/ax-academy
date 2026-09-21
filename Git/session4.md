# Session 4 — 브랜치

협업하고 안전하게 개발하기 위한 **작업용 공간**.

---

## 1. 브랜치를 쓰는 이유

### 기존 코드 보호

메인 브랜치(`main`/`master`)는 안정적인 코드가 있어야 한다.  
새 기능을 main에서 직접 만들면 코드를 망가뜨릴 위험이 있다.

→ 브랜치를 따로 만들어 작업해야 main이 안전하게 유지된다.

### 여러 작업 동시에 진행

팀원마다 기능별 브랜치를 만들면 서로 영향을 주지 않고 **병렬 개발**이 가능하다.

### 기록 · 협업 · 롤백

- 협업에 적합
- 버전 관리와 롤백이 쉬움  
  → 브랜치마다 시점이 달라, 이전 상태로 돌아가거나 특정 기능을 되살리기 쉽다.

---

## 2. 브랜치 기능

| 동작          | 설명                                       |
| ------------- | ------------------------------------------ |
| 분기 (branch) | main에서 새 브랜치를 만드는 것             |
| 병합 (merge)  | 작업이 끝난 브랜치 내용을 main에 합치는 것 |

---

## 3. 실습 — 저장소 · 브랜치 만들기

폴더 생성 후 VS Code에서 연다. 깃을 쓰려면 저장소로 만든다.

```bash
git init
git add test.txt
git commit -m "test 1"
git log

# 내용 추가 후 커밋
git commit -am "test 2"
git commit -am "test 3"
```

공통 설명서를 완성한 뒤, 고객사마다 다른 설명서가 필요한 상황이면  
디렉터리를 복사하는 대신 **브랜치**를 쓴다. (예: naver, google, ms)

```bash
git branch          # 목록 확인 (저장소 생성 시 main이 기본)
git branch naver    # 새 브랜치 생성
git branch google
git branch ms
git branch          # 확인
git log
```

→ 새로 만든 브랜치도 최신 커밋이 `test 3`이다. (분기 시점의 커밋을 공유)

---

## 4. 실습 — 새 커밋 추가

```bash
git commit -am "main test 4"
git log --oneline
```

- `main test 4`는 **현재 브랜치(main)**에만 적용된다.
- naver / google / ms는 아직 `test 3` 상태.

→ 커밋은 **지금 작업 중인 브랜치**에만 쌓인다.  
브랜치가 여러 개면, 브랜치마다 서로 다른 커밋을 만들 수 있다.

### 브랜치 전환 (`switch`)

```bash
git switch naver
git log --oneline
```

- naver를 만들기 전까지 main에 있던 커밋은 naver에도 그대로 있다.
- `test.txt`에는 분기 전 내용(3개 행)만 보인다.

---

## 5. 실습 — 브랜치에서 커밋하기

전환한 브랜치에서 `test.txt` 수정 + `naver.txt` 생성 후:

```bash
git add .
git commit -m "naver test 4"
git log --oneline              # 현재 naver, 최신 = naver test 4
```

### 브랜치와 커밋 관계

```bash
git log --oneline --branches   # 브랜치별 최신 커밋 한눈에
```

### 브랜치 간 차이

커밋이 많아지면 차이를 보기 어렵다. `..`(점 2개)로 비교한다.

```bash
git log main..naver    # main에는 없고 naver에만 있는 커밋
git log naver..main    # naver에는 없고 main에만 있는 커밋
```

---

## 6. 실습 — 브랜치 병합

새 폴더(`git_manual2`)에서:

```bash
git init
git add test.txt
git commit -m "test1"

git branch j2

# main에서
git add main.txt
git commit -m "main test 2"

# j2에서
git switch j2
git add j2.txt
git commit -m "j2 test 2"

git log --oneline --branches
git log --oneline --branches --graph
```

- `test1`은 main·j2가 공유
- main에는 `main test 2`, j2에는 `j2 test 2`

VS Code: `Ctrl + Shift + P` → **Git Graph: View Git Graph**

### j2 → main 병합

병합 전에 **받을 쪽 브랜치(main)**로 먼저 전환한다.

```bash
git switch main
git merge j2
git log --oneline --branches --graph
```

---

## 7. 병합 — 다른 위치 수정 (충돌 없음)

새 폴더(`git_manual3`)에서 같은 파일의 **다른 줄**을 수정하면 자동 병합된다.

```bash
git init
git add test.txt
git commit -m "test 1"
git branch jw2

# main에서 일부 줄 수정
git commit -am "main test 2"

git switch jw2
# jw2에서 다른 줄 수정
git commit -am "jw2 test 2"

git switch main
git merge jw2    # 충돌 없이 병합
```

---

## 8. 병합 — 같은 위치 수정 (충돌)

같은 줄을 양쪽에서 고치면 **충돌**이 난다.

```bash
git switch main
git merge jw2
```

1. 충돌 메시지 → **Resolve in Merge Editor** 클릭
2. jw2 / main / 병합 결과 3분할 화면
3. main 수락 · jw2 수락 체크 (순서대로 반영)
4. 병합 결과를 스테이징 후 커밋

```bash
git commit -am "merge jw2 branch"
git log --oneline --branches --graph
```

### merge 취소

커밋 전에만 abort 가능. (이미 커밋하면 merge 완료 → abort 불가)

```bash
git merge --abort
```

---

## 9. 브랜치 삭제

```bash
git branch
git branch -d jw2    # 일반 삭제 (병합된 브랜치만)
git branch           # 확인
git branch -D jw2    # 강제 삭제 (= -d -f)
```

같은 이름으로 다시 만들면, 예전 브랜치의 커밋은 히스토리/reflog 등으로 다시 찾을 수 있는 경우가 있다.

---

## 10. 강제 옵션 (`-f` / `--force`)

`-f`는 **강제(force)**. 이미 있거나, 수정이 남아 있어도 실행한다.  
잘못 쓰면 수정·히스토리가 날아갈 수 있으니 주의.

### 브랜치 위치 강제 이동 (`git branch -f`)

이미 있는 브랜치를 **다른 커밋으로 옮길** 때:

```bash
git branch -f naver main
# naver 포인터를 main이 가리키는 커밋으로 강제 이동
```

- 브랜치가 없으면 → 새로 생성
- 브랜치가 이미 있으면 → `-f` 없이 옮기려 하면 실패

### 브랜치 전환 강제 (`git switch -f`)

저장하지 않은 수정이 있어도 **버리고** 브랜치를 바꾼다.

```bash
git switch -f naver
# 또는
git checkout -f naver
```

→ 로컬 수정이 사라질 수 있다. 가능하면 `git restore`로 정리한 뒤 전환하는 편이 안전하다.

### `-d` / `-D` / `-f` 구분

| 옵션 | 뜻 |
|------|-----|
| `-d` | 병합된 브랜치만 삭제 |
| `-D` | 병합 안 됐어도 강제 삭제 (`-d -f`와 같음) |
| `-f` | 브랜치 이동·전환 등에서 “있어도/수정 있어도 강제” |

---

## 한눈에 보기

| 상황 | 명령어 |
|------|--------|
| 브랜치 목록 | `git branch` |
| 브랜치 생성 | `git branch {이름}` |
| 브랜치 전환 | `git switch {이름}` |
| 브랜치 위치 강제 이동 | `git branch -f {이름} {기준}` |
| 전환 강제 (수정 버림) | `git switch -f {이름}` |
| 브랜치별 로그 | `git log --oneline --branches --graph` |
| A에만 있는 커밋 | `git log B..A` |
| 병합 | `git switch main` → `git merge {브랜치}` |
| 병합 취소 (커밋 전) | `git merge --abort` |
| 브랜치 삭제 | `git branch -d {이름}` / `-D` (강제) |
