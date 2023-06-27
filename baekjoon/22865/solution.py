// [문제 링크]: https://www.acmicpc.net/problem/22865

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import heapq
​
​
def solution():
    n = int(input())
    a, b, c = map(int, input().split())
    graph = defaultdict(list)
    m = int(input())
    for _ in range(m):
        d, e, l = map(int, input().split())
        graph[d].append((e, l))
        graph[e].append((d, l))
​
    distance = {a: [sys.maxsize] * (n + 1), b: [sys.maxsize] * (n + 1), c: [sys.maxsize] * (n + 1)}
​
    def dist(node):
        q = []
        heapq.heappush(q, (0, node))
        while q:
            cur_cost, cur_node = heapq.heappop(q)
            if distance[node][cur_node] < cur_cost:
                continue
​
            for next_node, next_cost in graph[cur_node]:
                cost = cur_cost + next_cost
                if cost < distance[node][next_node]:
                    distance[node][next_node] = cost
                    heapq.heappush(q, (cost, next_node))
​
        return
​
    distance[a][a] = 0
    dist(a)
    distance[b][b] = 0
    dist(b)
    distance[c][c] = 0
    dist(c)
​
    answer = []
    for i in range(1, n + 1):
        if i == a or i == b or i == c:
            continue
        heapq.heappush(answer, (-min(distance[a][i], distance[b][i], distance[c][i]), i))
​
    print(answer[0][1])
    return
​
​
solution()
​