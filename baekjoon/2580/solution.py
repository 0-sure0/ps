// [문제 링크]: https://www.acmicpc.net/problem/2580

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    board = []
    board99 = [[0] * 10 for _ in range(10)]
    row = [[0] * 10 for _ in range(10)]
    column = [[0] * 10 for _ in range(10)]
    zeros = []
    for r in range(9):
        t = list(map(int, input().split()))
        for c in range(9):
            if t[c] == 0:
                zeros.append((r, c))
            else:
                row[r][t[c]] = 1
                column[c][t[c]] = 1
                board99[r // 3 * 3 + c // 3][t[c]] = 1
        board.append(t)
​
    def dfs(idx):
        if idx >= len(zeros):
            return True
​
        r, c = zeros[idx]
        for k in range(1, 10):
            if board99[r // 3 * 3 + c // 3][k] or row[r][k] or column[c][k]:
                continue
​
            board99[r // 3 * 3 + c // 3][k] = row[r][k] = column[c][k] = 1
            board[r][c] = k
            if dfs(idx + 1):
                return True
            board99[r // 3 * 3 + c // 3][k] = row[r][k] = column[c][k] = 0
            board[r][c] = 0
​
        return False
​
    dfs(0)
    for r in range(9):
        print(*board[r])
    return
​
solution()