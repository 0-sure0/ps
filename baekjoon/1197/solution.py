// [문제 링크]: https://www.acmicpc.net/problem/1197

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import heapq
​
​
def solution():
    v, e = map(int, input().split())
    vertices = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        vertices[a].append((b, c))
        vertices[b].append((a, c))
​
    checked = [0] * (v + 1)
    q = []
    answer = 0
    heapq.heappush(q, (0, 1))
    while q:
        c, v = heapq.heappop(q)
        if checked[v]:
            continue
​
        checked[v] = 1
        answer += c
        for next_v, cost in vertices[v]:
            if not checked[next_v]:
                heapq.heappush(q, (cost, next_v))
​
    print(answer)
    return
​
solution()
​