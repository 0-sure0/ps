// [문제 링크]: https://www.acmicpc.net/problem/1967

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
​
def solution():
    N = int(input())
    graph = defaultdict(list)
    for _ in range(N - 1):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
​
    def dfs(node, t):
        nonlocal goal, answer
​
        visited[node] = 1
​
        for n, w in graph[node]:
            if not visited[n]:
                dfs(n, t + w)
​
        if answer < t:
            goal = node
            answer = t
        return
​
    visited = defaultdict(int)
    answer = 0
    goal = 0
    dfs(1, 0)
    visited.clear()
    answer = 0
    dfs(goal, 0)
​
    print(answer)
    return
​
solution()