# 내장 함수
# 절대값
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# 모든 요소가 참인지 판단
print(all([1, 2, 3])) # True
print(all([1, 2, 3, 0])) # Fale
print(all([])) #True - 인자가 빈 값인 경우 True 반환

# 하나라도 참인지 판단
print(any([1, 2, 3, 0])) # True
print(any([0, ''])) # False
print(any([])) # False - 인자가 빈 값인 경우 False 반환

# chr - 유니코드 숫자를 문자로 리턴
print(chr(97))
print(chr(44032))

# ord - 문자를 유니코드 숫자로 리턴
print(ord('a'))
print(ord('가'))


# dir - 객체가 지닌 변수나 함수를 리턴 property
print(dir([1, 2, 3]))
print(dir({'1': 'a'}))

# divmod - 인자 a, b를 받아 a 를 나눈 값과 나머지를 튜플로 리턴
print(divmod(7, 3))

# enumrate
for i, name in enumerate(['body', 'foo', 'bar']):
  print(i, name)
for i, key in enumerate({'a': 'body', 'b': 'foo', 'c': 'bar'}):
  print(i, key)

# filter
def positive(l):
  result = []
  for i in l:
    if i > 0:
      result.append(i)
  return result

print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
  return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# map
def two_times(numberList):
  result = []
  for number in numberList:
    result.append(number * 2)
  return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times(x):
  return x * 2

print(list(map(two_times, [1, 2, 3, 4])))

list1 = [1, 2, 3, 4, 5]
re3 = list(map(lambda x: x + 10, list1))
print(re3)

# max
print(max([1, 2, 3]))
print(max("python"))

# min
print(min([1, 2, 3]))
print(min("python"))

# pow - x, y 을 인자로 x 를 y 번 제곱한 값을 리턴
print(pow(2, 4))
print(pow(3, 3))

# range
print(range(5))
print(range(5, 10))
print(range(1, 10, 2))

# round
print(round(4.6))
print(round(3.141231234, 2))

# zip - 동일한 갯수로 이루어진 데이터들을 묶어서 리턴
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip('abc', 'def')))


li1 = [i for i in range(1, 6)]

map1 = list(map(lambda i: i, range(1, 6)))
print(map1)

filter1 = list(filter(lambda x: x < 3, range(1, 6)))
print(filter1)

map2 = list(map(
  lambda x: x + 100,
  range(1, 11)
))
print(map2)


def square(x):
  return x ** 2
list1 = [1, 2, 3, 4, 5]
re1 = list(map(square, list1))
print(re1)

re2 = list(map(lambda x: x ** 2, list1))
print(re2)

re3 = [x ** 2 for x in list1]
print(re3)

re4 = [x for x in range(1, 21) if x%2 == 0]
print(re4)