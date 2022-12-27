// [문제 링크]: https://www.acmicpc.net/problem/2407

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, M = map(int, input().split())
    dp = [0] * 101
    dp[1] = 1
​
    for i in range(2, N+1):
        dp[i] = dp[i-1] * i
​
    print(dp[N] // (dp[M] * dp[N-M]))
​
    return
​
solution()
​