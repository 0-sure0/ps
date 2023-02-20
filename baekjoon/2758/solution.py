// [문제 링크]: https://www.acmicpc.net/problem/2758

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    T = int(input())
    dp = [[1] * 2001 if i == 0 else [0] * 2001 for i in range(11)]
    for i in range(1, 11):
        for j in range(1, 2001):
            dp[i][j] = dp[i][j-1] + dp[i - 1][j // 2]
​
    for _ in range(T):
        ans = set()
        N, M = map(int, input().split())
        print(dp[N][M])
​
    return
​
solution()