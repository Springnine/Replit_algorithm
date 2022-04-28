# 계수 정렬

array = list(map(int, input().split()))

count = [0] * (max(array) + 1)

for i in array:
  count[i] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')