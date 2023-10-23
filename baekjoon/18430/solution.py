// [문제 링크]: https://www.acmicpc.net/problem/18430

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    shape = {0: [0, -1, 1, 0], 1: [-1, 0, 0, -1], 2: [-1, 0, 0, 1], 3: [0, 1, 1, 0]}
    checked = [[0] * m for _ in range(n)]
    answer = 0
​
    def dfs(i, j, s):
        nonlocal answer
​
        if j == m:
            i += 1
            j = 0
        if i == n:
            answer = max(answer, s)
            return
​
        if not checked[i][j]:
            for k in range(4):
                a, b, c, d = shape[k]
                x, y, xx, yy = i + a, j + b, i + c, j + d
                if 0 <= x < n and 0 <= xx < n and 0 <= y < m and 0 <= yy < m and not checked[x][y] and not checked[xx][yy]:
                    checked[x][y] = checked[xx][yy] = checked[i][j] = 1
                    dfs(i, j + 1, s + board[i][j] * 2 + board[x][y] + board[xx][yy])
                    checked[x][y] = checked[xx][yy] = checked[i][j] = 0
        dfs(i, j + 1, s)
        return
​
    dfs(0, 0, 0)
    print(answer)
    return
​
solution()
​