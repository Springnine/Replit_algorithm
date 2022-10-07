# 전보
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
  if d != 1e9:
    count += 1
    max_distance = max(max_distance, d)

print(count - 1, max_distance)


""" 워셜로 구현( 노드가 많아지면 시간초과 판정을 받을 수 있음 )
INF = int(1e9)
n, m, c = map(int, input().split())
t = 0
num = 0

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x][y] = z

for k in range(1, n + 1):
  for x in range(1, n + 1):
    for y in range(1, n + 1):
      graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])


for i in range(1, n + 1):
  if graph[c][i] != 0 and graph[c][i] != INF:
    num += 1
print(num, end=" ")

for x in range(1, n + 1):
  for y in range(1, n + 1):
    if graph[x][y] != INF:
      t = max(t, graph[x][y]) 

print(t, end=" ")
"""