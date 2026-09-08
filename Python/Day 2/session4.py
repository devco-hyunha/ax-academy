#if boolean
# 참: "javascript", ["python"], (10), {a:3}, 1, {'aa'}
# 거짓: "" [] () {} 0 None

# and, or, not
money = 2000
card = True
print(money > 3000 and card)
print(money > 3000 or card)
print(not money > 3000)

# in, not in
x = [10, 20, 30]
y = {70, 80, 90, 100}
z = { "name": "kim", "city": "seoul", "id": "gildong" }
m = (10, 20, 24)

print(25 in x)
print(90 in y)
print(20 not in m)
print("city" in z)
print("gildong" in z.values())

#중첩 조건문
grade = 'A'
total = 85

if grade == 'A':
  if total >= 90:
    print('장학생')
  elif total>= 80:
    pass
  else:
    print('학생')
else:
  print('재시험')


# while 조건:
#   실행코드
num = 5
while num > 0:
  print(num)
  num -= 1

n = 10
while n > 0:
  print(n)
  n -= 1
  if n == 2:
    continue

a1 = ['water', 'python', 'java', 'phone']
s1 = 'py'
i = 0

while i < len(a1):
  if a1[i] == s1:
    break
  i+=1
else:
  print('hi')