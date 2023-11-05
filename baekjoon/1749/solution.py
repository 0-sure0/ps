// [문제 링크]: https://www.acmicpc.net/problem/1749

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
N, M = map(int, input().split())
board = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
​
for r in range(1, N + 1):
    for c in range(1, M + 1):
        board[r][c] = board[r][c] + board[r - 1][c] + board[r][c - 1] - board[r - 1][c - 1]
​
ans = -sys.maxsize
for r1 in range(1, N + 1):
    for c1 in range(1, M + 1):
        for r2 in range(r1, N + 1):
            for c2 in range(c1, M + 1):
                ans = max(ans, board[r2][c2] - board[r2][c1 - 1] - board[r1 - 1][c2] + board[r1 - 1][c1 - 1])
print(ans)
​