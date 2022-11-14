// [문제 링크]: https://www.acmicpc.net/problem/3584

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**9)
​
​
def solution():
    def dfs(node):
        nonlocal found, ans
​
        if node in parents:
            ans = node
            found = True
            return found
​
        parents.add(node)
        for n in tree[node]:
            if n in parents:
                found = True
                ans = n
                return found
            if dfs(n):
                return found
​
​
        return found
​
    parents = set()
    found = False
    ans = 0
​
    dfs(t1)
    dfs(t2)
​
    print(ans)
​
    return
​
​
T = int(input())
for _ in range(T):
    N = int(input())
    tree = defaultdict(list)
    for _ in range(N-1):
        A, B = map(int, input().split())
        tree[B].append(A)
    t1, t2 = map(int, input().split())
    solution()