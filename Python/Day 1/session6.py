# 튜플
# 리스트는 [], 튜플은 ()

# 튜플의 요소가 하나일 경우 쉼표를 붙여야 한다.
# 값이 변하지 않는 데이터에 사용 

t1 = ()
t2 = (1,)
t3 = (1, 2, 3, 4, 5)
t4 = 1, 2, 3, 4, 5
t5 = ('a', 'b', ('c', 'd', 'e'))

print(t1, t2, t3, t4, t5)
print(type(t1), type(t2), type(t3), type(t4), type(t5))

# 수정, 삭제 불가

#인덱싱
print(t3[0])
print(t3[3])
print(t5[2][1])

# 슬라이싱
print(t3[1:4])
print(t5[2][1:3])

# 연산
print(t3 + t4)
print(t3 * 3)
print(str(t3[0]) + 'hi')

# 길이
print(len(t3))