// [문제 링크]: https://www.acmicpc.net/problem/1238

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import heapq
​
​
def solution():
    n, m, x = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a].append((t, b))
​
    def dijkstra(node):
        distance = [sys.maxsize] * (n + 1)
        distance[node] = 0
        q = []
        heapq.heappush(q, (0, node))
​
        while q:
            cur_cost, cur_node = heapq.heappop(q)
            if distance[cur_node] < cur_cost:
                continue
​
            for next_cost, next_node in graph[cur_node]:
                cost = cur_cost + next_cost
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
​
        for i in range(n + 1):
            if distance[i] == sys.maxsize:
                distance[i] = -1
        return distance
​
    dist = [[0] * (n + 1)] + [dijkstra(i) for i in range(1, n + 1)]
    answer = sorted([(dist[i][x] + dist[x][i], i) for i in range(1, n + 1)], key=lambda x: x[0], reverse=True)
    print(answer[0][0])
    return
​
​
solution()
​