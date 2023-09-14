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
    ice = deque()
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            if tmp[j] > 0:
                ice.append((i, j))
        board.append(tmp)
​
    def bfs(r, c):
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited[r][c] = 1
        q = deque([(r, c)])
        to_del = []
        while q:
            for _ in range(len(q)):
                cnt = 0
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dir[d][0]
                    nc = c + dir[d][1]
                    if 0 <= nr < N and 0 <= nc < M:
                        if board[nr][nc] == 0:
                            cnt += 1
                        else:
                            if not visited[nr][nc]:
                                visited[nr][nc] = 1
                                q.append((nr, nc))
                if cnt:
                    if cnt == 4:
                        return 1
                    to_del.append((r, c, cnt))
​
        for r, c, cnt in to_del:
            board[r][c] = max(0, board[r][c] - cnt)
​
        return 1
​
    answer = 0
    while ice:
        group = 0
        visited = [[0] * M for _ in range(N)]
        for r, c in ice:
            if not visited[r][c]:
                group += bfs(r, c)
        if group > 1:
            print(answer)
            return
​
        for _ in range(len(ice)):
            r, c = ice[0]
            if board[r][c] == 0:
                ice.popleft()
            else:
                ice.rotate(-1)
​
        answer += 1
​
    print(0)
    return
​
solution()