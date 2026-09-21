# Session 7 — merge vs rebase

## 1. merge와 rebase의 기본 개념

두 기능 모두 **다른 브랜치의 변경 사항을 가져오는 작업**이지만 히스토리를 다루는 방식이 다르다.

초기 상태:
```text
A - B - C  (main)
         \
          D - E  (feature)
```

`main`에 새 커밋 `F`가 추가됨:
```text
A - B - C - F  (main)
         \
          D - E  (feature)
```

---

## 2. merge 방식

`feature` 브랜치에서 실행:

```bash
git merge main
```

결과:
```text
A - B - C - F  (main)
         \     \
          D - E - M  (feature)
```

- `M`이라는 **새로운 머지 커밋(Merge Commit)**이 생긴다.
- 브랜치가 갈라졌다가 다시 합쳐진 기록이 그대로 남는다.

---

## 3. rebase 방식

`feature` 브랜치에서 실행:

```bash
git rebase main
```

결과:
```text
A - B - C - F (main)
             \
              D' - E' (feature)
```

- 머지 커밋이 생성되지 않는다.
- 기존 커밋(`D`, `E`)을 떼어내어 `main`의 최신 커밋(`F`) 뒤에 **새로운 커밋(`D'`, `E'`)으로 다시 작성**한다.
- 히스토리가 한 줄로 깔끔하게 정렬된다.

---

## 4. rebase를 사용하는 이유와 주의점

### 언제 쓰는가?
- 커밋 히스토리를 깔끔한 일직선으로 유지하고 싶을 때
- 팀 프로젝트에서 PR(Pull Request)을 올리기 전 최신 기준점으로 맞출 때
- 내 작업 내용을 최신 `main` 브랜치 기준으로 다시 붙이고 싶을 때

### pull 할 때의 rebase 옵션

로컬과 원격이 서로 다른 커밋을 가지고 있을 때 동기화 방식:

```bash
# 기본 방식: 원격 변경 사항을 가져와 머지 커밋 생성
git pull --no-rebase

# rebase 방식: 원격 커밋을 가져온 뒤 내 로컬 커밋을 그 위에 재정렬
git pull --rebase
```

---

## 5. merge vs rebase 한눈에 비교

| 구분 | merge | rebase |
|------|-------|--------|
| 새 커밋 생성 | O (머지 커밋 생성) | X (기존 커밋을 새 해시로 재생성) |
| 히스토리 형태 | 갈라지고 합쳐진 흔적 보존 | 일직선으로 단순화 |
| 히스토리 재작성 | X | O (커밋 해시 변경됨) |
| 원격 협업 안전성 | 안전 | 이미 원격에 푸시된 브랜치는 주의 필요 |
