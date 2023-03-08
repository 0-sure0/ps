// [문제 링크]: https://www.acmicpc.net/problem/17485

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from math import inf
​
def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[0, 0, 0] if i != 0 else [board[i][j]] * 3 for j in range(M)] for i in range(N)]
​
    for r in range(1, N):
        for c in range(M):
            for t in range(3):
                if t == 0:
                    if c == 0:
                        dp[r][c][t] = inf
                    else:
                        dp[r][c][t] = board[r][c] + min(dp[r - 1][c - 1][1], dp[r - 1][c - 1][2])
                elif t == 1:
                    dp[r][c][t] = board[r][c] + min(dp[r - 1][c][0], dp[r - 1][c][2])
                else:
                    if c == M - 1:
                        dp[r][c][t] = inf
                    else:
                        dp[r][c][t] = board[r][c] + min(dp[r - 1][c + 1][0], dp[r - 1][c + 1][1])
                        
    ans = inf
    for c in range(M):
        ans = min(ans, min(dp[N - 1][c]))
    print(ans)
    return
​
​
solution()
​