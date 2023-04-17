// [문제 링크]: https://www.acmicpc.net/problem/16918

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    R, C, N = map(int, input().split())
    board = []
    bomb = [[-1] * C for _ in range(R)]
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
​
    for r in range(R):
        t = list(input().rstrip())
        for c in range(C):
            if t[c] == 'O':
                bomb[r][c] = 0
        board.append(t)
​
    for i in range(2, N + 1):
        if i % 2 == 0:
            for r in range(R):
                for c in range(C):
                    if board[r][c] == '.':
                        board[r][c] = 'O'
                        bomb[r][c] = i
        else:
            for r in range(R):
                for c in range(C):
                    if bomb[r][c] == i - 3:
                        bomb[r][c] = -1
                        board[r][c] = '.'
​
                        for d in range(4):
                            nr = r + dir[d][0]
                            nc = c + dir[d][1]
                            if 0 <= nr < R and 0 <= nc < C and bomb[nr][nc] != i - 3:
                                bomb[nr][nc] = -1
                                board[nr][nc] = '.'
​
    for r in range(R):
        print(''.join(board[r]))
​
    return
​
solution()
​