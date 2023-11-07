// [문제 링크]: https://www.acmicpc.net/problem/1277

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import math
import heapq
​
​
N, W = map(int, input().split())
M = float(input())
factory = [0] * (N + 1)
graph = defaultdict(list)
​
​
def get_distance(a, b):
    return math.sqrt((factory[a][0] - factory[b][0]) ** 2 + (factory[a][1] - factory[b][1]) ** 2)
​
​
for i in range(1, N + 1):
    x, y = map(int, input().split())
    factory[i] = (x, y)
​
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        d = get_distance(i, j)
        if d <= M:
            graph[i].append((d, j))
            graph[j].append((d, i))
​
for _ in range(W):
    a, b = map(int, input().split())
    graph[a].append((0, b))
    graph[b].append((0, a))
​
​
dist = [sys.maxsize] * (N + 1)
dist[1] = 0
q = []
heapq.heappush(q, (0.0, 1))
while q:
    d, node = heapq.heappop(q)
    if dist[node] < d:
        continue
​
    for w, next_node in graph[node]:
        if d + w < dist[next_node]:
            dist[next_node] = d + w
            heapq.heappush(q, (d + w, next_node))
​
print(int(dist[N] * 1000))
​
​