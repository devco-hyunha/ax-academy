def score1(name, score):
  with open('./score1.txt','a', encoding='UTF-8') as f:
    f.write(f'{name}, {score}\n')

score1('홍길동', 100)
score1('김길동', 90)

def average():
  sum = 0
  cnt = 0
  try:
    with open('./score1.txt','r', encoding='UTF-8') as f:
      lines = f.readlines()
      for i in lines:
        i = i.strip()
        name, score = i.split(',')
        if score: 
          sum += int(score.strip())
          cnt += 1
    return (sum / cnt)
  except FileNotFoundError:
    print('파일이 없습니다')

avg = average()
print(avg)