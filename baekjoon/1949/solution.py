// [문제 링크]: https://www.acmicpc.net/problem/1949

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10 ** 8)
​
​
N = int(input())
tree = defaultdict(list)
village = [0] + list(map(int, input().split()))
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
​
​
def dfs(cur):
    checked[cur] = 1
    for node in tree[cur]:
        if not checked[node]:
            dfs(node)
            dp[cur][1] += dp[node][0]
            dp[cur][0] += max(dp[node])
    return
​
​
checked = [0] * (N + 1)
dp = [[0, village[i]] for i in range(N + 1)]
dfs(1)
print(max(dp[1]))
​