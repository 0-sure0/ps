// [문제 링크]: https://www.acmicpc.net/problem/16973

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    N, M = map(int, input().split())
    board = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    H, W, sr, sc, fr, fc = map(int, input().split())
    wall = []
​
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if board[r][c] == 1:
                wall.append((r, c))
​
    def check_wall(r, c):
        for wr, wc in wall:
            if r <= wr < r + H and c <= wc < c + W:
                return 1
        return 0
​
    q = deque([[sr, sc]])
    visited = [[0] * (M + 1) for _ in range(N + 1)]
    visited[sr][sc] = 1
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cnt = 0
    answer = sys.maxsize
    while q:
        cnt += 1
        for _ in range(len(q)):
            cr, cc = q.popleft()
            for d in range(4):
                nr = cr + dir[d][0]
                nc = cc + dir[d][1]
                if (nr, nc) == (fr, fc):
                    answer = min(answer, cnt)
                    continue
​
                if 1 <= nr < N + 1 and 1 <= nc < M + 1 and 1 <= nr < N + 2 - H and 1 <= nc < M + 2 - W and not visited[nr][nc] and not check_wall(nr, nc):
                    q.append((nr, nc))
                    visited[nr][nc] = 1
​
    print(answer if answer != sys.maxsize else -1)
    return
​
solution()