# [Day 7 - Session 1] 객체지향 프로그래밍: 데이터 모델(User) 및 관리자(UserManager) 클래스

- **실습 파일**: `session1.py`
- **주요 내용**:
  - `User` 엔티티 클래스 정의: `__init__`, `info()`, `__str__()`
  - `UserManager` 컬렉션 관리 클래스 정의: `add_user()`, `find_user()`, `delete_user()`, `list()`
  - 객체 간 상호작용 및 기본 CRUD(Create, Read, Delete, Search) 패턴
  - 클래스 변수 vs 인스턴스 변수 사용 시 주의점

---

## 1. 실습 코드 및 단계별 해설

### 1.1 User 엔티티 클래스

```python
class User:
  def __init__(self, id, name, email):
    self.id = id
    self.name = name
    self.email = email

  def info(self):
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email
    }

  def __str__(self):
    # 객체 출력 시(print 함수 등) 자동으로 호출되어 사람이 읽기 쉬운 문자열을 반환
    return f"{self.id}, {self.name}, {self.email}"
```

- **설명**:
  - 개별 사용자의 속성(`id`, `name`, `email`)을 캡슐화합니다.
  - `info()` 메서드는 객체의 상태를 딕셔너리 형태로 직렬화하여 반환합니다.
  - `__str__()` 매직 메서드를 구현함으로써 `print(user)` 호출 시 `<__main__.User object ...>` 대신 사용자 정의 문자열(`"1, 가, a@domain.com"`)이 출력됩니다.

---

### 1.2 UserManager 관리자 클래스

```python
class UserManager:
  users = []

  def list(self):
    return list(self.users)

  def add_user(self, User):
    self.users.append(User)

  def delete_user(self, id):
    user = UserManager.find_user(self, id)
    if user:
      self.users.remove(user)
    else:
      print('none id')

  def find_user(self, user_id):
    for user in self.users:
      if user.id == user_id:
        return user
    return None
```

- **설명**:
  - `add_user(user)`: 새로운 사용자 객체를 리스트에 추가합니다.
  - `find_user(user_id)`: 전달받은 `user_id`와 일치하는 객체를 리스트에서 순회 검색하고, 없으면 `None`을 반환합니다.
  - `delete_user(id)`: `find_user()`로 검색된 객체가 존재하면 `remove()`로 제거하고, 없을 경우 오류 메시지를 출력합니다.
  - `list()`: 현재 보관된 사용자 목록을 새 리스트로 얕은 복사하여 반환합니다.

---

### 1.3 실행 테스트

```python
user1 = User(1, '가', 'a@domain.com')
user2 = User(2, '나', 'b@domain.com')
user3 = User(3, '다', 'c@domain.com')

manager = UserManager()

manager.add_user(user1)
manager.add_user(user2)
manager.add_user(user3)

manager.delete_user(2)  # id가 2인 user2 삭제

for user in manager.list():
  print(user)
# 출력:
# 1, 가, a@domain.com
# 3, 다, c@domain.com
```

---

## 2. 핵심 포인트 및 권장 개선 사항

### 💡 클래스 변수 `users` vs 인스턴스 변수 `self.users`
- 실습 코드의 `users = []`는 **클래스 변수**로 선언되어 있습니다. 이 경우 서로 다른 매니저 객체(`m1 = UserManager()`, `m2 = UserManager()`)를 생성하더라도 같은 리스트를 공유하게 됩니다.
- 각 매니저 객체마다 독립적인 사용자 리스트를 유지하려면 생성자(`__init__`) 내부에서 인스턴스 변수로 초기화하는 것이 표준 권장사항입니다:

```python
class UserManager:
  def __init__(self):
    self.users = []  # 각 인스턴스별 독립 리스트 생성
```
