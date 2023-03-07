// [문제 링크]: https://www.acmicpc.net/problem/2225

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, K = map(int, input().split())
    dp = [[1 if i == 0 or j == 0 else 0 for j in range(N + 1)] for i in range(K)]
​
    for i in range(1, K):
        for j in range(1, N + 1):
            for t in range(j // 2 + 1):
                if t == j - t:
                    dp[i][j] += dp[i - 1][t]
                else:
                    dp[i][j] += dp[i - 1][t] + dp[i - 1][j - t]
    print(dp[K - 1][N] % 1000000000)
    return
​
​
solution()
​