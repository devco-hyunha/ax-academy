# 함수
def add(a, b):
  print('a:', a, end = ' + ')
  print('b:', b, end = ' = ' )
  return a + b

print(add(1, 2))
print(add(a = 1, b = 2))
print(add(b = 1, a = 2))

def say():
  return 'hi'

def printAdd(a, b):
  print( a + b )

def printSay():
  print('hi')


def multi(x):
  y1 = x * 5
  y2 = x * 10
  y3 = x * 20
  return y1, y2, y3

x, y, z = a = multi(2)

print(x, y, z)
print(list(a))

def func3(x):
  y1 = x * 5
  y2 = x * 10
  y3 = x * 20
  return {'y1': y1, 'y2': y2, 'y3': y3}

a = func3(5)
print(a)

print(a.get('y2'))

for k in a.keys():
  print(k, end = ' : ')
  print(a.get(k))

print(list(a.values()))

# *args : tuple 반환
def add_many(*args):
  result = 0
  for i in args:
    result += i
  return result

c = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9 ,10)
print(c)

# **kwargs: dict 반환
def func2(**kwargs):
  for i in kwargs.keys():
    print(i)

func2(name1 = '철수')
func2(name1 = '철수', name2 = '영희')
func2(name1 = '길동', name2 = '철수', name3 = '영희')

def func3(arg1, arg2, *args, **kwargs):
  print(arg1, arg2, args, kwargs)
  return

func3(10, 20, 'kim', 'lee', age=10, addr='seoul')

#매개변수의 순서 - (일반 인자, tuple, dict) 의 순서로 하는것이 좋다


# 15시에 방문하고 3개 이상 구매시 10%할인
# 12시에 방문하고 5개 이상 구매시 20%할인
# => 형민씨는 10%할인= 18000원 형태로 출력 (format함수 . c스타일. f스트링)
def calcu(name, time, count, price):
  discount = 0
  if time == 15 and count >= 3:
   discount = 10
  elif time == 12 and count >= 5:
    discount = 20
  print(f'{name}씨는 {discount}% 할인= {int(price / 100 * (100 - discount))}원')
  print('%s씨는 %d%% 할인= %d원' %(name, discount, int(price / 100 * (100 - discount))))
  # c스타일에서 %는 %% 작성해야 출력됨
  print('{0}씨는 {1}% 할인= {2}원'.format(name, discount, int(price / 100 * (100 - discount))))

calcu("형민", 15, 4, 20000)
calcu("종진", 12, 5, 50000)
calcu("한빈", 10, 2, 70000)

def is_odd(number):
  if number % 2 == 1:
    return True
  else:
    return False

def avg_numbers(*args):
  result = 0
  for i in args:
    result += i
  return result / len(args)

def say(name, man, old = 20):
  print(name)
  if man:
    print('남자', old)
  else:
    print('여자', old)

say('juli', True)
say('tom', False, 10)