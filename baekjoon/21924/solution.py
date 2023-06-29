// [문제 링크]: https://www.acmicpc.net/problem/21924

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import heapq
​
​
def solution():
    n, m = map(int, input().split())
    uf = [-1] * (n + 1)
    edges = []
    total = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        heapq.heappush(edges, (c, a, b))
        total += c
​
    def find(x):
        if uf[x] < 0:
            return x
        uf[x] = find(uf[x])
        return uf[x]
​
    def union(a, b):
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
    print(total - answer if uf[1:].count(-1) <= 1 else -1)
    return
​
solution()
​