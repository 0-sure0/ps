// [문제 링크]: https://www.acmicpc.net/problem/20924

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**9)
​
​
def solution():
    def dfs(node, distance):
        nonlocal longest, giga_len, giga_checked
        checked[node] = 1
​
        l = len(tree[node]) - 1 if node != R else len(tree[node])
        if l >= 2 and not giga_checked:
            giga_len = distance
            giga_checked = True
​
        for n, d in tree[node]:
            if not checked[n]:
                if not giga_checked and l >= 2:
                    giga_len = distance + d
                    giga_checked = True
                dfs(n, distance + d)
​
        if len(tree[node]) - 1 == 0:
            longest = max(longest, distance)
            if not giga_checked:
                giga_len = distance
                giga_checked = True
        return
​
    giga_len = 0
    longest = 0
    giga_checked = False
    checked = defaultdict(list)
    dfs(R, 0)
    print(giga_len, longest - giga_len)
​
    return
​
​
N, R = map(int, input().split())
tree = defaultdict(list)
for _ in range(N-1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))
solution()
​