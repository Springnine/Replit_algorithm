# 왕실의 나이트

pos = input()
row = int(pos[1])
cal = int(ord(pos[0])) - int(ord('a')) + 1
count = 0

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_cal = cal + step[1]
  if next_row >= 1 and next_row <= 8 and next_cal >= 1 and next_cal <= 8:
    count += 1

print(count)