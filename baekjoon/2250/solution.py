// [문제 링크]: https://www.acmicpc.net/problem/2250

import sys
#sys.stdin = open("test.txt", "r")
input = sys.stdin.readline
from collections import defaultdict
​
def solution():
    def find_root():
        nonlocal root
        has_parent = set()
        for node in tree:
            for n in tree[node]:
                has_parent.add(n)
        root = list(set(tree.keys()) - has_parent)[0]
        return
​
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
    root = 0
    find_root()
    dfs(root, 1)
​
    ans = sorted([(level, max(levels[level]) - min(levels[level]) + 1) for level in levels], key=lambda x: (x[1], -x[0]), reverse=True)
    print(*ans[0])
    return
​
​
N = int(input())
tree = defaultdict(list)
for _ in range(N):
    node, l, r = map(int, input().split())
    tree[node].extend([l, r])
solution()