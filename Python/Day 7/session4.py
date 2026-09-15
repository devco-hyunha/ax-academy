# def gen1():
#   yield 0
#   yield 1
#   yield 2

# g1 = gen1()
# a = next(g1)
# print(a)

# for i in gen1():
#   print(i)

# def even_gen():
#   num = 0
#   while True:
#     yield num
#     num += 2

# class even_gen:
#   def __init__(self):
#     self.current = 0

#   def __iter__(self):
#     return self

#   def __next__(self):
#     result = self.current
#     self.current += 2
#     return result


# g = even_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# login_state = False

# def login(func):
#   def wrapper():
#     if not login_state:
#       print('로그인')
#       return
#     return func()
#   return wrapper

# @login
# def write_post():
#   print('글 작성 완료')

# write_post()

# login_state = True
# write_post()


#json
import json

def loading():
  try:
    with open('myinfo.json', 'r', encoding='UTF-8') as f:
      return json.load(f)
  except FileNotFoundError:
    print('no file')

d = {
  'name': '홍길동',
  'birth': '0525',
  'age': 30
}

def add(data):
  with open('C:/AX Academy/study/Python/Day 7/stu.json','w',encoding='UTF-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    # indent: indent 만큼의 들여쓰기로 보기 좋게 정렬
    # ensure_ascii: 테이터를 저장항때 아스키로 변환 하지 않는다

data = [
  { 'name': 'Tom', 'score': 100 },
  { 'name': 'Juli', 'score': 80 }
]

add (data)
print('저장')