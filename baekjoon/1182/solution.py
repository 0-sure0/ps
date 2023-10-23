// [문제 링크]: https://www.acmicpc.net/problem/1182

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, S = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
​
    def dfs(i, t):
        nonlocal ans
        if i >= len(l):
            return
​
        if t == S:
            ans += 1
​
        for j in range(i + 1, len(l)):
            dfs(j, t + l[j])
​
        return
​
    for i in range(len(l)):
        dfs(i, l[i])
​
    print(ans)
    return
​
solution()
​