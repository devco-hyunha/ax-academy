# id
a = 3
print(id(3))
print(id(a))

b = a
print(id(b))
print(b is a) # 같은 객체를 가리키고 있는지 확인

# 얕은 복사
# from [] import [] - 외부 모듈에서 함수를 가져오는 것
from copy import copy
a2 = [1, 2, 3]
b2 = copy(a2)
print(b2 is a2)
print(id(a2))
print(id(b2))

#2장 되새김 문제
# 1. 평균 점수 구하기
sco = {
  'korean': 80,
  'english': 75,
  'math': 55
}

sum = 0
for value in sco.values():
  sum += value

# 2. 자연수 13이 홀수 인지 짝수 인지
n1 = 13
if n1 % 2 == 1:
  print('홀수')
else :
  print('짝수')

# 5. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# 6. 리스트 역순
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

# 7. 리스트 → 문자열
a = ['Life' , 'is', 'too', 'short']
result = ' '.join(a)
print(result)

# 8. 튜플 더하기
a = (1, 2, 3)
a += (4,)
print(a)

# 9. 딕셔너리 키
a = dict()
# a['name'] = 'python' # 가능
# a[('a', )] = 'python' # 가능
# a[[1]] = 'python' #불가능: array는 키로 활용할 수 없음
# a[250] = 'python' # 가능

# 10. 딕셔너리 값 추출
a = { 'A': 90, 'B': 80, 'C': 70 }
result = a.pop('B')
print(a)
print(result)

# 11. 리스트 중복 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5]
aSet = set(a)
b = list(aSet)
print(b)

# 12. 파이썬 변수
a = b = [1, 2, 3] # a, b 는 동일한 id를 가지고 있기 때문
a[1] = 4
print(b)
