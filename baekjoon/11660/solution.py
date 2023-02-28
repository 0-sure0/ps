// [문제 링크]: https://www.acmicpc.net/problem/11660

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, M = map(int, input().split())
    board = [[0] * (N + 1)]
    for _ in range(N):
        board.append([0] + list(map(int, input().split())))
​
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            board[r][c] += board[r][c - 1] + board[r - 1][c] - board[r - 1][c - 1]
​
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        print(board[x2][y2] - board[x2][y1 - 1] - board[x1 - 1][y2] + board[x1 - 1][y1 - 1])
​
    return
​
solution()
​