i = 0
while True:
  i += 1
  if i%2 == 0:
    print(i)
  elif i>=10:
    break

dic = { 'name': 'tom', 'age': '11' }
dic['subject'] = 'python'
del dic['name']
print(dic)

li1 = [1, 2, 3]
st1 = set(li1)
print(st1)

st1 = 'python'
li2 = list(st1)
print(li2)

s4 = set([1, 2, 3, 4, 5])
s5 = set([6, 7, 8, 9, 10])
print(s4.intersection(s5))
print(s4.union(s5))
