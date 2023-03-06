// [문제 링크]: https://www.acmicpc.net/problem/2294

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from math import inf
​
def solution():
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    dp = [inf] * (K + 1)
    dp[0] = 0
​
    for coin in coins:
        for i in range(coin, K + 1):
            dp[i] = min(dp[i - coin] + 1, dp[i])
​
    print(-1 if dp[K] == inf else dp[K])
    return
​
​
solution()
​