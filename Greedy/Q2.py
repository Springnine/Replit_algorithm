# 곱하기 혹은 더하기

s = input()
result = int(s[0])

for i in range(1, len(s)):
  num = int(s[i])
  
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)

""" 
- Solution

data = input() 
result = int(data[0])

for i in range(1, len(data)): 
  num = int(data[i]) 

  if num <= 1 or result <= 1: 
    result += num 
  else: 
    result *= num 

print(result) 

"""