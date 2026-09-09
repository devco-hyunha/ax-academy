# for

names = ['kim', 'lee', 'park', 'choi']

for name in names:
  print(name)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
  print(first)
  print(last)

word = 'python'
for char in word:
  print(char)

profile = {
  'name': 'hong',
  'age': 33
}
for key in profile:
  print(key)
  print(profile[key])

for value in profile.values():
  print(value)

num = [34, 62, 63, 1, 35, 6, 2]
for i in num:
  if i == 35:
    print('35!')
    break
  else:
    print(i)

# is : 두 객체가 같은 타입객체(메모리 주소가 같은지) 인지 비교하는 연산자
# == : 값이 같은지 비교
# type : 하나의 고정된 타입 객체 반환

li = ['3', 1, 2, True, 4.5]

for i in li:
  if type(i) is str:
    print('true')
    continue
  print(i, type(i))

# for else 구문
# else 블록은 for 문이 break로 중간에 끊기지 않고 끝까지 실행되었을때만 실행
num = [34, 62, 63, 1, 35, 6, 2]
for i in num:
  if i == 35:
    print('35!')
    break
else:
  print('hihi')

fruit2 = 'Mango'
print(reversed(fruit2)) # 객체 주소 값 반환
print(fruit2)
print(list(reversed(fruit2))) # 객체 안에 들어 있는 값을 실제로 꺼내서 리스트로 출력
print(tuple(fruit2))
print(set(fruit2)) # 순서 유지 안됨
print(''.join(list(reversed(fruit2))))

# for 문과 함께 사용하는 range 함수
a = range(10)
print(list(a))

a = range(1, 10)
print(list(a))

a = range(1, 10, 2)
print(list(a))

for i2 in range(1, 11):
  print(i2)

i = 1
while(i<=10):
  print(i)
  i += 1

print()

for i3 in range(1,11,2):
  print(i3, end = ' ')
print()

for i in range(2, 10):
  for j in range(2, 10):
    print(i, end = ' x ')
    print(j, end = ' = ')
    print(i * j, end = ' ')
  print()

msg = 'It is Time'
for index in range(len(msg)):
  if msg[index].isupper():
    print(msg[index], end = ' ')

print()
print('홀수: ', end = '')
for i in range(1, 11):
  if i%2 == 0:
    continue
  print(i, end = ' ')
print()

print('3~32까지 수 중 3의 배수: ', end = '')
for i in range(3, 33, 3):
  print(i, end = ' ')
print()
