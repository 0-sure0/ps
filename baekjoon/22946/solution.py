// [문제 링크]: https://www.acmicpc.net/problem/22946

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
import math
sys.setrecursionlimit(10 ** 9)
​
def solution():
    N = int(input())
    circles = [(i, list(map(int, input().split()))) for i in range(1, N + 1)]
    circles.sort(key=lambda x: x[1][2])
    graph = defaultdict(list)
    p = [0] * (N + 1)
    end_node = []
    for i in range(N):
        ai, (ax, ay, ar) = circles[i]
        for j in range(i + 1, N):
            bi, (bx, by, br) = circles[j]
            d = math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)
            if d < abs(br - ar):
                graph[ai].append(bi)
                graph[bi].append(ai)
                p[ai] = bi
                break
        if not p[ai]:
            graph[ai].append(0)
            graph[0].append(ai)
        if len(graph[ai]) == 1:
            end_node.append(ai)
​
    def dfs(node, depth):
        nonlocal answer
​
        visited[node] = 1
        for n in graph[node]:
            if not visited[n]:
                dfs(n, depth + 1)
        answer = max(answer, depth)
        return
​
    answer = 0
    for s in end_node:
        visited = [0] * (N + 1)
        dfs(s, 0)
​
    print(answer)
    return
​
solution()