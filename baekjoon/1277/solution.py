// [문제 링크]: https://www.acmicpc.net/problem/1277

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import math
import heapq
​
​
N, W = map(int, input().split())
M = float(input())
factory = [0] * (N + 1)
graph = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]
​
​
for i in range(1, N + 1):
    x, y = map(int, input().split())
    factory[i] = (x, y)
​
for _ in range(W):
    a, b = map(int, input().split())
    graph[a][b] = 0
    graph[b][a] = 0
​
​
def get_distance(a, b):
    return math.sqrt((factory[a][0] - factory[b][0]) ** 2 + (factory[a][1] - factory[b][1]) ** 2)
​
​
dist = [sys.maxsize] * (N + 1)
dist[1] = 0
q = []
heapq.heappush(q, (0.0, 1))
while q:
    d, node = heapq.heappop(q)
    for next_node in range(1, N + 1):
        if node == next_node:
            continue
        new_d = get_distance(node, next_node)
        w = min(new_d, graph[node][next_node])
        
        if d + w < dist[next_node]:
            dist[next_node] = d + w
            heapq.heappush(q, (d + w, next_node))
​
print(int(dist[N] * 1000))
​
​