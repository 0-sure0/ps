// [문제 링크]: https://www.acmicpc.net/problem/17836

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
def solution():
    N, M, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
​
    def bfs():
        nonlocal ans
​
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        checked = [[0] * M for _ in range(N)]
        q = deque([(0, 0)])
        cnt = 0
        checked[0][0] = 1
        while q and cnt < T:
            cnt += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dir[d][0]
                    nc = c + dir[d][1]
                    if 0 <= nr < N and 0 <= nc < M and not checked[nr][nc] and board[nr][nc] != 1:
                        if (nr, nc) == (N - 1, M - 1):
                            ans = min(ans, cnt)
                            continue
                        if board[nr][nc] == 0:
                            q.append((nr, nc))
                            checked[nr][nc] = 1
                        elif board[nr][nc] == 2:
                            if cnt + (N - 1 - nr) + (M - 1 - nc) <= T:
                                ans = min(ans, cnt + (N - 1 - nr) + (M - 1 - nc))
        return
​
    ans = sys.maxsize
    bfs()
    print("Fail" if ans == sys.maxsize else ans)
    return
​
​
solution()
​