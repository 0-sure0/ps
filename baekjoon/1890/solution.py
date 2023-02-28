// [문제 링크]: https://www.acmicpc.net/problem/1890

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
​
def solution():
    N = int(input())
    dir = [(0, 1), (1, 0)]
    board = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
​
    for r in range(N):
        for c in range(N):
            if r == N - 1 and c == N - 1:
                break
            for i in range(2):
                nr = r + dir[i][0] * board[r][c]
                nc = c + dir[i][1] * board[r][c]
                if 0 <= nr < N and 0 <= nc < N:
                    dp[nr][nc] += dp[r][c]
    print(dp[N-1][N-1])
    return
​
solution()
​