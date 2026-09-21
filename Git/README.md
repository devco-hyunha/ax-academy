# Git 학습 정리

| 세션 | 주제 | 핵심 명령어 |
|------|------|-------------|
| [session1](./session1.md) | 핵심 기능 · 환경 설정 · 저장소 | `git config`, `git init` |
| [session2](./session2.md) | 버전 관리 (add → commit) | `git status`, `git add`, `git commit`, `git log` |
| [session3](./session3.md) | 작업 되돌리기 | `git restore`, `git reset`, `git revert` |
| [session4](./session4.md) | 브랜치 | `git branch`, `git switch`, `git merge` |
| [session5](./session5.md) | 깃허브 (원격) | `git remote`, `git push`, `git pull`, SSH |
| [session6](./session6.md) | 깃 협업 | `git clone`, `git fetch`, `git pull` |
| [session7](./session7.md) | merge vs rebase | `git merge`, `git rebase`, `git pull --rebase` |
| [session8](./session8.md) | VS Code 소스 제어 & 워크플로우 | GUI 스테이징·커밋·브랜치, PR 협업 흐름 |
| [session9](./session9.md) | README 파일 | 프로젝트 안내 문서 구조 및 작성법 |

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
