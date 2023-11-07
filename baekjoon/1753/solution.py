// [문제 링크]: https://www.acmicpc.net/problem/1753

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import heapq
​
​
V, E = map(int, input().split())
K = int(input())
edges = defaultdict(list)
INF = sys.maxsize
dist = [INF] * (V + 1)
dist[K] = 0
​
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
​
q = []
heapq.heappush(q, (0, K))
​
while q:
    d, node = heapq.heappop(q)
    if dist[node] < d:
        continue
​
    for next_node, w in edges[node]:
        if d + w < dist[next_node]:
            dist[next_node] = d + w
            heapq.heappush(q, (d + w, next_node))
​
for i in range(1, V + 1):
    print(dist[i] if dist[i] != INF else 'INF')
​
​