# Session 5 — 깃허브 (원격 저장소)

## 원격 저장소란?

지역 저장소와 원격 저장소를 연결해 버전 관리 파일을 **쉽게 백업**할 수 있다.

| 구분 | 설명 |
|------|------|
| 지역 저장소 (local) | 내 컴퓨터에 있는 저장소 |
| 원격 저장소 (remote) | 깃허브 등 다른 컴퓨터/서버에 있는 저장소 |

| 동작 | 설명 |
|------|------|
| `push` | 지역 → 원격으로 커밋을 올림 |
| `pull` | 원격 → 지역으로 커밋을 내려받음 |

### 깃허브로 할 수 있는 일

- 원격에서 깃 사용
- 협업 프로젝트
- 지역 저장소 백업
- 온라인 개발 툴 사용
- 개발 이력 남기기

---

## 1. 지역 저장소 준비

```bash
git init
git add t1.txt
git commit -m "add a"
git log
```

---

## 2. 원격 저장소에 연결

깃허브에서 만든 저장소 URL을 연결한다.  
`origin` = 원격 저장소의 **기본 별칭**.

```bash
git remote add origin https://github.com/{user}/{repo}.git
git remote -v    # 연결 확인 (fetch / push URL)
```

---

## 3. 지역 ↔ 원격 동기화

### 처음 푸시

```bash
git branch -M main              # 브랜치 이름을 main으로
git push -u origin main         # upstream 설정 + 첫 푸시
```

- `-u` (`--set-upstream`): 이후부터는 `git push` / `git pull`만으로 가능

### 이후 푸시

```bash
git commit -am "add b"
git push
```

### 원격에서 직접 커밋한 뒤 내려받기

깃허브 웹에서 파일을 만들거나 수정하면 지역과 **버전 차이**가 생긴다.  
→ `pull`로 맞춘다.

```bash
git pull origin main
git log
```

---

## 4. SSH 원격 접속

**SSH (Secure Shell)**: 프라이빗 키 · 퍼블릭 키로 기기를 깃허브에 인증하는 방식.

### 키 생성

```bash
cd ~                                    # 홈 디렉터리
ssh-keygen -t ed25519 -C "email@example.com"
# Enter로 진행하면 키 생성

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

키 확인: `cd ~/.ssh` → `ls -la`

### 깃허브에 퍼블릭 키 등록

```bash
clip < ~/.ssh/id_ed25519.pub            # Windows: 클립보드 복사
```

깃허브: **Settings → SSH and GPG keys → New SSH Key**  
→ 복사한 퍼블릭 키 붙여넣기

### SSH 주소로 연결 · 푸시

```bash
git init
git remote add origin git@github.com:{user}/{repo}.git
git remote -v

git add t.txt
git commit -m "text ssh"
git branch -M main                      # 브랜치 이름을 main으로 (-m / -M)
git push -u origin main
```

### 원격 강제 푸시 (`-f` / `--force`)

로컬 히스토리를 원격에 **덮어쓸** 때. 원격 커밋이 지워질 수 있어 위험하다.

```bash
git push -f origin main
# 또는
git push --force origin main

# 권장(더 안전): 다른 사람이 먼저 push한 경우에만 막음
git push --force-with-lease origin main
```

→ 협업 브랜치에서는 `push -f`를 피한다. 원격 기록이 꼬일 수 있다.

---

## 한눈에 보기

| 상황 | 명령어 |
|------|--------|
| 원격 추가 | `git remote add origin {URL}` |
| 원격 확인 | `git remote -v` |
| 브랜치 이름 → main | `git branch -M main` |
| 첫 푸시 | `git push -u origin main` |
| 이후 푸시 | `git push` |
| 원격 내려받기 | `git pull` / `git pull origin main` |
| 원격 강제 푸시 | `git push -f` / `--force-with-lease` |
| SSH 키 생성 | `ssh-keygen -t ed25519 -C "{email}"` |
| 퍼블릭 키 복사 | `clip < ~/.ssh/id_ed25519.pub` |

> 참고: [Notion — 깃허브](https://app.notion.com/p/22e974c0f4ae805b8638d8fb37d65f27) 수업자료 중 「깃허브」 페이지
