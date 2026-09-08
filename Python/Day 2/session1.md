# [Day 2 - Session 1] 튜플 언패킹, 딕셔너리(Dictionary) 기초/메서드 및 리스트 복습 실습

- **실습 파일**: `session1.py`
- **주요 내용**: 
  - 튜플 패킹(Packing)과 언패킹(Unpacking)
  - 딕셔너리 특징 (순서 없음/삽입순 유지, Key 중복 불가, 가변성)
  - 다양한 딕셔너리 생성 방식 (리터럴 `{}` 및 `dict()` 생성자 활용)
  - Key를 통한 Value 접근 및 에러 방지 (`dict['key']` vs `dict.get('key')`)
  - Key-Value 추가, 수정 및 Key 중복 시 동작
  - 딕셔너리 순회 및 내장 메서드 (`keys()`, `values()`, `items()`, `pop()`, `clear()`, `in` 연산자)
  - 리스트 조작 복습 실습 (인덱싱, 수정, 결합, `append`, `insert`, `pop`, `del`, `remove`, `index`)

---

## 1. 실습 코드 및 단계별 해설

### 1.1 튜플 패킹(Packing)과 언패킹(Unpacking)

```python
# 튜플 패킹(packing)
tu22 = ( 'phone', 'book', 'computer', 'mouse' )
print(tu22)

# 튜플 언패킹(unpacking)
(w, x, y, z) = tu22
print(w, x, y, z)
```

- **설명**:
  - **패킹(Packing)**: 여러 개의 데이터를 튜플 하나로 묶는 과정입니다.
  - **언패킹(Unpacking)**: 튜플 내부의 요소들을 각각의 개별 변수에 순서대로 나누어 담는 과정입니다.
  - **주의**: 좌변 변수의 개수(4개)와 우변 튜플 원소의 개수(4개)가 일치해야 하며, 개수가 다르면 `ValueError`가 발생합니다.

---

### 1.2 딕셔너리 선언 및 다양한 데이터 형태 수용

```python
# 딕셔너리
# 순서 없음(파이썬 3.7+부터는 삽입 순서 유지), 키 중복 안됨, 수정/삭제 가능
# javascript의 json과 동일 형식
dic1 = { "name" : "Lee", "phone" : "010-0000-0000", "birth" : "001122" }
dic2 = { 0 : "python" }
dic3 = { 'ary' : [ 1, 2, 3, 4 ]}
dic4 = {
  'name': 'tom',
  'addr': 'seoul',
  'age': '22',
  'grade': 'A',
  'status': True
}
dic5 = dict()
```

- **설명**:
  - 딕셔너리는 `Key: Value` 쌍으로 이루어진 매핑(Mapping) 자료형입니다.
  - **Key의 조건**: 불변(Immutable) 값이어야 하므로 문자열, 숫자, 튜플 등은 사용 가능하지만 **리스트나 딕셔너리는 Key로 사용할 수 없습니다.**
  - **Value의 조건**: 정수, 문자열, 불리언은 물론 리스트(`[1, 2, 3, 4]`), 딕셔너리 등 모든 자료형을 값으로 담을 수 있습니다.
  - `dic5 = dict()`는 `{}`와 마찬가지로 빈 딕셔너리를 생성합니다.

---

### 1.3 `dict()` 생성자를 이용한 튜플 리스트 변환

```python
dic6 = dict([ ( 'name', 'tom' ), ( 'addr', 'seoul' ), ( 'age', '22' ), ( 'grade', 'A' ), ( 'status', True ) ])
# 가장 안쪽 구조 : 튜플 구조
# 안쪽을 감싸는 구조: 리스트 구조(여러 개의 튜플을 하나로 묶음 → 튜플의 리스트)
# 가장 바깥쪽 구조 : 딕셔너리 구조로 변환
# (키, 값) 튜플 → 딕셔너리 {키: 값}
# dict() 는 인자를 1개만 받을 수 있음
```

- **설명**:
  - `dict()` 함수는 `[(Key1, Value1), (Key2, Value2), ...]` 형태의 **(키, 값) 튜플을 요소로 갖는 리스트/시퀀스 1개**를 받아 딕셔너리로 변환할 수 있습니다.
  - 데이터베이스 조회 결과나 외부 API의 Key-Value 쌍 목록을 딕셔너리로 재구성할 때 자주 쓰입니다.

---

### 1.4 값 조회: `[]` vs `.get()` 메서드 차이

```python
# key를 이용해 value 값 추출
# 딕셔너리명['키']
# print(dic1['name1']) # 키가 없으면 KeyError 오류
print(dic1.get('name1')) # 키가 없으면 None
```

- **설명**:
  - **`dic1['key']`**: 키가 존재하면 해당 값을 가져오지만, **키가 존재하지 않으면 프로그램이 중단되며 `KeyError`가 발생**합니다.
  - **`dic1.get('key')`**: 키가 존재하지 않을 때 에러를 발생시키지 않고 **`None`을 안전하게 반환**합니다. (예: `dic1.get('name1', '기본값')`처럼 기본값 지정도 가능)

---

### 1.5 키 중복 및 데이터 추가/수정

```python
# 키가 중복 될 경우 마지막 키:값만 노출
a = { 1: 'c', 1: 'a', 1: 'b', 1: 'd' }
print(a) # {1: 'd'}

dic1['address'] = 'yongsan'
print(dic1)

dic1['score'] = [90, 30, 40]
print(dic1)
print(len(dic1))
```

- **설명**:
  - **Key 중복 불가**: 딕셔너리에 동일한 키를 여러 번 정의하면, 이전 값을 덮어쓰고 **가장 마지막에 작성된 `Key: Value` 쌍만 유지**됩니다.
  - **추가/수정 문법**: `dic['새키'] = 값`을 대입하면 새로운 항목이 추가되고, 기존에 있던 키라면 새 값으로 수정됩니다.
  - `len(dic1)`: 딕셔너리에 등록된 `Key: Value` 쌍의 총 개수를 반환합니다.

---

### 1.6 Key, Value, Items 추출 및 순회

```python
# key
print(dic1.keys())        # dict_keys 객체
print(list(dic1.keys()))  # 리스트로 변환
for k in dic1.keys():
  print(k)

# value
print(dic1.values())       # dict_values 객체
print(list(dic1.values())) # 리스트로 변환
for v in dic1.values():
  print(v)

# items - (key, value) 튜플 목록
print(dic1.items())       # dict_items 객체: [('name', 'Lee'), ...]
print(list(dic1.items())) # 리스트로 변환
```

- **설명**:
  - **`keys()`**: 딕셔너리의 모든 Key를 담은 `dict_keys` 뷰(View) 객체를 반환합니다.
  - **`values()`**: 딕셔너리의 모든 Value를 담은 `dict_values` 뷰 객체를 반환합니다.
  - **`items()`**: `(Key, Value)` 쌍을 튜플로 묶은 `dict_items` 뷰 객체를 반환합니다.
  - 뷰 객체들은 메모리를 낭비하지 않고 `for` 반복문에서 바로 순회할 수 있으며, 리스트 기능(인덱싱 등)이 필요하면 `list()`로 감싸서 변환합니다.

---

### 1.7 요소 추출/삭제 및 존재 여부 확인 (`pop`, `in`, `clear`)

```python
# pop - 값을 꺼내고, 딕셔너리에서 키를 삭제
print(dic1.pop('birth'))
print('birth' in dic1) # 키를 삭제 했기때문에 False

# clear
dic1.clear()
print(dic1) # {}
```

- **설명**:
  - **`pop('key')`**: 지정한 키에 해당하는 값을 반환하면서 딕셔너리에서 해당 항목을 완전히 제거합니다. (키가 없으면 `KeyError` 발생)
  - **`'key' in dic`**: 해당 키가 딕셔너리에 존재하는지 확인하여 `True` / `False`를 반환합니다. (Value가 아닌 **Key를 기준**으로 검사)
  - **`clear()`**: 딕셔너리 내부의 모든 요소를 비워 빈 딕셔너리 `{}`로 만듭니다.

---

### 1.8 리스트 조작 복습 실습 (연습 문제)

```python
# 1
odd = [1, 3, 5, 7, 8]
print(odd[0])
print(odd[1])

odd[0] = 10 # 0번 인덱스 값 수정

# 2
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# 리스트를 합쳐본다
c = a + b
# a.extend(b)

# a리스트에 마지막 요소에 6을 추가한다
a.append(6)

# 인덱스 3에다 정수 7을 삽입
a.insert(3, 7)

# 맨 마지막 값을 삭제해본다
a.pop()

# 인덱스 3을 삭제한다
del a[3]

# 숫자 4를 삭제한다
a.remove(4)

# 숫자 5의 위치를 알아낸다
print(a.index(5))
```

- **설명**:
  - `odd[0] = 10`: 인덱스를 통한 가변 객체 리스트의 값 변경.
  - `a + b` vs `a.extend(b)`: `+` 연산자는 새 리스트 `c`를 생성하고, `extend()`는 기존 `a` 리스트 자체를 확장합니다.
  - `a.append(6)`: 맨 뒤에 단일 원소 추가.
  - `a.insert(3, 7)`: 3번 인덱스 위치에 7 삽입 (기존 원소들은 뒤로 밀림).
  - `a.pop()`: 맨 마지막 원소 꺼내며 삭제.
  - `del a[3]`: 인덱스 위치 기준으로 삭제.
  - `a.remove(4)`: 특정 값(`4`)을 기준으로 첫 번째 일치 항목 삭제.
  - `a.index(5)`: 값 `5`가 위치한 인덱스 번호 반환.

---

## 2. 핵심 요약 및 복습 포인트

| 기능 | 문법 / 메서드 | 특징 및 주의사항 |
| :--- | :--- | :--- |
| **언패킹** | `w, x, y, z = (1, 2, 3, 4)` | 변수 개수와 원소 개수가 반드시 일치해야 함 |
| **값 조회** | `dic['key']` | 키 부재 시 **`KeyError` 발생** |
| **안전 조회** | `dic.get('key', default)` | 키 부재 시 `None` 또는 기본값 반환 (에러 없음) |
| **Key 목록** | `dic.keys()` | `for k in dic.keys():` 형태로 직접 순회 가능 |
| **Value 목록** | `dic.values()` | 값들만 모아서 순회 또는 확인 |
| **Key-Value 쌍** | `dic.items()` | `for k, v in dic.items():`로 튜플 언패킹 순회에 자주 활용 |
| **항목 꺼내기** | `dic.pop('key')` | 값을 반환하고 딕셔너리에서 삭제 |
| **Key 검사** | `'key' in dic` | Key 존재 여부 boolean 반환 |
| **전체 비우기** | `dic.clear()` | 내부 모든 요소 삭제 후 빈 딕셔너리 `{}` 유지 |
| **리스트 삭제** | `del a[i]` / `a.pop()` / `a.remove(val)` | 인덱스 기준(`del`, `pop`) vs 값 기준(`remove`) 구분 필요 |
