// [문제 링크]: https://www.acmicpc.net/problem/1753

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import heapq
​
​
def solution():
    INF = 10 ** 9
    V, E = map(int, input().split())
    k = int(input())
    graph = defaultdict(list)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
​
    distance = [INF] * (V + 1)
    distance[k] = 0
    q = []
    heapq.heappush(q, (0, k))
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
​
        for next_node, w in graph[cur]:
            cost = dist + w
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    for i in range(1, V + 1):
        print("INF" if distance[i] == INF else distance[i])
    return
​
​
solution()
​