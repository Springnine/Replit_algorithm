# 퀵 정렬

array = list(map(int, input().split()))

def quick(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료
    return
  pivot = start # 피벗은 첫 번째 원소
  left = start + 1
  right = end

  while(left <= right):
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while(right >= left and array[right] >= array[pivot]):
      right -= 1
    if(left > right): # 엇갈렸으면 피벗과 작은 데이터 교체
      array[pivot], array[right] = array[right], array[pivot]
    else: # 엇갈리지 않았으면 작은 데이터와 큰 데이터 교체
      array[right], array[left] = array[left], array[right]
  # 분할 이후 왼쪽 부분과 오른쪽 부분 각각 정렬 수행
  quick(array, start, right - 1)
  quick(array, right + 1, end)
  
quick(array, 0, len(array) - 1)
print(array)
