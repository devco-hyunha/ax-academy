# Session 2 — 버전 관리

## 버전이란?

수정 내용이 쌓이면 번호를 붙여 **이전 상태와 구별**하는 것.  
문서를 수정하고 저장할 때마다 생긴다.

---

## 버전 만드는 3단계

```
[ Working Directory ]  ← 내가 수정하는 파일 (작업 트리)
         ↓  git add
[ Staging Area ]       ← 커밋 대기실 (스테이지)
         ↓  git commit
[ Repository ]         ← 커밋 기록 저장소
```

| 단계 | 설명 | 예시 |
|------|------|------|
| 작업 트리 | 파일 수정·저장을 하는 디렉터리 | `jw-git` |
| 스테이지 | 버전으로 만들 파일이 대기하는 곳 | — |
| 저장소 | 스테이지 파일을 버전으로 저장하는 곳 | `.git` |

흐름: 작업트리에서 수정 → 원하는 파일만 스테이지에 올림 → 커밋하면 버전 생성

---

## 1. 상태 확인

```bash
git status
```

- **Untracked files**: 아직 한 번도 버전 관리하지 않은 파일 (작업 트리에만 존재)

### 변경 사항 비교

파일 수정·저장 후, 저장소의 파일과 어떻게 다른지 확인:

```bash
git diff
```

---

## 2. 스테이징 (`git add`)

작업 트리의 변경 사항을 스테이지에 올린다.  
= 깃에게 **버전 만들 준비**를 시킨다.

```bash
git add {file}   # 특정 파일만
git add .        # 전부
```

올린 뒤 확인:

```bash
git status
```

→ `Changes to be committed`에 스테이징된 파일 목록이 보인다.

---

## 3. 커밋 (`git commit`)

스테이지에 있는 파일로 버전을 만든다.

```bash
git commit -m "메시지명"
```

- 변경 사항을 알아볼 수 있도록 **메시지를 반드시 기록**한다.
- 커밋 후 스테이지 파일이 저장소에 추가된다.

---

## 4. 로그 확인 (`git log`)

```bash
git log            # 커밋 이력
git log --oneline  # 한 줄 요약
git log --stat     # 커밋 + 관련 파일 요약
```

### 변경 사항 상세 보기

커밋에서 무엇이 바뀌었는지 보고 싶을 때:

| 옵션 | 설명 |
|------|------|
| `git log --stat` | 파일별 몇 줄 수정됐는지 요약 |
| `git log -p` / `--patch` | 추가·삭제된 코드 전체 diff (가장 상세) |
| `git log --name-only` | 변경된 파일 이름만 |
| `git log --name-status` | 파일 이름 + 상태 (`M` 수정, `A` 추가, `D` 삭제) |

### 출력 형식 바꾸기

로그를 한 줄로 보거나, 원하는 정보만 골라 볼 때:

| 옵션 | 설명 |
|------|------|
| `git log --oneline` | 해시 앞부분 + 메시지만 한 줄로 |
| `git log --graph` | 브랜치·머지 흐름을 텍스트 그래프로 |
| `git log --decorate` | 브랜치·태그 이름 함께 표시 |
| `git log --format="..."` | 출력 형식 직접 지정 |

```bash
# 해시 · 작성자 · 상대 시간 · 메시지
git log --format="%h - %an, %ar : %s"
```

자주 쓰는 조합:

```bash
git log --oneline --graph --decorate
```

### 범위·조건으로 걸러내기

특정 커밋만 골라보고 싶을 때:

| 옵션 | 설명 | 예시 |
|------|------|------|
| `--author="이름"` | 특정 작성자 | `git log --author="kim"` |
| `--grep="단어"` | 메시지에 단어 포함 | `git log --grep="fix"` |
| `--since` / `--until` | 기간 지정 | `git log --since="2 weeks ago"` |
| `-n <숫자>` | 최근 N개만 | `git log -n 5` |
| `<b1>..<b2>` | b1에는 없고 b2에만 있는 커밋 | `git log main..feature` |

---

## 실습 한 줄 흐름

```bash
# 수정 후
git status
git diff
git add .
git commit -m "메시지"
git log --oneline
```
