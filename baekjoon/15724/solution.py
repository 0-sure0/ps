// [문제 링크]: https://www.acmicpc.net/problem/15724

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, M = map(int, input().split())
    board = [[0] * (M + 1) for _ in range(N + 1)]
    for r in range(1, N + 1):
        t = list(map(int, input().split()))
        for c in range(M):
            board[r][c + 1] = t[c]
​
    for r in range(1, N + 1):
        for c in range(M + 1):
            if c == 0:
                board[r][c] += board[r-1][c]
            else:
                board[r][c] += board[r-1][c] + board[r][c-1] - board[r-1][c-1]
​
​
    K = int(input())
    target = [list(map(int, input().split())) for _ in range(K)]
​
    for x1, y1, x2, y2 in target:
        print(board[x2][y2] - board[x2][y1 - 1] - board[x1 - 1][y2] + board[x1-1][y1-1])
​
    return
​
​
solution()
​