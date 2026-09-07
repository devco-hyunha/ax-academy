#파이썬 기본 교재 : Do it! 점프 투 파이썬

# 파이썬 자료형
# '''
# int : 정수
# float : 실수
# complex : 복소수
# bool : 불리언
# str : 문자열
# list : 리스트
# tuple : 튜플
# set : 집합
# dict : 딕셔너리
# '''

# 데이터 타입
str1 = "Python"
bool1 = True
float1 = 10.4
int1 = 3
list1 = [str1]
dict1 = { "name": "gildong", "id": 3 }
tuple1 = (4, 2, 4)
set1 = {1, 23, 4}

# 데이터 타입 출력
print(type(str1)) # <class 'str'>
print(type(bool1)) # <class 'bool'>
print(type(float1)) # <class 'float'>
print(type(int1)) # <class 'int'>
print(type(list1)) # <class 'list'>
print(type(dict1)) # <class 'dict'>
print(type(tuple1)) # <class 'tuple'>
print(type(set1)) # <class 'set'>

#str1 = "Python"
#str1이라는 문자자체를 객체로 만들고 다양한 속성(변수), 행동(함수)을 넣을 수 있다

# 숫자형 연산자
# +, -, *, /, %
i1 = 30
i2 = 944
big_int1 = 123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999
print(i1 + i2)
print(big_int1 + big_int2) # 메모리 허용 범위 내에서는 무한대 연산 가능(정수 크기 제한 없음)

print(3**4) # 3의 3제곱

f1 = 1.234
f2 = 3.458
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)

# 형 변환
a = 3.
b = 10
c = .5
d=12.5
print(type(a), type(b), type(c), type(d))

# 정수 → 실수
print(float(b))

# 실수 c → 정수
print(int(c))

# bool true → 정수
print(int(True))

print(float(True))
print(int(False))
print(complex(3))

# 수치 함수
print(abs(-4)) # 절대값
print(pow(3, 4)) # 3의 4제곱
print(divmod(7, 3)) # 7을 3으로 나눈 몫과 나머지