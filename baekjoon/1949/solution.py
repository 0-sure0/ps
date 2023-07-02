// [문제 링크]: https://www.acmicpc.net/problem/1949

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10 ** 8)
​
def solution():
    n = int(input())
    people = [0] + list(map(int, input().split()))
    dp = [[0, people[i]] for i in range(n + 1)]
​
    graph = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
​
    def dfs(cur):
        checked[cur] = 1
        for node in graph[cur]:
            if not checked[node]:
                dfs(node)
                dp[cur][1] += dp[node][0]
                dp[cur][0] += max(dp[node][0], dp[node][1])
​
        return
​
    checked = [0] * (n + 1)
    dfs(1)
    print(max(dp[1]))
    return
​
​
solution()
​