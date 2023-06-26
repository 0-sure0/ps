// [문제 링크]: https://www.acmicpc.net/problem/11404

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import heapq
​
​
def solution():
    n = int(input())
    m = int(input())
    bus = defaultdict(list)
    answer = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
​
    for _ in range(m):
        a, b, c = map(int, input().split())
        bus[a].append((c, b))
​
​
    def dijkstra(s):
        q = []
        heapq.heappush(q, (0, s))
​
        while q:
            cur_cost, cur_node = heapq.heappop(q)
            if answer[s][cur_node] < cur_cost:
                continue
​
            for next_cost, next_node in bus[cur_node]:
                cost = cur_cost + next_cost
                if cost < answer[s][next_node]:
                    answer[s][next_node] = cost
                    heapq.heappush(q, (cost, next_node))
​
        return
​
    for i in range(1, n + 1):
        answer[i][i] = 0
        dijkstra(i)
​
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            print(answer[r][c] if answer[r][c] != sys.maxsize else 0, end=' ')
        print()
    return
​
​
solution()
​