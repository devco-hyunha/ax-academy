# Git 학습 정리

| 세션 | 주제 | 핵심 명령어 |
|------|------|-------------|
| [session1](./session1.md) | 핵심 기능 · 환경 설정 · 저장소 | `git config`, `git init` |
| [session2](./session2.md) | 버전 관리 (add → commit) | `git status`, `git add`, `git commit`, `git log` |
| [session3](./session3.md) | 작업 되돌리기 | `git restore`, `git reset`, `git revert` |

## 전체 흐름

```
Working Directory  →  git add  →  Staging Area  →  git commit  →  Repository
     (작업 트리)                      (대기실)                        (저장소)
```

## 되돌리기 한눈에

| 상황 | 명령어 |
|------|--------|
| 수정만 버리고 싶을 때 (스테이징 전) | `git restore {file}` |
| 스테이징만 취소 | `git restore --staged {file}` |
| 커밋 취소 + 수정 내용 유지 | `git reset HEAD^` / `git reset --soft` |
| 커밋·수정 전부 삭제 | `git reset --hard {해시}` |
| 기록은 남기고 취소 | `git revert {해시}` |
