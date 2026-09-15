def calc(oper, *args):
  try:
    if oper == 'add':
      print(sum(args))
      return sum(args)
    elif oper == 'mul':
      result = 1
      for x in args:
        result *= x
      print(result)
      return result
    elif oper == 'avg':
      print(sum(args) / len(args))
      return sum(args) / len(args)
    else:
      raise ValueError('잘못된 연산입니다')
  except ValueError as e:
    print(e)
    return None

calc("add", 1,2,3) # 6
calc("mul", 1,2,3,4) # 24
calc("avg", 10,20,30) # 20


# 사용자에게 나이 입력 받기
# 숫자가 아니면 예외 처리
# (0 이하 입력하면 사용자 정의 예외 발생)
# 정상 입력 시 "입력 완료"
class AgeError(Exception):
  def __str__(self):
    return "나이는 0보다 작을수 없습니다"

try:
  age = int(input('나이를 입력하세요: '))
  if age < 0:
    raise AgeError()
  print('입력 완료')
except ValueError as e:
  print('숫자만 입력해야 합니다')
except AgeError as e:
  print(e)
