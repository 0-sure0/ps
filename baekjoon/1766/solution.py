// [문제 링크]: https://www.acmicpc.net/problem/1766

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import heapq
​
​
def solution():
    n, m = map(int, input().split())
    indegree = [0] * (n + 1)
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
​
    q = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
​
    answer = []
    while q:
        cur = heapq.heappop(q)
        answer.append(cur)
        for node in graph[cur]:
            indegree[node] -= 1
            if indegree[node] == 0:
                heapq.heappush(q, node)
​
    print(*answer)
    return
​
​
solution()
​