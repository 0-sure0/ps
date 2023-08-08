// [문제 링크]: https://www.acmicpc.net/problem/9465

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    T = int(input())
    for _ in range(T):
        n = int(input())
        l = [list(map(int, input().split())) for _ in range(2)]
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = l[0][0]
        dp[1][0] = l[1][0]
​
        for c in range(1, n):
            for r in range(2):
                dp[r][c] = max(l[r][c] + dp[(r + 1) % 2][c - 1], dp[r][c - 1])
​
        print(max(dp[0][-1], dp[1][-1]))
​
    return
​
solution()
​