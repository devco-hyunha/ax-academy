# 집합
# 순서 없음, 중복 안됨

s1 = set()
s2 = set([1, 2, 3, 4])# 리스트 자료형을 집합 자료형으로 변호나
s3 = set([1, 4, 6, 7])
s4 = set([1, 2, 'apple', 'mango', 'python'])
s5 = {'phone', 'computer', 'notebook', 'water', 'phone'}
s6 = {12, 'mouse', (1, 2, 3), 3.14}

print( type(s1), type(s2), type(s3), type(s4), type(s5), type(s6) )

t = tuple(s2)
print(t, type(t), s2)
print(t[0], t[1:3])


# list로 변환 할 때, 입력한 순서가 유지 안됨
li1 = list(s3)
li2 = list(s4)
print(li1, type(li1))
print(li2, type(li2))

set1 = set([1, 2, 3, 4, 5, 6])
set2 = set([4, 5, 6, 7 ,8, 9])

# 교집합
print(set1 & set2)
print(set1.intersection(set2))

# 합집합
print(set1 | set2)
print(set1.union(set2))

# 차집합
print(set1 - set2)
print(set1.difference(set2))

# 두 집합이 서로소인지 확인
print(set1.isdisjoint(set2))

# 부분집합 확인
print(set1.issubset(set2))

# 상위집합 확인
print(set1.issuperset(set2))

a = set([1, 2, 3, 4])
# 요소 추가
a.add(5)

# 요소 추가
a.update([6, 7, 8])

# 요소 삭제
# 요소가 없으면 에러 발생
a.remove(5)
# 요소가 없어도 에러 발생 안함
a.discard(6)

# 모든 요소 삭제
a.clear()
