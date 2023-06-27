// [문제 링크]: https://www.acmicpc.net/problem/10159

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict, deque
​
​
def solution():
    n = int(input())
    m = int(input())
    weight = [[0] * (n + 1) for _ in range(n + 1)]
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
​
    def bfs(node):
        checked = [0] * (n + 1)
        q = deque([node])
        checked[node] = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for next_node in graph[cur]:
                    if not checked[next_node]:
                        weight[node][next_node] = 1
                        weight[next_node][node] = 1
                        weight[cur][next_node] = 1
                        weight[next_node][cur] = 1
                        q.append(next_node)
                        checked[next_node] = 1
        return
​
    for i in range(1, n + 1):
        if sum(weight[i]) != n:
            bfs(i)
            
    for i in range(1, n + 1):
        print(n - 1 - sum(weight[i]))
    return
​
​
solution()
​