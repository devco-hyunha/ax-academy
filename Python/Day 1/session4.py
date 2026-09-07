
#format 함수
print('I eat {0} apples'.format(3))

print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two')) # 인덱스 1과 0을 사용하여 출력

print('{0:06d}'.format(15)) # 6자리 빈 문자열에 15를 채움, 0으로 채움
print('{0:06d}'.format(-15)) # 6자리 빈 문자열에 -15를 채움, 0으로 채움

print('{0:f}'.format(3.14)) # 3.14를 소수점 6자리까지 출력
print('{0:10f}'.format(3.14)) # 10자리 빈 문자열에 3.14를 소수점 6자리까지 출력
print('{0:10.4f}'.format(3.14)) # 10자리 빈 문자열에 3.14를 소수점 4자리까지 출력
print('{0:10.4f}'.format(3.14)) # 10자리 빈 문자열에 3.14를 소수점 4자리까지 출력


# 문자열 포멧팅
name = '홍길동'
age = 30

str1 = f'저는 {name}입니다. 나이는 {age}살입니다.'
print(str1)

str2 = '저는 {0}입니다. 나이는 {1}살입니다.'.format(name, age)
print(str2)


x = 10
y = 30
z = 'Lee'

# c스타일(서식문자)
test1 = 'z=%s, sum=%d' % (z, (x + y))
print(test1)

test2 = 'z={z}, sum={sum}'.format(z = z, sum = (x + y))
print(test2)

#정렬
print('{0:<10}'.format('hi')) # 10자리 빈 문자열에 hi를 왼쪽 정렬로 채움
print('{0:>10}'.format('hi')) # 10자리 빈 문자열에 hi를 오른쪽 정렬로 채움
print('{0:^10}'.format('hi')) # 10자리 빈 문자열에 hi를 중앙 정렬로 채움
print('{0:*^10}'.format('hi')) # 10자리 빈 문자열에 hi를 중앙 정렬로 채움, *로 채움

print(f'{"hi":<10}') # 10자리 빈 문자열에 hi를 왼쪽 정렬로 채움
print(f'{"hi":>10}') # 10자리 빈 문자열에 hi를 오른쪽 정렬로 채움
print(f'{"hi":^10}') # 10자리 빈 문자열에 hi를 중앙 정렬로 채움
print(f'{"hi":*^10}') # 10자리 빈 문자열에 hi를 중앙 정렬로 채움, *로 채움

n = 50
print(f'{n:^10}')
print(f'{n:_<20}')

# 문자열 내장 함수

# count 함수
print('hobby'.count('b'))

# find 함수
print('hobby'.find('b'))

# index 함수
print('hobby'.index('b'))

# join 함수
print(' '.join('hobby'))
print(', '.join(['a', 'b', 'c']))

# upper 함수
print('hobby'.upper())

# lower 함수
print('hobby'.lower())

# lstrip 함수
print('  hi  '.lstrip())

# rstrip 함수
print('  hi  '.rstrip())

# strip 함수
print('  hi  '.strip())

# replace 함수
print('hobby'.replace('b', 'c'))

# split 함수
print('a b c d'.split())
print('a:b:c:d'.split(':'))
print('a:b:c:d'.split(':', 1))
print('a:b:c:d'.split(':', 2))
print('a:b:c:d'.split(':', 3))
print('a:b:c:d'.split(':', 4))
print('a:b:c:d'.split(':', 5))