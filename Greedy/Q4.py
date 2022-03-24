#상하좌우

n = int(input())
t = list(map(str, input().split()))
x, y = 1, 1

array = [[0] * n for _ in range(n)]

for i in range(len(t)):
  if(t[i] == 'R' and y<n):
    y += 1
  elif(t[i] == 'L' and y>1):
    y -= 1
  elif(t[i] == 'U' and x>1):
    x -= 1
  elif(t[i] == 'D' and x<n):
    x += 1
  else:
    continue

print(x, y)

"""
- Solution

n = int(input())
x, y = 1, 1
plans = input().split()

#     L, R, U, D에 따른 이동 방향
dx = [0, 0 , -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
   # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:  
    continue
  x, y = nx, ny
print(x, y)

"""
