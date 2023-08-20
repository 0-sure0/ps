// [문제 링크]: https://www.acmicpc.net/problem/15486

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    work = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n + 1)
    cur_max = 0
    for i, (t, p) in enumerate(work):
        cur_max = max(cur_max, dp[i])
        if i + t <= n:
            dp[i + t] = max(dp[i + t], cur_max + p)
​
    print(max(dp))
    return
​
solution()
​