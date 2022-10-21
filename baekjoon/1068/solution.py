// [문제 링크]: https://www.acmicpc.net/problem/1068

import sys
# sys.stdin = open("./test.txt", "r")
input = sys.stdin.readline
from collections import defaultdict
​
​
def solution():
    def dfs(node):
        checked[node] = 1
​
        if not tree[node]:
            del tree[node]
            return
​
        for n in tree[node]:
            if not checked[n]:
                dfs(n)
​
        del tree[node]
​
        return
​
    checked = defaultdict(int)
    dfs(target)
​
    leaf = 0
    for t in tree:
        if not tree[t]:
            leaf += 1
    if l[target] != -1 and len(tree[l[target]]) == 1:
        leaf += 1
    print(leaf)
    return
​
​
N = int(input())
l = list(map(int, input().split()))
tree = {i: [] for i in range(N)}
target = int(input())
for i in range(N):
    if l[i] == -1:
        continue
    tree[l[i]].append(i)
​
solution()
​