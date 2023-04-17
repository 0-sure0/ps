// [문제 링크]: https://www.acmicpc.net/problem/2606

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict, deque
​
​
def solution():
    n = int(input())
    m = int(input())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
​
    def bfs():
        checked = [0] * (n + 1)
        q = deque([1])
​
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not checked[node]:
                    checked[node] = 1
                    for next_node in graph[node]:
                        q.append(next_node)
​
        return checked.count(1) - 1
​
    infected = bfs()
    print(infected)
    return
​
solution()
​