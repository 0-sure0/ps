// [문제 링크]: https://www.acmicpc.net/problem/13023

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def solution():
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
​
    def dfs(root, depth):
        checked[root] = 1
​
        if depth == 5:
            return True
​
        for node in graph[root]:
            if not checked[node]:
                if dfs(node, depth + 1):
                    return True
        checked[root] = 0
        return False
​
    checked = [0] * N
    for i in range(N):
        if dfs(i, 1):
            print(1)
            return
​
    print(0)
    return
​
​
solution()
​