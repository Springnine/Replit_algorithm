def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
     # 찾은 경우 중간점 인덱스 변환
    if array[mid] == target:
      return target
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
  
  """
  if start > end:
    return None
  mid = (start + end) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array,target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)
  """
n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다")

else:
  print(result + 1)