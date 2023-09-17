// [문제 링크]: https://www.acmicpc.net/problem/16932

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
​
    def bfs(r, c):
        q = deque([(r, c)])
        cnt = 1
        visited[r][c] = g_idx
​
        while q:
            r, c = q.popleft()
            for d in range(4):
                nr = r + dir[d][0]
                nc = c + dir[d][1]
​
                if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = g_idx
                    q.append((nr, nc))
                    cnt += 1
​
        return cnt
​
    visited = [[0] * M for _ in range(N)]
    group = dict()
    g_idx = 1
    for r in range(N):
        for c in range(M):
            if not visited[r][c] and board[r][c] == 1:
                cnt = bfs(r, c)
                group[g_idx] = cnt
                g_idx += 1
​
    answer = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                check_group = set()
                for d in range(4):
                    nr = r + dir[d][0]
                    nc = c + dir[d][1]
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 1 and visited[nr][nc] not in check_group:
                        check_group.add(visited[nr][nc])
                t = 1
                for g in check_group:
                    t += group[g]
                answer = max(answer, t)
​
    print(answer)
    return
​
solution()