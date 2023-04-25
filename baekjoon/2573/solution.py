// [문제 링크]: https://www.acmicpc.net/problem/2573

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    N, M = map(int, input().split())
    board = []
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ice = []
    answer = 0
    for r in range(N):
        t = list(map(int, input().split()))
        for c in range(M):
            if t[c] != 0:
                ice.append((r, c))
        board.append(t)
​
    def bfs(r, c):
        q = deque([(r, c)])
        checked[r][c] = 1
        sea_list = []
​
        while q:
            r, c = q.popleft()
            sea = 0
            for d in range(4):
                nr = r + dir[d][0]
                nc = c + dir[d][1]
                if 0 <= nr < N and 0 <= nc < M:
                    if not board[nr][nc]:
                        sea += 1
                    elif board[nr][nc] and not checked[nr][nc]:
                        q.append((nr, nc))
                        checked[nr][nc] = 1
            if sea > 0:
                sea_list.append((r, c, sea))
​
        for r, c, sea in sea_list:
            board[r][c] = max(0, board[r][c] - sea)
​
        return 1
​
    while ice:
        checked = [[0] * M for _ in range(N)]
        deleted = set()
        group = 0
        for r, c in ice:
            if board[r][c] and not checked[r][c]:
                group += bfs(r, c)
            if board[r][c] == 0:
                deleted.add((r, c))
​
        if group > 1:
            print(answer)
            return
​
        ice = list(set(ice) - deleted)
        answer += 1
​
    print(0)
    return
​
solution()
​
​