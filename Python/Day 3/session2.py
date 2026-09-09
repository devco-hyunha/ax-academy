# 리스트 컴프리헨션
a = [1, 2, 3, 4]
result = []
for num in a:
  result.append(num*3)
print(result)

a= [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)

b2 = [i for i in range(1, 31) if i % 3 == 0]
print(b2)

result = [
  x * y
    for x in range(2, 10)
      for y in range(1, 10)
]
print(result)

# 되새김 문제

a = 'Life is too short, you need python'

if 'wife' in a: print('wife')
elif 'python' in a and 'you' not in a: print('python')
elif 'shirt' not in a: print('shirt')
elif 'need' in a: print('need')
else: print('none')
# 결과값 : shirt

# while 문을 사용해 1~100까지의 자연수 중 3의 배수의 합을 구하라
result = 0
i = 1
while i <= 1000:
  if i % 3 == 0:
    result += i
  i += 1
print(result)

# whila 문을 활용하여 다음의 결과 값을 얻어라
# *
# **
# ***
# ****
# *****
i = 0
while True:
  i += 1
  if (i > 5):
    break
  print('*'*i)

# for 문을 사용해 1~ 100 까지 출력
for i in range(1, 101):
  print(i, end = ' ')
print()

# for 문을 사용해서 평균을 구하라
A = [70, 60, 55, 75, 95, 90, 80, 85, 100]
total = 0
for score in A:
  total += score
average = total / len(A)
print(average)

# 리스트 컴프리헨션 사용
# numbers = [1, 2, 3, 4, 5]
# result = []
# for n in numbers:
#   if n % 2 == 1:
#     result.append(n * 2)

result = [n * 2 for n in [1, 2, 3, 4, 5]]
print(result)
