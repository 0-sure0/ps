// [문제 링크]: https://www.acmicpc.net/problem/1915

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, m = map(int, input().split())
    board = [[0] * m] + [list(map(int, list(input().rstrip()))) for _ in range(n)]
​
    for r in range(1, n + 1):
        for c in range(1, m):
            if board[r][c] and board[r - 1][c - 1] and board[r - 1][c] and board[r][c - 1]:
                board[r][c] = min(board[r - 1][c - 1], board[r - 1][c], board[r][c - 1]) + 1
​
    answer = 0
    for r in range(1, n + 1):
        answer = max(answer, max(board[r]))
    print(answer ** 2)
    return
​
​
solution()
​