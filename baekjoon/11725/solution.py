// [문제 링크]: https://www.acmicpc.net/problem/11725

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict, deque
​
​
def solution():
    n = int(input())
    graph = defaultdict(list)
​
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
​
    def dfs(node):
        checked[node] = 1
​
        for next_node in graph[node]:
            if not checked[next_node]:
                parent[next_node] = node
                dfs(next_node)
​
        return
​
    def bfs():
        q = deque([1])
        while q:
            for _ in range(len(q)):
                root = q.popleft()
                checked[root] = 1
                for node in graph[root]:
                    if not checked[node]:
                        checked[node] = 1
                        parent[node] = root
                        q.append(node)
​
        return
​
    checked = [0] * (n + 1)
    parent = [0] * (n + 1)
    # dfs(1)
    bfs()
    print(*parent[2:], sep='\n')
​
    return
​
​
solution()
​