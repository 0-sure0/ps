// [문제 링크]: https://www.acmicpc.net/problem/2293

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    dp = [1 if i == 0 else 0 for i in range(K + 1)]
​
    for coin in coins:
        for i in range(1, K + 1):
            if i < coin:
                continue
            dp[i] += dp[i - coin]
​
    print(dp[K])
    return
​
​
solution()
​