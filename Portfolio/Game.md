# Game — 대학생 시뮬레이터 분석

CLI 기반의 **대학생 인생 시뮬레이터**다. 12개월 동안 매월 행동을 선택해 스탯을 키우고, 이벤트·엔딩으로 결말을 내는 구조를 목표로 한다. 현재는 **인트로 → 세이브 선택 → 로비 → 스케줄 선택** 흐름까지 연결되어 있고, 캐릭터 영속화·행동 적용·엔딩 판정은 스켈레톤 단계다.

---

## 1. 프로젝트 개요

| 항목 | 내용 |
|------|------|
| 실행 진입점 | `Game/main.py` |
| 장르 | 텍스트 기반 턴제 시뮬레이션 |
| UI | 터미널 입출력 (CLI) |
| 영속화 | `resources/*.json` (JSON 파일) |
| 아키텍처 | Controller / Service / View / Manager / Config 계층 분리 |

**핵심 규칙 (설계값, `config/constants.py`)**

- 총 **12개월** (`TOTAL_MONTHS`)
- 월당 **행동 3회** (`MONTHLY_ACTIONS`), 행동당 **10일** (`DAYS_PER_ACTION`)
- 스탯 범위 `0 ~ 100` (`STAT_MIN` / `STAT_MAX`)
- 초기 스탯: 재력 500, 지능·매력·체력 5, 스트레스 0

---

## 2. 디렉터리 구조

```
Portfolio/Game/
├── main.py                      # 앱 기동, DataManager + SceneController 연결
├── utils.py                     # 한글 표시 너비 계산·패딩 (터미널 정렬)
├── config/                      # 상수·스키마·콘텐츠 데이터
│   ├── constants.py             # STATUS/CODE, 스탯·아웃컴·턴 규칙
│   ├── defaultData.py           # character 기본 스키마
│   ├── actions.py               # 선택 가능 행동 + 스탯 weight
│   ├── events.py                # 이벤트(아픔, 번아웃) mock
│   └── endings.py               # 엔딩 정의
├── controllers/                 # 씬·플로우 제어
│   ├── scene_controller.py      # 인트로 / 세이브 / 로비
│   └── schedule_controller.py   # 월간 스케줄 선택·월 진행
├── services/                    # 도메인 로직
│   ├── character_services.py
│   └── actions_services.py
├── managers/                    # 데이터 CRUD·파일 I/O
│   ├── data_manager.py
│   └── file_manager.py
└── views/                       # 터미널 UI
    ├── system_views.py          # 공통 headline / subtitle / menu / choice
    ├── intro_views.py
    ├── character_views.py       # 로비 스탯·세이브 목록
    └── schedule_views.py        # 월간 행동 선택 UI
```

실행 시 `Game/resources/` 폴더가 자동 생성되며, 키별 JSON 파일이 저장된다.

---

## 3. 아키텍처 & 데이터 흐름

```
main
  └─ DataManager (store) ── FileManager ── resources/*.json
  └─ SceneController
        ├─ CharacterServices(store)
        ├─ ScheduleController
        │     ├─ CharacterServices(store)
        │     └─ ScheduleViews
        ├─ IntroViews
        └─ CharacterViews
```

### 기동·플레이 흐름

1. `main`이 `Game` 디렉터리 경로로 `DataManager` 생성
2. `SceneController(store)` 생성 후 `intro()` 호출
3. 인트로 메뉴: **새로하기 / 이어하기 / 종료**
4. 이어하기 → 세이브 선택 → `lobby(character)`
5. 로비: 스탯 표시 → **스케줄 관리** 또는 **뒤로가기**
6. 스케줄 관리 → `ScheduleController.scheduleSelection()` → 월 증가 / 엔딩 stub

### 계층 역할

| 계층 | 역할 |
|------|------|
| **Controller** | 메뉴 분기, 씬 전환, Service·View 조합 |
| **Service** | 캐릭터 생성·로드·저장, (예정) 행동 처리 |
| **View** | 타이틀·메뉴·입력 검증 등 출력만 담당 |
| **Manager** | 키 기반 CRUD, JSON read/write, 기본값 seed |
| **Config** | 게임 규칙·행동·이벤트·엔딩 등 정적 데이터 |

결과 객체는 대체로 `{ status, code, data }` 형태로 통일되어 있다 (`STATUS` / `CODE`).

---

## 4. 모듈별 상세

### 4.1 `main.py`

- `DataManager(basePath)` → `SceneController` → `intro()`
- 클래스명이 `main`으로, 모듈/관례상 `Main` 또는 함수형 진입이 더 자연스럽다.

### 4.2 Controllers

**SceneController**

| 메서드 | 상태 | 설명 |
|--------|------|------|
| `intro()` | 구현됨 | 인트로 루프 (1: start, 2: chooseSave, 3: exit) |
| `start()` | stub | `print('new game!')`만 수행 |
| `chooseSave()` | 부분 구현 | 목록 표시 후 선택 시 `loadCharacter` → `lobby` |
| `lobby()` | 부분 구현 | 스탯 표시, 스케줄 관리 / 뒤로가기, 12월이면 종료 stub |
| `exit()` | 구현됨 | 메시지 출력 후 `sys.exit(0)` |

**ScheduleController**

| 메서드 | 상태 | 설명 |
|--------|------|------|
| `scheduleSelection()` | 부분 구현 | 행동 선택 루프 → `nextMonth` / `endGame` |
| `nextMonth()` | 부분 구현 | `month += 1` 후 `saveCharacter` |
| `endGame()` | 부분 구현 | `ending` 설정 후 `saveCharacter` |

### 4.3 Services

**CharacterServices**

- `createCharacter()`: `DEFAULT_DATA['character']` 딥카피로 인메모리 생성
- `findAllCharacters()` / `loadCharacter()`: **샘플 데이터** (실제 `DataManager` 미연동)
- `saveCharacter()`: 미구현
- `playCharacter`: 현재 플레이 중인 캐릭터 상태 보관용 (미사용)

**ActionsServices**

- `store`만 보관하는 스켈레톤. 행동 적용·판정 로직 없음.

### 4.4 Managers

**FileManager**

- 경로: `{basePath}/resources/{key}.json`
- `write` / `read`, UTF-8, `ensure_ascii=False`
- 파일 없음 → `FILE_NOT_FOUND`, JSON 깨짐 → `INVALID_JSON`

**DataManager**

- `DEFAULT_DATA`에 등록된 키만 허용 (`UNKNOWN_KEY` 방어)
- `findAll` / `findBy` / `create` / `update` / `delete` / `save` / `load`
- 파일 없을 때 기본 스키마를 써 넣고 반환 (auto-seed)
- `create` 시 `id` 자동 채번 (`generateId`)

> 참고: `DEFAULT_DATA['character']`는 **단일 객체 스키마**인데, `DataManager.create`는 **리스트에 append**하는 전제다. 캐릭터 세이브 연동 시 키를 `characters`(리스트)로 두거나, `load`/`create` 계약을 맞출 필요가 있다.

### 4.5 Views

**SystemViews** — 공통 UI

- `lineBreak` / `headline` / `subtitle`
- `menu` / `choice`: 번호 메뉴 + 범위·숫자 검증 루프
- `errorMessage`: `[System]` 프리픽스

**IntroViews** — 타이틀 `대학생 시뮬레이터`, 메뉴 3종  
**CharacterViews** — 로비 타이틀·스탯 바·메뉴, 세이브 슬롯(최대 8) 선택  
**ScheduleViews** — 월간 스케줄 타이틀·선택 목록·행동 메뉴

### 4.6 Config (콘텐츠·규칙)

**스탯** (`DEFAULT_STATS` / `STAT_LABELS`)

- money(소지금), intelligence(지능), charm(매력), stamina(체력), stress(스트레스)
- 라벨 키와 스탯 키가 일치함

**행동** (`ACTIONS`, 8종)

| ID | 이름 | 주요 weight 경향 |
|----|------|------------------|
| 1 | 취업 준비 | 지능↑, 스트레스↑ |
| 2 | 알바 | 재력↑, 체력↓ |
| 3 | 외관 관리 | 매력↑, 스트레스↓ |
| 4 | 쇼핑 | 재력↓↓, 스트레스↓↓ |
| 5 | 건강 관리 | 체력↑, 스트레스↓ |
| 6 | 영어 공부 | 지능↑↑ |
| 7 | 돈 모으기 | 재력↑ |
| 8 | 휴식/여가 | 스트레스↓↓ |

**아웃컴 배율**

- 대성공 ×2.0 / 성공 ×1.0 / 실패 ×0.3 / 대실패 ×0.0 (+ 스트레스 보너스 2)

**이벤트** (`EVENTS`) — schedule 루프 연결 예정 mock

- `illness`, `burnout`: stress ≥ 100 시 트리거, 일수 감소 + 스탯 보정

**엔딩** (`ENDINGS`) — 7종

- 대기업 / 창업 / 해외 도피 / 유튜버 / 노가다 / 중소기업 / 백수

### 4.7 `utils.py`

- `getDisplayWidth`: 한글·자모 2칸, 그 외 1칸
- `padByDisplayWidth`: left / right / center 정렬 패딩  
→ CLI에서 한글·영문 혼용 시 박스가 깨지지 않게 함

---

## 5. 캐릭터 데이터 모델

```python
{
  'name': 'unknown',
  'turn': 0,
  'month': 1,
  'stats': {
    'money': 500,
    'intelligence': 5,
    'charm': 5,
    'stamina': 5,
    'stress': 0,
  },
  'history': [],
  'action_counts': {},
  'events_triggered': [],
  'ending': None,
}
```

세이브 목록 UI는 `name`, `month`, `turn`, `ending`을 사용한다.

---

## 6. 구현 완성도

| 영역 | 완성도 | 비고 |
|------|--------|------|
| 인트로 메뉴 | ✅ | 새로하기 / 이어하기 / 종료 |
| 공통 CLI UI | ✅ | headline, subtitle, menu, choice |
| JSON 파일 계층 | ✅ | FileManager + DataManager CRUD |
| 세이브 목록 UI | △ | UI 있음, 데이터는 샘플 8개 |
| 로비(스탯·메뉴) | △ | 표시·분기 가능, 12월 종료는 stub |
| 스케줄 선택 UI | △ | 선택·월 증가 stub, 행동 적용 없음 |
| 캐릭터 영속화 | ❌ | Service ↔ Manager 미연결 |
| 새 게임 시작 | ❌ | stub |
| 행동 적용·아웃컴 | ❌ | config만 준비 |
| 이벤트·엔딩 판정 | ❌ | 데이터만 정의 |

---

## 7. 설계상 강점

1. **계층 분리가 명확** — View는 출력, Manager는 I/O, Controller는 흐름만 담당
2. **결과 코드 통일** — `STATUS` / `CODE`로 성공·실패 분기 가능
3. **콘텐츠와 로직 분리** — 행동·이벤트·엔딩을 config에 두어 밸런스 조정 용이
4. **한글 CLI 정렬 유틸** — 포트폴리오용 터미널 게임에 실무적으로 유용
5. **씬/스케줄 컨트롤러 분리** — 인트로·로비와 월간 루프 책임이 나뉨

---

## 8. 개선·주의 포인트

1. **스키마 불일치**: `DEFAULT_DATA['character']`(객체) vs `DataManager` 리스트 CRUD
2. **세이브 미연동**: `CharacterServices`가 store를 쓰도록 `findAll` / `create` / `update` 연결 필요
3. **본편 루프 미완성**: 행동 weight×아웃컴 → 이벤트 → 엔딩 판정 미연결
4. **`ActionsServices` 빈 구현**
5. **네이밍**: `main` 클래스, View 메서드의 `@staticmethod`와 인스턴스 혼용

---

## 9. 권장 구현 순서 (다음 단계)

1. `characters`(리스트) 키로 세이브 스키마 확정 후 `CharacterServices` ↔ `DataManager` 연동  
2. `start()`에서 이름 입력 → `createCharacter` → 저장 → `lobby`  
3. `ActionsServices`: 행동 선택 → 아웃컴 롤 → 스탯 clamp(0~100) 적용  
4. `scheduleSelection`에서 선택한 스케줄에 행동 적용 + 월간 결과 뷰  
5. stress 기반 이벤트 트리거, 12개월 종료 시 `ENDINGS` 판정  
6. 이어하기: 선택 id로 `load` → 로비 재개  

---

## 10. 실행 방법

```bash
cd Portfolio/Game
python main.py
```

인트로에서 `1` 새로하기 / `2` 이어하기(샘플 목록) / `3` 종료를 선택할 수 있다.

---

*분석 기준 경로: `Portfolio/Game/` (컨트롤러·서비스·매니저·뷰·config 전 파일)*
