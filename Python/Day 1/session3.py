
str1 = "Python interesting"
print('str1[7]:', str1[7])
print('str1[0:3]:', str1[0:3]) # 0~2 까지 출력
print('str1[4:]:', str1[4:]) # 4~끝까지 출력
print('str1[1:4]:', str1[1:4]) # 1~3 까지 출력
print('str1[:3]:', str1[:3]) # 0~2 까지 출력
print('str1[1:]:', str1[1:]) # 1~끝까지 출력
print('str1[:]:', str1[:]) # 0~끝까지 출력
print('str1[:len(str1)]:', str1[:len(str1)]) # 문자열 전체를 출력
print('str1[1:-2]:', str1[1:-2]) # 1~끝-2 까지 출력
print('str1[-4:-2]:', str1[-4:-2]) # 끝-4~끝-2 까지 출력
print('str1[1:4:2]:', str1[1:4:2]) # 1~3 까지 2의 배수 인덱스 출력
print('str1[::2]:', str1[::2]) # 0 부터 2의 배수 인덱스 출력
print('str1[::-1]:', str1[::-1]) # 문자열 전체를 역순으로 출력

#test case 1: 주민번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print('yyyymmdd:', yyyymmdd)
print('num:', num)

#test case 2: 주민번호 성별 나누기
pin = "881120-1068234"
gender = pin[7]
print('gender:', gender)

#format = c스타일(%s:문자열, %d:정수, %f:실수, %c: character, %e: 과학적 표기법)
# - %s에서 s는 string(문자열)의 약자
# - %d에서 d는 decimal(정수)의 약자
# - %f에서 f는 float(실수)의 약자
# - %c에서 c는 character(문자)의 약자
# - %e에서 e는 exponential(과학적 표기법)의 
print('문자열 %s와 문자열 %s가 있다' %('one', 'two'))
print('정수 %d와 정수 %d가 있다' %(3, 4))
print('실수 %f가 있다' %(3.14)) # %f는 소수점 6자리까지 출력

# %10s는 10자리 문자열을 출력
# %[숫자][type]는 숫자만큼 %[type]을 출력, 오른쪽 정렬
# %[-숫자][type]는 숫자만큼 %[type]을 출력, 왼쪽 정렬

print('%10s' %('hi')) # 오른쪽 정렬
print('%-10s' %('hi')) # 왼쪽 정렬

# test case 3: 정수 4, 6을 입력 → %d 로 출력
print('정수 %d, %d를 출력' %(4, 6))

# test case 4: python 이라는 문자를 20자리에서 오른쪽 정렬로 출력
print('%20s' %('python'))

# 소수점 표현
print('%0.4f' %(3.141592653589793)) # 소수점 4자리까지 출력
print('%10.4f' %(3.141592653589793)) # 최소 정수 10자리에 소수점 4자리까지 출력
print('%10.4f' %(1234567890123.141592653589793)) # 최소 정수 10자리에 소수점 4자리까지 출력
