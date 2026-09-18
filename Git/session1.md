# Session 1 — 깃 핵심 기능 · 환경 설정 · 저장소

## 깃의 핵심 기능

### 1. 버전 관리

문서를 수정할 때마다 **언제, 무엇을 변경했는지** 기록한다.

```
초기코드 → 수정 → 수정2 → 최종
```

중요한 시점마다 세이브포인트를 만들어 되돌아갈 수 있다.

### 2. 백업

현재 컴퓨터의 자료를 다른 컴퓨터에 복제한다.

### 3. 협업

팀원이 누가 어느 부분을 어떻게 수정했는지 기록으로 남겨, 오류 발생 시 파악하기 쉽다.

---

## 깃 환경 설정

```bash
git config --global user.name "name"   # 이름 설정
git config --global user.email "email" # 이메일 설정
```

---

## 리눅스 기본 명령어

```bash
pwd      # 현재 위치 경로
ls       # 현재 디렉터리 파일/폴더 목록
ls -l    # 상세 정보 표시
clear    # 터미널 화면 정리
cd ..    # 상위 디렉터리로 이동
cd ~     # 홈 디렉터리로 이동
```

| 기호 | 의미 |
|------|------|
| `~` | 현재 사용자 홈 디렉터리 |
| `.` | 현재 작업 디렉터리 |
| `..` | 상위 디렉터리 |

---

## 디렉터리 만들고 삭제

```bash
cd {folder}       # change directory — 이동
mkdir {folder}    # make directory — 생성
ls                # 목록 확인
rm -r {folder}    # remove — 삭제
exit              # 종료
```

---

## 깃 저장소 만들기

1. 연동할 폴더 생성 후 해당 폴더로 이동
2. 깃 초기화

```bash
git init   # git initialize
```

성공 시 메시지 예:

```
Initialized empty Git repository in {folder}/.git/
```

→ Staging Area와 Repository가 생성된다.

```bash
ls -la   # .git 디렉터리 확인 (버전이 저장되는 저장소)
```

- **`.gitignore`**: 깃에 포함하지 않을 파일 목록
