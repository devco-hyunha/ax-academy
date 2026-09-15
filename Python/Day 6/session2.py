# 예외처리
# SyntaxError, NameError, IndexError, ZeroDivisionError, KeyError, ValueError, TypeError...

# li = ['db', 'python', 'react']
# try:
#   pass

# except:# 오류 종류에 상관 없이 except 실행
# except ZeroDivisionError:# 숫자를 0으로 나눌때 오류
#   print('0으로 나눌 수 없습니다')
# except IndexError:# 리스트의 조회 가능한 범위를 벗어난 조회시 오류
#   print('인덱싱 할 수 없습니다')
# except NameError:# 선언하지 않은 변수를 조회시 오류
#   print('인덱싱 할 수 없습니다')
# except KeyError:# dict에서 없는 키를 통한 조회시 오류
# except ValueError:# list에서 없는 값을 삭제시 오류
# except FileNotFoundrror:# file 조회시 파일이 없을때 오류
# except TypeError:#  다른 타입끼리 연산시 오류
#
# except ValueError as e:
#   print(e)

# else:# 오류가 나지 않을 경우에만 실행
  # print('else')

# finally:# 예외와 상관 없이 동작
#   print('final')

class MyError(Exception):
  def __str__(self):
    # return super().__str__()
    return '허용되지 않는 별명입니다'

def say_nick(nick):
  if nick == '바보':
    raise MyError()#raise 오류를 일부러 발생시키는 호출
  print(nick)

try:
  say_nick('a')
  say_nick('바보')
except MyError as e:
   print(e)


# def add(x):
#   def calcutate(y):
#     return x + y
#   return calcutate

class add:
  def __init__(self, x):
    self.x = x
  def __call__(self, y):
    return self.x + y

# print(add(2)(3))
# add2 = add(2)
# print(add2(3))


# decorator

# def trace(func):
#   def wrapper():
#     print('start')
#     func()
#     print('end')
#   return wrapper

# @trace# trace(hi)
# def hi():
#   print('hi')

# # t1 = trace(hi)
# hi()# hi = trace(hi)를 자동으로, 함수 정의 시점에 실행해 준다

def trace(func):
  def wrapper(*args, **wkargs):
    result = func(*args, **wkargs)
    print(args, wkargs, result)
    return result
  return wrapper

@trace
def big(*args):
  return max(args)

@trace
def mini(**kwargs):
  return min(kwargs.values())

print(big(10, 20))
print(mini(x=20, y=30, z=40))


class Tr:
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwds):
    print(self.func.__name__, 'start')
    self.func()
    print(self.func.__name__, 'end')


@Tr# Tr 클래스의 __init__에 hi를 전달. hi는 Tr의 인스턴스
def hi():
  print('hi')

hi()
# hi()를 호출하면, Tr의 인스턴스 이므로 __call__ 호출
