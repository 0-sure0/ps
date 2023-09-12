// [문제 링크]: https://www.acmicpc.net/problem/13023

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def solution():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
​
    def dfs(node, depth):
        visited[node] = 1
        if depth == 5:
            return 1
​
        for next_node in graph[node]:
            if not visited[next_node]:
                if dfs(next_node, depth + 1):
                    return 1
                visited[next_node] = 0
​
        return 0
​
    for i in range(n):
        visited = [0] * n
        if dfs(i, 1):
            print(1)
            return
​
    print(0)
    return
​
solution()