// [문제 링크]: https://www.acmicpc.net/problem/1106

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    C, N = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(N)]
    dp = [sys.maxsize] * (C + 100)
    dp[0] = 0
​
    for c, p in l:
        for i in range(p, C + 100):
            dp[i] = min(dp[i-p] + c, dp[i])
​
    print(min(dp[C:]))
    return
​
solution()
​