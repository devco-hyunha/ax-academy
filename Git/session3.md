# Session 3 — 작업 되돌리기 (restore · reset · revert)

## 1. 수정사항 폐기 (`restore`)

스테이징 **전**, 작업 트리의 수정만 버릴 때:

```bash
git restore {file}
```

→ 해당 파일의 수정사항을 폐기한다.

---

## 2. 스테이징 되돌리기

```bash
git add {file}
git status
git restore --staged {file}   # 스테이징만 취소 (수정 내용은 유지)
git status
```

---

## 3. 최신 커밋 되돌리기 (`reset`)

```bash
git commit -am "메시지명"
git log
git reset HEAD^    # 커밋만 취소, 수정 내용은 남김
```

---

## 4. 특정 커밋으로 되돌리기

예시 커밋 흐름:

```bash
git add hi3.txt
git commit -m "H1"
# 코드 수정 후
git commit -am "H2"
git commit -am "H3"
git commit -am "H4"
```

H2 이후 커밋을 없애고 H2로 이동:

```bash
git reset --hard {H2커밋해시}   # 커밋 + 스테이징 + 작업 내용까지 전부 삭제
# git reset --soft {해시}       # 커밋만 취소 (수정·스테이징 유지)
git log
```

---

## 5. 커밋 이력은 남기고 취소 (`revert`)

커밋을 취소하되 **기록은 남겨두고** 싶을 때:

```bash
git commit -am "H5"
git log
git revert {H5커밋해시}
git log
```

→ 취소용 커밋이 **새로 추가**된다.

---

## reset vs revert

| 구분 | reset | revert |
|------|-------|--------|
| 기존 커밋 | 브랜치에서 제거 | 삭제하지 않음 |
| 새 커밋 생성 | X | O |
| 히스토리 변경 | O (위험) | X (안전) |
| 협업 브랜치 | 위험 | 안전 |
| reflog | 복구에 필요 | 거의 불필요 |

**한 줄 정리**

- **reset** = 과거로 돌아감 (히스토리 변경)
- **revert** = 과거는 두고, 취소 커밋 하나 추가

> 이미 원격에 push한 커밋에 `reset --hard`를 쓰면 다른 사람 기록이 꼬인다.  
> 협업 중에는 `revert`를 쓰는 것이 안전하다.
