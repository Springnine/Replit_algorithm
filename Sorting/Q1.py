# 두 배열의 원소 교체

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0

def sort(array, reverse):
  arr = []
  count = [0] * (max(array) + 1)

  for i in array:
    count[i] += 1
  if reverse == 0:
    for i in range(len(count)):
      for j in range(count[i]):
        arr.append(i)
  else:
    for i in range(len(count)-1, 0, -1):
      for j in range(count[i]):
        arr.append(i)
  return arr

b = sort(b, 1)
a = sort(a, 0)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break;

for i in range(len(a)):
  result += a[i]

print(result)

""" 
- Solution

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  a[i], b[i] = b[i], a[i]

print(sum(a))

"""
