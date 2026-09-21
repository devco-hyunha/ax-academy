# Session 6 — 깃 협업

하나의 원격 저장소를 **여러 지역 저장소**(집 PC / 회사 PC 등)에서 같이 쓰는 방법.

> session5의 `push` / `pull` / `origin` 개념을 전제로 한다.

---

## 1. 원격 저장소 복제 (`clone`)

다른 폴더·다른 PC에서 같은 원격을 쓰려면, 원격 내용을 지역으로 **통째로 가져온다**.

```bash
# 현재 폴더(.)로 복제
git clone https://github.com/{user}/{repo}.git .
```

실습 예: `test_home`, `test_office` 두 폴더를 각각 만들어 같은 원격을 clone  
→ clone하면 **이미 `origin`에 연결**되어 있다. (`git remote add` 불필요)

---

## 2. 여러 PC에서 pull / push

규칙: 지역이 2개 이상이면, 작업 전에 **원격의 최신 변경을 먼저** 가져온다.

### 집 (`test_home`)에서 올리고

```bash
git commit -am "add c"
git push
```

### 회사 (`test_office`)에서 받은 뒤 작업

```bash
git pull                 # 원격에 새로 올라온 커밋 받기
git commit -am "add d"
git push
```

### 집으로 돌아와 다시 맞추기

```bash
git pull                 # = git fetch + git merge
```

```
[ test_home ] ──push──► [ origin(원격) ] ◄──push── [ test_office ]
       ▲                      │                         │
       └──────── pull ────────┴──────── pull ───────────┘
```

---

## 3. 원격 브랜치 변화 (`fetch` → `merge`)

`pull`은 원격 커밋을 **바로 합친다**.  
최신 커밋을 당장 합치지 않고, **원격 정보만** 가져온 뒤 필요할 때 합칠 수 있다.

### 지역이 원격보다 앞선 경우

`test_home`에서 파일 추가 후 커밋:

```bash
git add t3.txt
git commit -m "create t3.txt"
git log --oneline
git status
```

| 포인터 | 가리키는 곳 |
|--------|-------------|
| `main` (지역) | 방금 만든 커밋 (`create t3.txt`) |
| `origin/main` (원격 추적) | 아직 예전 커밋 (`add d`) |

→ `status`에 “원격보다 앞서 있다, push 하라”고 나온다.

```bash
git push
git log --oneline
```

### 다른 PC에서 fetch만 하기

`test_office`로 이동:

```bash
git fetch                # 원격 최신 상태만 가져옴 (작업 트리는 그대로)
ls -al                   # t3.txt는 아직 안 보임 (merge 전)
git log --oneline
git status               # 원격보다 뒤처짐
```

차이와 병합:

```bash
git diff HEAD origin/main
git merge origin/main    # 원격에서 가져온 커밋을 지역에 합침
git log --oneline
```

---

## `pull` vs `fetch`

| 명령 | 동작 |
|------|------|
| `git fetch` | 원격 정보만 가져옴 (`origin/main` 갱신). 작업 파일은 안 바뀜 |
| `git merge origin/main` | 가져온 원격 커밋을 현재 브랜치에 합침 |
| `git pull` | `fetch` + `merge`를 한 번에 |

---

## 한눈에 보기

| 상황 | 명령어 |
|------|--------|
| 원격 복제 | `git clone {URL} .` |
| 최신 받아 바로 합치기 | `git pull` |
| 원격 정보만 가져오기 | `git fetch` |
| 지역 ↔ 원격 차이 | `git diff HEAD origin/main` |
| fetch 후 합치기 | `git merge origin/main` |
| 지역 커밋 올리기 | `git push` |
