a = 1
def vartest(a):
  a = a + 1

vartest(a)
print(a)

add = lambda a, b: a + b
result = add(3, 4)
print(result)

def multi(x, y):
  return x * y

multi = lambda x, y: x * y
print(multi(3, 4))

def plus(x):
  return x + 10
plus = lambda x: x + 10
print(plus(1))

a = multi # 함수명을 a에 할당함 (a = alias - 별칭)
print(a(4, 5))

def final(x, y, func1):
  print(x, y, func1(5, 6))

final(1, 2, multi)

dict = {}
while True:
  name = input('이름?')
  tv = input('좋아하는 방송?')
  dict[name] = tv

  ans = input('친구한테 물어볼까?')
  if ans == 'no':
    break
print(dict)

li1 = [i for i in range(1, 6)]
li2 = list(range(1, 6))
print(li1)
print(li2)