// [문제 링크]: https://www.acmicpc.net/problem/1766

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import heapq
​
N, M = map(int, input().split())
indegree = [0] * (N + 1)
p = defaultdict(list)
​
for _ in range(M):
    a, b = map(int, input().split())
    indegree[b] += 1
    p[a].append(b)
​
q = []
ans = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
​
while q:
    node = heapq.heappop(q)
    ans.append(node)
    for next_node in p[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            heapq.heappush(q, next_node)
​
print(*ans)
​