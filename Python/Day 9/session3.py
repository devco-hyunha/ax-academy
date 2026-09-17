#csv

import csv

weather1_path = 'C:/AX Academy/study/resource/weather1.csv'

with open(weather1_path, 'r') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row)

print('-' * 50)
with open(weather1_path, 'r') as file:
  reader = csv.DictReader(file)
  for row in reader:
    for key, value in row.items():
      print(key, value)


import os
# 디렉터리, 파일 등 os자원 제어해주는 모듈

file_path="C:/test2/a.txt"

#경로 존재 확인
print(os.path.exists(file_path))

#파일인지 디렉토리인지 확인
print("파일 여부", os.path.isfile(file_path))
print("디렉토리 여부", os.path.isdir(file_path))

dir_name=os.path.dirname(file_path)
base_name=os.path.basename(file_path)
print("디렉토리", dir_name)
print("파일명", base_name)

#경로 합쳐봄
new_path=os.path.join(dir_name, "backup","report_a.txt")
print("합친 경로", new_path)


#특정 디렉토리 안에있는 파일 목록 순회함
target_dir="." #현재 작업 디렉토리

for i in os.listdir(target_dir):
    full_path=os.path.join(target_dir, i)
    if os.path.isfile(full_path):
        size=os.path.getsize(full_path) #파일의 크기를 바이트 단위로 가져옴
        print(i, size)