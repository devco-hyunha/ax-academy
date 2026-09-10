# 파일 입출력
# 객체 변수 = open(파일 명, 파일 열기 모드)
# 파일 열기 모드 - r: 읽기, w: 쓰기(파일 생성), a: 추가

# 'w'모드로 파일을 오픈할때, 동일 파일이 이미 존재 할때, 원래 있던 내용은 삭제
# 'w'모드로 open 시, 작업 후 close() 필수
# f = open('./resource/news.txt', 'w')
# 폴더가 없을 경우 오류

f = open('./resource/news.txt', 'r', encoding='UTF-8')

print(f)
print(f.encoding)
print(f.name)
print(f.mode)
print(f.readline())
print(f.readlines())
print(f.read())
f.close()

f = open('./resource/news.txt', 'r', encoding='UTF-8')
for line in f:
  print(line)
f.close()

f = open('./resource/news.txt', 'w', encoding='UTF-8')
for i in range(1, 20):
  data = '%d번째 줄입니다\n' % i
  f.write(data)

f.close()

# with open('./resource/news.txt', 'w') as f:
#   f.write("Life is to short, you need python")

with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
  c = f.read()
  print(type(c))
  print(list(c))
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
  c = f.read(30)
  print(type(c))
  print(c)

with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
  while True:
    line = f.readline()
    if not line: break
    print(line)
  
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
  lines = f.readlines()
  print(lines)

with open('./resource/test2.txt', 'w', encoding='UTF-8') as f:
  li = ['1\n', '2\n', '3\n']
  f.writelines(li)

