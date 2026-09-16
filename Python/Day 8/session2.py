import threading
import time

def game(name):
  print(f'{name} start')
  time.sleep(2)
  print(f'{name} end')


names = ['t1', 't2', 't3', 't4', 't5']

threads = []
for name in names:
  # 반복문 안에서 스레드 생성
  t = threading.Thread(target=game, args=(name,))
  threads.append(t)
  t.start()  # 스레드 시작

for t in threads:
  t.join()  # 모든 스레드 종료 대기
  # 스레드 자체가 비동기적으로 실행되기 때문에, join을 하면 모든 스레드가 종료될 때까지 대기한다.

# start를 먼저 실행 한다고 해서 순서가 보장되지 않는다.
print('all done')

