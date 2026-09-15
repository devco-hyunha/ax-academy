#이터레이터
a = [1, 2, 3]
ia = iter(a)

print(type(ia))# <class 'list_iterrator'>

next(ia)
next(ia)
next(ia)
# next(ia)# 리턴할 값이 없으면, StopIteration 예외 발생

ia = iter(a)
for i in ia:
  print(i)
# for 문을 사용하면 자동으로 값을 호출 하므로 예외를 신결쓸 필요 없다
# for 문을 재 호출 할경우 재 동작 하지 않는다
for i in ia:
  print(i)

it = [1, 2, 3, 4, 5].__iter__()# iter 선언과 동일
print(next(it))

# class MyIterater:
#   def __init__(self, data):
#     self.data = data
#     self.position = 0

#   def __iter__(self):
#     return self

#   def __next__(self):
#     if self.position >= len(self.data):
#       raise StopIteration
#     result = self.data[self.position]
#     self.position += 1
#     return result

# if __name__ == '__main__':
#   i = MyIterater([1, 2, 3])
#   for item in i:
#     print(item)

class Cnt:
  def __init__(self, stop):
    self.current = 0
    self.stop = stop

  def __iter__(self):
    return self

  def __next__(self):
    if self.current < self.stop:
      result = self.current
      self.current += 1
      return result
    else:
      raise StopIteration

c = Cnt(5)
for i in Cnt(5):
  print(i)

# 제너레이터
# 이터레이터를 생성해주는 함수
# __iter__, __next__ 없이 yield 만으로 이터레이터 생성
# 메모리 효율성이 좋다
# 상태 유기가 자동으로 됨 - 별도로 변수를 관리할 필요성이 없음
# 메모리 절약, 속도 샹항, 문법 간결
# 제너레이터는 이터레이터의 일부

# def mygen():
#   for i in range(1, 100):
#     result = i * i
#     yield result

# gen = mygen()

def get():
  for i in range(1, 100000):
    yield i * 2
g = get() #제너레이터 객체만 생김
print(next(g)) #한개씩 계산되어 나옴

