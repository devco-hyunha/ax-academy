import asyncio

# 코루틴 함수 정의
async def show(text, sec):  # 비동기 함수
  print('start')
  await asyncio.sleep(sec)  # 비동기 함수 대기
  print(f'{text} end')

asyncio.run(show('Hello, World!', 3))


async def main():
  # 비동기 함수 동시 실행
  await asyncio.gather(
    show('Hello,', 2),
    show('World!', 1)
  )

asyncio.run(main())


# 쓰레드
import threading
import time

def download(name, sec):
  print(f'{name} start')
  time.sleep(sec)
  print(f'{name} end, {sec} delay')

t1 = threading.Thread(target=download, args=('t1', 2))
t2 = threading.Thread(target=download, args=('t2', 3))

t1.start()
t2.start()

t1.join()
t2.join()

print('all done')

# 쓰레드와 비동기의 차이점
# 쓰레드는 동시에 여러 작업을 수행할 수 있지만, 비동기는 동시에 여러 작업을 수행할 수 없다.
# 여러 작업 동시 vs 작업을 분할
