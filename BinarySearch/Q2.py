# 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

result = array.count(x)


if result == 0:
  print("-1")
else:
  print(result)

"""
# Solution

def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)
  if (right_index - left_index) == 0:
    return -1
  return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

print(count_by_range(array, x, x))

"""

