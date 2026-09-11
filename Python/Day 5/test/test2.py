# test.py 파일에 있는 add 와 multi 함수 호출

# import test
# print(test.add(1, 2))

# from test import *

# print(add(1, 2))


# 3
all([1, 2, abs(-3) -3])
# >>> False

chr(ord('a')) == 'a'
# >>> True

# 4
list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))

# 7
a = [-8, 2, 7, 5, -3, 5, 0, 1]
b = min(a) + max(a)

# 8
round(17 / 3, 4)

# 11
import time
now = time.localtime(time.time())
formatTime = time.strftime('%Y/%m/%d %H:%M:%S', now)

# 12
import random
ball = list(range(1, 46))
loop = list(range(6))

lotto = list(
  map(
    lambda i: ball.pop(
      random.randint(0, len(ball) - 1)
    )
    , loop))

# 17
people = ['김승현', '김진호', '강춘자', '이예준', '김현주']
work = ['청소', '빨래', '설거지']
etc = '휴식'

random.shuffle(people)

for i, p in enumerate(people):
  print(len(work), i)
  if len(work) == i:
    work.append(etc)

print(list(zip(people, work)))