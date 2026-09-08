# 튜플 패킹(packing)
tu22 = ( 'phone', 'book', 'computer', 'mouse' )
print(tu22)
# 튜플 언패킹(unpacking)
(w, x, y, z) = tu22
print(w, x, y, z)

# 딕셔너리
# 순서 없음, 키 중복 안됨, 수정/삭제 가능
# javascript의 json과 동일 형식
dic1 = { "name" : "Lee", "phone" : "010-0000-0000", "birth" : "001122" }
dic2 = { 0 : "python" }
dic3 = { 'ary' : [ 1, 2, 3, 4 ]}
dic4 = {
  'name': 'tom',
  'addr': 'seoul',
  'age': '22',
  'grade': 'A',
  'status': True
}
dic5 = dict()
dic6 = dict([ ( 'name', 'tom' ), ( 'addr', 'seoul' ), ( 'age', '22' ), ( 'grade', 'A' ), ( 'status', True ) ])
# 가장 안쪽 구조 : 튜플 구조
# 안쪽을 감싸는 구조: 리스트 구조(여러 개의 튜플을 하나로 묶음 → 튜플의 리스트)
# 가장 바깥쪽 구조 : 딕셔너리 구조로 변환
# (키, 값) 튜플 → 딕셔너리 {키: 값}
# dict() 는 인자를 1개만 받을 수 있음

# key를 이용해 value 값 추출
# 딕셔너리명['키']
# print(dic1['name1']) # 키가 없으면 KeyError 오류
print(dic1.get('name1')) # 키가 없으면 None

# 키가 중복 될 경우 마지막 키:값만 노출
a = { 1: 'c', 1: 'a', 1: 'b', 1: 'd' }
print(a) 

dic1['address'] = 'yongsan'
print(dic1)

dic1['score'] = [90, 30, 40]
print(dic1)
print(len(dic1))

# key
print(dic1.keys())
print(list(dic1.keys()))
for k in dic1.keys():
  print(k)

# value
print(dic1.values())
print(list(dic1.values()))
for v in dic1.values():
  print(v)

# items - (key, value) 튜플 목록
print(dic1.items())
print(list(dic1.items()))

# pop - 값을 꺼내고, 딕셔너리에서 키를 삭제
print(dic1.pop('birth'))
print('birth' in dic1) # 키를 삭제 했기때문에 False

# clear
dic1.clear()
print(dic1)


# 1
odd = [1, 3, 5, 7, 8]
print(odd[0])
print(odd[1])

odd[0] = 10

# 2
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# 리스트를 합쳐본다
c = a + b
# a.extend(b)

# a리스트에 마지막 요소에 6을 추가한다
a.append(6)

# 인덱스 3에다 정수 7을 삽입
a.insert(3, 7)

# 맨 마지막 값을 삭제해본다
a.pop()
# 인덱스 3을 삭제한다
del a[3]

# 숫자 4를 삭제한다
a.remove(4)

# 숫자 5의 위치를 알아낸다
print(a.index(5))