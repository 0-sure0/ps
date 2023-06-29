// [문제 링크]: https://www.acmicpc.net/problem/1647

import heapq
import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, m = map(int, input().split())
    uf = [-1] * (n + 1)
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        heapq.heappush(edges, (c, a, b))
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
    max_c = 0
    while edges:
        c, a, b = heapq.heappop(edges)
        if union(a, b):
            answer += c
            max_c = max(c, max_c)
    print(answer - max_c)
    return
​
solution()
​