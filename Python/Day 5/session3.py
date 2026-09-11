print(list(map(lambda x: -x, range(0, 10))))


# sorted: 객체 정렬후 반환
print(sorted([5,6,2,1,2,4]))
a = sorted([5,6,2,1,2,4])
print(a)

# sum
print(sum([1,2,3,4,5]))
print(sum(range(1, 101)))


## 외부 라이브러리
# time
import time
print(time.time())# 1970. 1. 1 0:0:0을 기준으로 지난 시간을 초단위로 리턴
print(time.localtime(time.time()))# 년,월,일,시,분,초로 변환하여 리턴
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))# 정해진 포멧으로 변환

# 랜덤
import random
print(random.random())# 0.0 ~ 1.0 사이의 실수 반환
print(random.randint(1, 10))# 1 ~ 10 사이의 정수 반환

# pickle
# 객체의 형태를 유지하면서 파일을 저장하고 불러오는 모듈
import pickle
f = open('test.obj', 'wb') # 파일을 쓰기용 바이너리 모드로 열기
obj = {1: 'python', 2: 'study', 3: 'basic'}
pickle.dump(obj, f)
f.close()

with open('test.obj', 'wb') as f: pickle.dump(obj, f)

with open('test.obj', 'rb') as f: 
  data = pickle.load(f)
  print(data)

# webbrowser
# import webbrowser
# webbrowser.open('https://www.google.com')
# webbrowser.open_new('https://www.google.com')

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def multi(x, y):
  return x * y

def div(x, y):
  return x / y

# 파이썬 파일 실행할 때, 파이썬 인터프리터가 자동으로 그 파일에 __name__ 을 붙여준다
# 직접 실행하는 파일은 __name__ 이 __main__이 되고
# 다른 파일에서 import 해서 사용하는 파일은 __name__ 이 "파일명"이 된다
if __name__ == "__main__": 
  def add(x, y):
    return x + y

  def sub(x, y):
    return x - y

  def multi(x, y):
    return x * y

  def div(x, y):
    return x / y