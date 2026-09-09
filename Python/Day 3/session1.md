# [Day 3 - Session 1] for 반복문, for-else, reversed(), range() 및 중첩 루프

- **실습 파일**: `session1.py`
- **주요 내용**: 
  - `for` 반복문 기본 구조 및 다양한 컬렉션 순회 (리스트, 튜플 언패킹, 문자열, 딕셔너리)
  - 루프 제어문: `break`와 `continue`
  - 객체 동일성(`is`) vs 값 동등성(`==`)과 타입 검사
  - `for-else` 구문의 동작 원리
  - `reversed()` 내장 함수와 시퀀스 형 변환
  - `range()` 함수의 인자 구조(`start`, `stop`, `step`)와 활용
  - 중첩 `for` 루프 (구구단) 및 `print()`의 `end` 옵션
  - 문자열 메서드 `isupper()`를 활용한 대문자 필터링

---

## 1. 실습 코드 및 단계별 해설

### 1.1 `for` 반복문 기본과 다양한 시퀀스 순회

```python
names = ['kim', 'lee', 'park', 'choi']

for name in names:
  print(name)

# 튜플 언패킹 순회
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
  print(first)
  print(last)

# 문자열 순회
word = 'python'
for char in word:
  print(char)

# 딕셔너리 순회
profile = {
  'name': 'hong',
  'age': 33
}
for key in profile:
  print(key)
  print(profile[key])

for value in profile.values():
  print(value)
```

- **설명**:
  - `for 변수 in 이터러블:`: 리스트, 튜플, 문자열, 딕셔너리 등 반복 가능한 객체의 요소를 처음부터 끝까지 하나씩 꺼내어 반복합니다.
  - **튜플 언패킹 순회**: `(first, last)` 형태로 튜플 원소를 각각의 변수로 직접 분해하며 순회할 수 있어 코드가 간결해집니다.
  - **문자열 순회**: 문자열의 각 글자를 문자 단위로 순서대로 순회합니다.
  - **딕셔너리 순회**: 기본적으로 Key를 꺼내며, Value가 필요하면 `profile[key]`로 조회하거나 `profile.values()` 메서드를 사용합니다.

---

### 1.2 `break`와 `continue`를 통한 루프 제어

```python
num = [34, 62, 63, 1, 35, 6, 2]
for i in num:
  if i == 35:
    print('35!')
    break
  else:
    print(i)
```

- **설명**:
  - `if i == 35:` 조건이 참이 되면 `'35!'`를 출력한 뒤 **`break`를 만나 반복문 전체를 즉시 종료**합니다.
  - 35 이전의 숫자들만 출력되고 35 이후의 원소들은 순회하지 않습니다.

---

### 1.3 `is` vs `==` 비교와 타입 검사

```python
# is : 두 객체가 같은 타입객체(메모리 주소가 같은지) 인지 비교하는 연산자
# == : 값이 같은지 비교
# type : 하나의 고정된 타입 객체 반환

li = ['3', 1, 2, True, 4.5]

for i in li:
  if type(i) is str:
    print('true')
    continue
  print(i, type(i))
```

- **설명**:
  - **`==`**: 두 객체의 **값(Value)**이 같은지 비교합니다.
  - **`is`**: 두 객체의 **메모리 주소(Identity)**가 같은지 비교합니다.
  - `type(i) is str`: 파이썬에서 `str`, `int` 등의 자료형 클래스는 싱글톤처럼 메모리에 유일하게 존재하므로, 타입 객체 자체를 비교할 때 `is`를 사용할 수 있습니다.
  - `type(i) is str`인 경우 `'true'`를 출력하고 **`continue`를 호출하여 아래 출력을 건너뛰고 다음 반복**으로 넘어갑니다.

---

### 1.4 `for-else` 구문의 동작 원리

```python
# for else 구문
# else 블록은 for 문이 break로 중간에 끊기지 않고 끝까지 실행되었을때만 실행
num = [34, 62, 63, 1, 35, 6, 2]
for i in num:
  if i == 35:
    print('35!')
    break
else:
  print('hihi')
```

- **설명**:
  - 파이썬의 `for-else` 문에서 **`else` 블록은 반복문이 `break`를 만나지 않고 정상적으로 끝까지 순회했을 때만 실행**됩니다.
  - 위 코드에서는 `i == 35` 조건에서 `break`가 걸려 조기 종료되므로, `else:` 블록의 `'hihi'`는 실행되지 않습니다.
  - 특정 대상을 탐색하다가 찾지 못했을 때의 기본 동작(예: "검색 결과 없음")을 처리할 때 플래그 변수 없이 깔끔하게 구현할 수 있습니다.

---

### 1.5 `reversed()` 함수와 시퀀스 변환

```python
fruit2 = 'Mango'
print(reversed(fruit2)) # 객체 주소 값 반환 (<reversed object>)
print(fruit2)
print(list(reversed(fruit2))) # ['o', 'g', 'n', 'a', 'M']
print(tuple(fruit2))          # ('M', 'a', 'n', 'g', 'o')
print(set(fruit2))            # 순서 유지 안됨, 중복 제거
print(''.join(list(reversed(fruit2)))) # 'ognaM'
```

- **설명**:
  - `reversed()`는 시퀀스를 역순으로 순회할 수 있는 **이터레이터 객체(`reversed object`)**를 반환합니다.
  - 실제 결과를 확인하거나 활용하려면 `list()`나 `tuple()`로 변환해야 합니다.
  - `set()`으로 변환하면 순서가 무작위로 섞이며 중복 글자가 제거됩니다.
  - `''.join(list(reversed(fruit2)))`는 뒤집힌 문자 리스트를 다시 하나의 문자열로 결합합니다 (`'ognaM'`).

---

### 1.6 `range()` 함수와 `for` 루프

```python
# for 문과 함께 사용하는 range 함수
a = range(10)
print(list(a)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = range(1, 10)
print(list(a)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = range(1, 10, 2)
print(list(a)) # [1, 3, 5, 7, 9]

for i2 in range(1, 11):
  print(i2)
```

- **설명**:
  - `range(stop)`: 0부터 `stop - 1`까지의 정수 수열을 생성합니다.
  - `range(start, stop)`: `start`부터 `stop - 1`까지 생성합니다.
  - `range(start, stop, step)`: `step` 간격으로 증감하며 생성합니다.
  - 메모리를 미리 할당하지 않고 필요할 때 값을 생성하는 이터레이터 방식이므로 큰 수의 범위도 효율적으로 다룹니다.

---

### 1.7 `while` vs `for` 비교 및 `print()`의 `end` 옵션

```python
# while 문으로 1~10 출력
i = 1
while(i <= 10):
  print(i)
  i += 1

print()

# for 문과 range의 step, end 옵션
for i3 in range(1, 11, 2):
  print(i3, end = ' ')
print()
```

- **설명**:
  - `while`문은 조건식을 만족하는 동안 수동으로 인덱스(`i`)를 증가시켜야 하지만, `for`문과 `range()`를 사용하면 증감 처리가 자동화되어 훨씬 간결합니다.
  - `print()`의 기본값은 개행(`end='\n'`)이지만, `end=' '`를 지정하면 줄바꿈 대신 공백으로 띄어 한 줄에 출력할 수 있습니다.

---

### 1.8 중첩 `for` 루프 (이중 반복문) : 구구단 출력

```python
for i in range(2, 10):
  for j in range(2, 10):
    print(i, end = ' x ')
    print(j, end = ' = ')
    print(i * j, end = ' ')
  print()
```

- **설명**:
  - 외부 루프 `i`가 한 번 돌 때 내부 루프 `j`가 2부터 9까지 전체 실행됩니다.
  - 한 단의 계산이 끝나면 빈 `print()`를 호출하여 줄바꿈을 수행합니다.

---

### 1.9 문자열 인덱스 순회 및 조건 필터링 실습

```python
# 문자열에서 대문자만 추출
msg = 'It is Time'
for index in range(len(msg)):
  if msg[index].isupper():
    print(msg[index], end = ' ') # I T
print()

# 1~10 중 홀수만 출력 (continue 활용)
print('홀수: ', end = '')
for i in range(1, 11):
  if i % 2 == 0:
    continue
  print(i, end = ' ')
print()

# range step을 활용한 3의 배수 출력
print('3~32까지 수 중 3의 배수: ', end = '')
for i in range(3, 33, 3):
  print(i, end = ' ')
print()
```

- **설명**:
  - `msg[index].isupper()`: 문자열 메서드로 해당 문자가 **영문 대문자**이면 `True`를 반환합니다 (`'I'`, `'T'`).
  - `if i % 2 == 0: continue`: 짝수일 때 출력을 건너뛰어 홀수만 출력합니다.
  - `range(3, 33, 3)`: `step=3`을 지정하여 조건문 없이 3의 배수만 직접 생성합니다.

---

## 2. 핵심 요약

1. **`for-else` 특성**: `break`로 반복이 중단되면 `else` 블록은 건너뜁니다.
2. **`is` vs `==`**: 값의 동일성은 `==`, 객체의 메모리 주소(정체성) 동일성은 `is`로 비교합니다.
3. **`range()`의 끝 값**: `range(1, 10)`은 10을 포함하지 않고 9까지만 생성합니다.
4. **`print(end=' ')`**: 줄바꿈 없이 가로 출력을 이어갈 때 사용합니다.
