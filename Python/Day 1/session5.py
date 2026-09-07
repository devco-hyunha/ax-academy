# 리스트
# 파이썬에서는 배열을 제공하지 않는다
# 리스트 (순서, 중복, 수정, 삭제) 가능

list1 = []
list2 = list()

print(list1, list2)
print(type(list1), type(list2))

list3 = [1, 2, 3, 4, 5]
list4 = [1, 2, 'three', 'four', 'five']
list5 = [1, 2, ['three', 'four', 'five']]
list6 = [1.23, 'hello', True, False, None]
list7 = list(range(1, 10))

print(list4[0] + list4[1])

print(list3, list4, list5, list6, list7)
print(type(list3), type(list4), type(list5), type(list6), type(list7))

list9 = list(range(1, 10, 2))
list10 = list(range(1, 10, 3))

print(list9, list10)
print(type(list9), type(list10))


# 인덱싱
print(list4[1])
print(list4[0] + list4[1] + list4[1])
print(list4[-1])
print(list4[-1][1])

# 슬라이싱
print(list4[0:3])
print(list4[2:])
print(list4[2][1:3])

# 연산
print(list3 + list4)
print(list3 * 3)
print(str(list3[0]) + 'hi')
print(list4[2] + 'hi')

# 수정
list3[0] = 4
print(list3)

list3[1:2] = ['a', 'b', 'c']
print(list3)

# 삭제
list3[1:2] = []
print(list3)

del list3[1]
print(list3)

del list3[1:3]
print(list3)


# 리스트 함수
a = [5, 4, 3, 2, 1]
# append
a.append(6)
print(a)

# sort
a.sort()
print(a)

# reverse
a.reverse()
print(a)

# index
print(a.index(5))

# insert
a.insert(2, 7)
print(a)

# remove
a.remove(1) # 첫번째 1 값만 제거
print(a)

# pop
print(a.pop())
print(a)

# count
print(a.count(3))

# extend
a.extend([8, 9, 10])
print(a)

# print(a.index(3))

