// [문제 링크]: https://www.acmicpc.net/problem/16234

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque, defaultdict
​
​
def solution():
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ans = 0
​
    def bfs(r, c):
        nonlocal total
        q = deque([(r, c)])
        tmp = [(r, c)]
​
        while q:
            r, c = q.popleft()
            for d in range(4):
                nr = r + dir[d][0]
                nc = c + dir[d][1]
                if 0 <= nr < N and 0 <= nc < N and not checked[nr][nc] and L <= abs(board[r][c] - board[nr][nc]) <= R:
                    checked[nr][nc] = 1
                    q.append((nr, nc))
                    tmp.append((nr, nc))
                    total += board[nr][nc]
​
        return tmp
​
    while True:
        checked = [[0] * N for _ in range(N)]
        move = False
​
        for r in range(N):
            for c in range(N):
                if not checked[r][c]:
                    checked[r][c] = 1
                    total = board[r][c]
                    t = bfs(r, c)
                    if len(t) > 1:
                        move = True
                        for tr, tc in t:
                            board[tr][tc] = total // len(t)
​
        if not move:
            break
        ans += 1
​
    print(ans)
​
    return
​
​
solution()
​