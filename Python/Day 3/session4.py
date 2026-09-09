# 사용자 입출력
# num = input('숫자를 입력하세요 : ')
# print(num)
# print(type(num))


# print("life" "is" "too short")
# print("life" "is" + "too short")
# print("life", "is", "too short")
# print("life", end = " ")
# print("is", "too short")

# input1 = input('첫 번째 숫자를 입력하세요:')
# input2 = input('두 번째 숫자를 입력하세요:')

# total = int(input1) + int(input2)
# print('두 숫자의 합은 %s입니다' % total)

height = input('키를 입력해 주세요: ')
print('당신의 키는 {height}cm 입니다'.format(height = height))
print(f'당신의 키는 {height}cm 입니다')

def avg(*args):
  sum = 0
  for i in args:
    sum += i
  result = sum / len(args)
  return print(result)

avg(1,2)
avg(1,2,3,4,5)