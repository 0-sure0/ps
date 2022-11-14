// [문제 링크]: https://www.acmicpc.net/problem/1967

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**9)
​
def solution():
    def dfs(node, d):
        nonlocal max_d, t
​
        checked[node] = 1
​
        for n, v in tree[node]:
            if not checked[n]:
                dfs(n, d + v)
​
        if d > max_d:
            max_d = d
            t = node
​
        return
​
    t = max_d = 0
    checked = defaultdict(int)
    dfs(1, 0)
    s = t
    t = max_d = 0
    checked.clear()
    dfs(s, 0)
    print(max_d)
    return
​
​
tree = defaultdict(list)
N = int(input())
for _ in range(N-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))
solution()
​