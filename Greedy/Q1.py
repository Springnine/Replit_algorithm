N = 1260
n=0

array = [500, 100, 50, 10]

for coin in array:
  n += N // coin
  N %= coin

print(n)