// [문제 링크]: https://www.acmicpc.net/problem/1197

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import heapq
​
def solution():
    v, e = map(int, input().split())
    parent = [-1] * (v + 1)
    edge = []
    answer = 0
    for _ in range(e):
        a, b, c = map(int, input().split())
        heapq.heappush(edge, (c, a, b))
​
    def find(x):
        if parent[x] < 0:
            return x
        parent[x] = find(parent[x])
        return parent[x]
​
    def should_union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[b] = a
            return True
​
        return False
​
    while edge:
        weight, a, b = heapq.heappop(edge)
        if should_union(a, b):
            answer += weight
​
    print(answer)
    return
​
solution()
​