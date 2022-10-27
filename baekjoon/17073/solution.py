// [문제 링크]: https://www.acmicpc.net/problem/17073

import sys
# sys.stdin = open("./test.txt", "r")
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**6)
​
def solution():
    def dfs(node):
        nonlocal leaf
        checked[node] = 1
        cnt = 0
​
        for n in g[node]:
            if checked[n] == 0:
                dfs(n)
                cnt = 0
            else:
                cnt += 1
​
        if len(g[node]) == cnt:
            leaf += 1
​
        return
​
    checked = defaultdict(int)
    leaf = 0
    dfs(1)
​
    ans = W / leaf
​
    return ans
​
​
N, W = map(int, input().split())
g = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, input().split())
    g[v].append(u)
    g[u].append(v)
print(solution())