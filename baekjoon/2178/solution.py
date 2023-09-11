// [문제 링크]: https://www.acmicpc.net/problem/2178

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    answer = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = deque([[0, 0]])
    answer[0][0] = 1
    visited[0][0] = 1
​
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            for d in range(4):
                nr = r + dir[d][0]
                nc = c + dir[d][1]
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == '1' and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    answer[nr][nc] = answer[r][c] + 1
                    q.append([nr, nc])
​
    print(answer[n - 1][m - 1])
    return
​
solution()