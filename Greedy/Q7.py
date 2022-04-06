# 문자열 재정렬
s = input()
sum = 0
word = []
for i in range(len(s)):
  if 47 < ord(s[i]) < 58:  # 숫자
    sum += int(s[i])
  elif 64 < ord(s[i]) < 91 or 96 < ord(s[i]) < 123: # 문자
    word.extend(s[i])
  
for i in range(len(word)):
  for j in range(0, len(word) - i - 1):
    if word[j] > word[j + 1]:
      word[j], word[j + 1] = word[j + 1], word[j]

word.append(str(sum))

result = ''.join(str(w) for w in word)

print(result)

# 개선점 : isalpha 와 sort 라이브러리를 사용하기

"""
Solution

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
  # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
      result.append(x)
  # 숫자는 따로 더하기
  else:
    value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하면 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))

"""
