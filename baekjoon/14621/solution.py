// [문제 링크]: https://www.acmicpc.net/problem/14621

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import heapq
​
​
def solution():
    n, m = map(int, input().split())
    uf = [-1] * (n + 1)
    school = [0] + input().split()
    edges = []
    for _ in range(m):
        u, v, d = list(map(int, input().split()))
        heapq.heappush(edges, (d, u, v))
​
    def find(x):
        if uf[x] < 0:
            return x
        uf[x] = find(uf[x])
        return uf[x]
​
    def union(a, b):
        if school[a] == school[b]:
            return False
        a = find(a)
        b = find(b)
        if a == b:
            return False
        uf[b] = a
        return True
​
    answer = 0
    while edges:
        c, a, b = heapq.heappop(edges)
        if union(a, b):
            answer += c
​
    print(-1 if uf.count(-1) > 2 else answer)
    return
​
solution()
​