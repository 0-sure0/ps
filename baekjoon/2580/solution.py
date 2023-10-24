// [문제 링크]: https://www.acmicpc.net/problem/2580

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
board = []
row = [[0] * 10 for _ in range(9)]
col = [[0] * 10 for _ in range(9)]
board33 = [[0] * 10 for _ in range(9)]
zeros = []
​
for r in range(9):
    t = list(map(int, input().split()))
    for c in range(9):
        if t[c] == 0:
            zeros.append((r, c))
        else:
            row[r][t[c]] = 1
            col[c][t[c]] = 1
            board33[r // 3 * 3 + c // 3][t[c]] = 1
    board.append(t)
​
def dfs(idx):
    if idx >= len(zeros):
        return True
​
    r, c = zeros[idx]
    for num in range(1, 10):
        if row[r][num] or col[c][num] or board33[r // 3 * 3  + c // 3][num]:
            continue
​
        row[r][num] = 1
        col[c][num] = 1
        board33[r // 3 * 3 + c // 3][num] = 1
        board[r][c] = num
        if dfs(idx + 1):
            return True
        row[r][num] = 0
        col[c][num] = 0
        board33[r // 3 * 3 + c // 3][num] = 0
        board[r][c] = 0
​
    return False
​
dfs(0)
for r in range(9):
    print(*board[r])