# Game — 대학생 시뮬레이터

CLI 기반 **대학생 인생 시뮬레이터**. 12개월 동안 매월 행동을 선택해 스탯을 키우고, 이벤트·엔딩으로 결말을 낸다.

**인트로 → 캐릭터 생성/이어하기 → 로비 → 월간 스케줄 → 엔딩** 본편 루프와  
**캐릭터 영속화**(`CharacterServices` ↔ `DataManager` ↔ `resources/character.json`)가 연결되어 있다.

---

## 1. 프로젝트 개요

| 항목        | 내용                                              |
| ----------- | ------------------------------------------------- |
| 실행 진입점 | `Game/main.py`                                    |
| 장르        | 텍스트 기반 턴제 시뮬레이션                       |
| UI          | 터미널 입출력 (CLI)                               |
| 영속화      | `resources/character.json` (세이브 슬롯 최대 8개) |
| 아키텍처    | Controller / Service / View / Manager / Config    |

**핵심 규칙** (`config/constants.py`)

| 항목           | 값                                               |
| -------------- | ------------------------------------------------ |
| 총 개월        | 12 (`TOTAL_MONTHS`)                              |
| 월당 행동 슬롯 | 3 (`MONTHLY_ACTIONS`)                            |
| 슬롯당 일수    | 10 (`DAYS_PER_ACTION`)                           |
| 스탯 범위      | 0 ~ 100 (`money` 제외)                           |
| 초기 스탯      | 소지금 1,500,000 / 지능·매력·체력 5 / 스트레스 0 |
| 아웃컴 확률    | 대성공 10% / 성공 60% / 실패 25% / 대실패 5%     |
| 아웃컴 배율    | ×2 / ×1 / ×0.7 / ×0.5 (`Fraction`)               |

---

## 2. 디렉터리 구조

```
Portfolio/Game/
├── main.py
├── utils.py                          # 한글 표시 너비·패딩
├── config/
│   ├── constants.py                  # STATUS/CODE, 턴·아웃컴 규칙
│   ├── defaultData.py                # CHARACTER_TEMPLATE, DEFAULT_DATA
│   ├── actions.py                    # 행동 8종 + weight/messages
│   ├── events.py                     # 고정·조건·랜덤 이벤트
│   └── endings.py                    # 엔딩 7종
├── controllers/
│   ├── scene_controller.py           # 인트로 / 생성·이어하기 / 로비
│   └── schedule_controller.py        # 월간 스케줄·일별 진행·엔딩
├── services/
│   ├── character_services.py         # 캐릭터 CRUD ↔ DataManager
│   ├── actions_services.py           # 행동 선택·일별 적용
│   ├── event_services.py             # 고정/조건/랜덤 이벤트
│   ├── ending_service.py             # get_ending(stats)
│   └── math_quiz.py                  # 중간/기말 수학 퀴즈
├── managers/
│   ├── data_manager.py               # 키 기반 CRUD
│   └── file_manager.py               # JSON I/O
├── views/
│   ├── system_views.py               # 공통 UI
│   ├── intro_views.py
│   ├── character_views.py            # 생성·로비·세이브 목록
│   └── schedule_views.py             # 스케줄·일 로그·엔딩 표시
└── resources/
    └── character.json                # 세이브 슬롯 목록 (list)
```

실행 시 `Game/resources/`가 없으면 Manager가 기본값으로 생성한다.

---

## 3. 아키텍처 & 데이터 흐름

```
main
  └─ DataManager (store) ── FileManager ── resources/*.json
  └─ SceneController
        ├─ CharacterServices(store)
        ├─ ScheduleController
        │     ├─ ActionsServices
        │     ├─ EventServices
        │     ├─ CharacterServices(store)
        │     ├─ get_ending
        │     └─ ScheduleViews / CharacterViews
        ├─ IntroViews
        └─ CharacterViews
```

### 플레이 흐름

1. `main` → `DataManager` → `SceneController.intro()`
2. 인트로: **새로하기 / 이어하기 / 종료**
3. 새로하기: 이름 입력 → `createCharacter` → lobby  
   이어하기: 세이브 목록 선택 → `loadCharacter` → lobby
4. 로비: 스탯 표시 → **스케줄 관리** / **뒤로가기**
5. 스케줄: 월 슬롯 3개 선택(고정 이벤트 슬롯 포함) → 일별 큐 실행
6. 매일: 행동 적용 또는 이벤트 진행 → `saveCharacter` → dayLog 표시
7. 월 종료 → 다음 달 / 12월이면 `get_ending` → `showEnding` → ending 저장

### 계층 역할

| 계층           | 역할                                       |
| -------------- | ------------------------------------------ |
| **Controller** | 메뉴 분기, 씬·월 루프, Service·View 조합   |
| **Service**    | 캐릭터·행동·이벤트·엔딩·퀴즈 도메인 로직   |
| **View**       | 표시·입력만 (조회하지 않음)                |
| **Manager**    | 키 기반 CRUD, JSON read/write, 기본값 seed |
| **Config**     | 규칙·행동·이벤트·엔딩 정적 데이터          |

결과 객체는 `{ status, code, data }` (`STATUS` / `CODE`).

---

## 4. 모듈별 상세

### 4.1 Controllers

**SceneController**

| 메서드         | 상태 | 설명                                                   |
| -------------- | ---- | ------------------------------------------------------ |
| `intro()`      | ✅   | 새로하기 / 이어하기 / 종료                             |
| `start()`      | ✅   | 이름 입력 → `createCharacter` → lobby (중복 시 재입력) |
| `chooseSave()` | ✅   | 세이브 목록 UI → `loadCharacter` → lobby               |
| `lobby()`      | ✅   | 스탯·메뉴, ending 있으면 종료                          |
| `exit()`       | ✅   | `sys.exit(0)`                                          |

**ScheduleController**

| 메서드                  | 상태 | 설명                                           |
| ----------------------- | ---- | ---------------------------------------------- |
| `scheduleSelection()`   | ✅   | 슬롯 선택(소지금 검사) → `runMonth` → next/end |
| `initializeSchedules()` | ✅   | 달력 고정 이벤트를 슬롯에 배치                 |
| `runDayQueue()`         | ✅   | pending / fixed / action → 이벤트 판정         |
| `enrichEventDayLog()`   | ✅   | event_services 결과 → 표시용 필드 보강         |
| `nextMonth()`           | ✅   | 월 종료 UI·스탯 → `month += 1` → 저장          |
| `endGame()`             | ✅   | `get_ending` → `showEnding` → ending 저장      |
| `saveCharacter()`       | ✅   | `CharacterServices.saveCharacter` 호출         |

### 4.2 Services

**CharacterServices** — DataManager 연동

| 메서드                               | 설명                                                         |
| ------------------------------------ | ------------------------------------------------------------ |
| `findAllCharacters()`                | `store.findAll('character')`, 최대 8슬롯                     |
| `createCharacter(name, birth_month)` | 슬롯 가득 참 / 중복 이름 / unknown 자동부여 → `store.create` |
| `loadCharacter(index)`               | 슬롯 인덱스로 로드 → `playCharacter` 지정                    |
| `saveCharacter(character)`           | `store.update` (사일런트 오토세이브)                         |

- 이름 미입력 → `unknown`, `unknown 2`, … 자동 부여
- 중복 이름 → `CODE['DUPLICATE_NAME']` 반환 (컨트롤러에서 재입력)
- 슬롯 8개 초과 → `SLOT_FULL` 반환

**ActionsServices**

- `findAllActions` / `buildDayQueue`
- `selectScheduleAction`: 소지금 부족 시 `INSUFFICIENT_MONEY`
- `rollOutcome` / `calcDayDelta` / `applyDay`: weight × 배율, day_log 생성

**EventServices**

- 고정 일정: `getCalendarEvents` / `applyFixedEventDay`
- 조건·랜덤: `findTriggeredEvent` / `toPendingEvent` / `applyEventDay`
- 상호작용: `math_quiz` · `choice` · 효과만 적용
- 퀴즈 판정: score ≥8 대성공 / ≥5 성공 / ≥2 실패 / 그 외 대실패

**고정 이벤트 달력**

| 월  | 이벤트        | 슬롯 |
| --- | ------------- | ---- |
| 4   | 중간고사      | 2    |
| 5   | 대학 축제     | 2    |
| 6   | 기말고사      | 2    |
| 11  | 졸업 프로젝트 | 2    |

**ending_service** — `get_ending(stats)` → `ENDINGS` 항목 반환  
**math_quiz** — `runMathQuiz(difficulty, time_limit) -> int`

### 4.3 Managers

**FileManager** — `{basePath}/resources/{key}.json` read/write  
**DataManager** — `findAll` / `findBy` / `create` / `update` / `delete` / `save` / `load`, `id` 자동 채번

- `DEFAULT_DATA['character']` = `[]` (세이브 슬롯 목록)
- `create`는 리스트에 append 후 `id` 부여

### 4.4 Views

| View             | 역할                                                                  |
| ---------------- | --------------------------------------------------------------------- |
| `SystemViews`    | headline / subtitle / menu / choice / input / errorMessage            |
| `IntroViews`     | 타이틀, 메뉴 3종                                                      |
| `CharacterViews` | 캐릭터 생성(제목·이름 입력), 로비 타이틀·스탯 바, 세이브 목록(최대 8) |
| `ScheduleViews`  | 스케줄 선택, monthStart/End, dayLog, insufficientMoney, showEnding    |

### 4.5 Config

**스키마** (`defaultData.py`)

| 상수                 | 용도                                 |
| -------------------- | ------------------------------------ |
| `CHARACTER_TEMPLATE` | 새 캐릭터 생성용 단일 dict 템플릿    |
| `DEFAULT_DATA`       | 파일 저장소 기본값 (`character: []`) |

**주요 CODE** (캐릭터 관련)

| CODE                 | 용도                       |
| -------------------- | -------------------------- |
| `DUPLICATE_NAME`     | 캐릭터 이름 중복           |
| `DUPLICATE_DATA`     | 일반 데이터 중복           |
| `SLOT_FULL`          | 세이브 슬롯 8개 가득 참    |
| `SAVE_FAILED`        | 캐릭터 저장 실패           |
| `INSUFFICIENT_MONEY` | 스케줄 선택 시 소지금 부족 |

**행동** (`ACTIONS`, 8종)

| ID  | 이름       |
| --- | ---------- |
| 1   | 취업 준비  |
| 2   | 아르바이트 |
| 3   | 외관 관리  |
| 4   | 쇼핑       |
| 5   | 건강 관리  |
| 6   | 영어 공부  |
| 7   | 돈 모으기  |
| 8   | 휴식/여가  |

각 행동에 `weights` · 아웃컴별 `messages`가 있다.

**이벤트** (`EVENTS`)

| ID                                | 유형 | 비고                |
| --------------------------------- | ---- | ------------------- |
| `midterm` / `final_exam`          | 고정 | `math_quiz`         |
| `festival` / `graduation_project` | 고정 | `choice`            |
| `illness`                         | 조건 | stress ≥ 80, 월 1회 |
| `travel`                          | 랜덤 | 7~9월               |
| `mock_interview`                  | 랜덤 | 7~12월              |

**엔딩** (`ENDINGS` + `get_ending` 조건 요약)

| ID              | 이름        | 대략 조건                     |
| --------------- | ----------- | ----------------------------- |
| `large_company` | 대기업 취업 | 지능≥75, 매력≥60, 스트레스≤50 |
| `abroad`        | 해외 도피   | 지능≥70, 소지금≥3,000,000     |
| `startup`       | 창업        | 소지금≥6,000,000, 지능≥60     |
| `youtuber`      | 유튜버      | 매력≥75                       |
| `labor`         | 노가다      | 체력≥80, 지능\<40             |
| `sme`           | 중소기업    | 지능≥50, 스트레스≤70          |
| `unemployed`    | 백수        | 그 외                         |

---

## 5. 캐릭터 데이터 모델

### 템플릿 (`CHARACTER_TEMPLATE`)

```python
{
  'name': 'unknown',
  'turn': 0,
  'month': 1,
  'stats': {
    'money': 1_500_000,
    'intelligence': 5,
    'charm': 5,
    'stamina': 5,
    'stress': 0,
  },
  'history': [],
  'action_counts': {},
  'events_triggered': [],
  'pending_event': None,
  'ending': None,
}
```

저장 시 `DataManager.create`가 `id`를 부여한다.

### 파일 (`resources/character.json`)

```python
[
  { 'id': 1, 'name': '...', 'month': 1, ... },
  { 'id': 2, 'name': '...', 'month': 3, ... },
]
```

세이브 UI는 `name`, `month`, `turn`, `ending`을 표시한다.

---

## 6. 구현 완성도

| 영역                    | 상태 | 비고                                 |
| ----------------------- | ---- | ------------------------------------ |
| 인트로·로비 UI          | ✅   |                                      |
| 공통 CLI UI             | ✅   |                                      |
| JSON Manager            | ✅   |                                      |
| 스케줄 선택·소지금 검사 | ✅   |                                      |
| 일별 행동·아웃컴        | ✅   |                                      |
| 고정/조건/랜덤 이벤트   | ✅   |                                      |
| 수학 퀴즈               | ✅   |                                      |
| 엔딩 판정·표시          | ✅   |                                      |
| 일 로그·엔딩 View       | ✅   |                                      |
| 캐릭터 영속화           | ✅   | create / findAll / load / save       |
| 새 게임 이름·저장       | ✅   | `CharacterViews` + `createCharacter` |
| 이어하기                | ✅   | 실제 세이브 목록에서 로드            |

---

## 7. 팀 구성 & 역할 분담

| 구분 | 이름   | 담당                                         |
| ---- | ------ | -------------------------------------------- |
| 본인 | 지현하 | 프로젝트 골격·본편 루프·계층 연동·UI/Manager |
| 팀원 | 오효정 | 이벤트 데이터·이벤트 서비스·수학 퀴즈        |
| 팀원 | 정진규 | 엔딩 판정 서비스                             |
| 팀원 | 임유빈 | 캐릭터 CRUD·DataManager 영속화               |

### 지현하 (본인)

- CLI 아키텍처 골격 (`main`, Controller / Service / View / Manager / Config)
- 인트로·로비·스케줄 선택 UI 및 씬 흐름 (`SceneController`, `*Views`)
- 월간 스케줄 실행 루프·일별 행동/고정 이벤트 처리 (`ScheduleController`, `ActionsServices`)
- JSON 영속화 기반 (`DataManager`, `FileManager`, `defaultData`)
- 팀원 모듈 연동 (이벤트·퀴즈·엔딩 → 스케줄/엔딩 플로우)
- 새 게임 이름 입력·이어하기 UI 연결, `Game.md` 정리

### 오효정

- 이벤트 정적 데이터 (`config/events.py`) — 고정·조건·랜덤
- 이벤트 도메인 로직 (`event_services.py`) — 달력/트리거/적용
- 중간·기말 수학 퀴즈 (`math_quiz.py`)

### 정진규

- 엔딩 판정 (`ending_service.py` — `get_ending(stats)`)

### 임유빈

- 캐릭터 서비스 (`character_services.py`)
  - `createCharacter` / `findAllCharacters` / `loadCharacter` / `saveCharacter`
  - 세이브 슬롯 8개·이름 중복·unknown 자동 부여
  - `DataManager` create/update 연동

---

## 8. 실행 방법

```bash
cd Portfolio/Game
python main.py
```

---

_기준 경로: `Portfolio/Game/`_
