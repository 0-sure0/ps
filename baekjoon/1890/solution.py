// [문제 링크]: https://www.acmicpc.net/problem/1890

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
​
    for r in range(N):
        for c in range(N):
            if r == N - 1 and c == N - 1:
                print(dp[r][c])
                continue
            move = board[r][c]
            if c + move < N:
                dp[r][c + move] += dp[r][c]
​
            if r + move < N:
                dp[r + move][c] += dp[r][c]
​
    return
​
solution()
​