// [문제 링크]: https://www.acmicpc.net/problem/1277

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict, deque
import heapq
import math
​
​
def dist(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
​
​
def solution():
    n, w = map(int, input().split())
    m = float(input().rstrip())
    coord = [0] * (n + 1)
    graph = defaultdict(list)
​
    for i in range(1, n + 1):
        x, y = map(int, input().split())
        coord[i] = (x, y)
​
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            d = dist(coord[i], coord[j])
            if d <= m:
                graph[i].append((j, d))
                graph[j].append((i, d))
​
    for _ in range(w):
        a, b = map(int, input().split())
        graph[a].append((b, 0))
        graph[b].append((a, 0))
​
    def dijkstra():
        distance = [10**9 for _ in range(n + 1)]
        distance[1] = 0
        q = []
        heapq.heappush(q, (0, 1))
​
        while q:
            cost, cur = heapq.heappop(q)
            if distance[cur] < cost:
                continue
​
            for next_node, weight in graph[cur]:
                if cost + weight < distance[next_node]:
                    distance[next_node] = cost + weight
                    heapq.heappush(q, (cost + weight, next_node))
​
        return int(distance[n] * 1000)
    
    print(dijkstra())
    return
​
​
solution()
​