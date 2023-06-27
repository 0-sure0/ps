// [문제 링크]: https://www.acmicpc.net/problem/1865

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import heapq
​
​
def solution():
    tc = int(input())
    INF = sys.maxsize
​
    #bellman ford
    def bf(node):
        distance = [INF] * (n + 1)
        distance[node] = 0
​
        for i in range(n):
            for edge in edges:
                cur, next_node, cost = edge
​
                if cost + distance[cur] < distance[next_node]:
                    distance[next_node] = cost + distance[cur]
​
                    if i == n - 1:
                        return True
        return False
​
    for _ in range(tc):
        edges = []
        n, m, w = map(int, input().split())
        for _ in range(m):
            s, e, t = map(int, input().split())
            edges.append((s, e, t))
            edges.append((e, s, t))
​
        for _ in range(w):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t))
​
        if bf(1):
            print('YES')
        else:
            print('NO')
    return
​
​
solution()
​