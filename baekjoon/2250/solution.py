// [문제 링크]: https://www.acmicpc.net/problem/2250

import sys
#sys.stdin = open("test.txt", "r")
input = sys.stdin.readline
from collections import defaultdict
​
def solution():
    def dfs(node, level):
        nonlocal column
​
        if tree[node] == [-1, -1]:
            levels[level].append(column)
            column += 1
            return
​
        l, r = tree[node]
        if l != -1:
            dfs(l, level + 1)
        levels[level].append(column)
        column += 1
        if r != -1:
            dfs(r, level + 1)
​
        return
​
    levels = defaultdict(list)
    column = 1
    dfs(root, 1)
​
    ans = sorted([(level, max(levels[level]) - min(levels[level]) + 1) for level in levels], key=lambda x: (x[1], -x[0]), reverse=True)
    print(*ans[0])
    return
​
​
N = int(input())
tree = defaultdict(list)
nodes = defaultdict(int)
for _ in range(N):
    node, l, r = map(int, input().split())
    nodes[l] += 1
    nodes[r] += 1
    tree[node].extend([l, r])
root = 0
for i in range(1, N+1):
    if nodes[i] == 0:
        root = i
        break
solution()