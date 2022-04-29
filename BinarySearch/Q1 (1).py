# 떡볶이 떡 만들기

def binary_search(array, target, start, end):
  result = 0
  while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in range(len(array)):
      if array[i] > mid:
        sum += array[i] - mid
    if sum < target:
      end = mid - 1
    else:
      result = mid
      start = mid + 1
  return result
        

n, m = map(int, input().split())
array = list(map(int, input().split()))
result = 0

array.sort()

a = binary_search(array, m, 0, max(array))
print(a)