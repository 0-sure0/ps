// [문제 링크]: https://www.acmicpc.net/problem/17836

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    n, m, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = 10001
    time = 0
​
    q = deque([[0, 0]])
    visited = [[0] * m for _ in range(n)]
    while time < T:
        time += 1
        for _ in range(len(q)):
            r, c = q.popleft()
            for d in range(4):
                nr = r + dir[d][0]
                nc = c + dir[d][1]
​
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and board[nr][nc] != 1:
                    if (nr, nc) == (n - 1, m - 1):
                        answer = min(answer, time)
                        continue
                    if board[nr][nc] == 2:
                        if time + (n - 1 - nr) + (m - 1 - nc) <= T:
                            answer = min(answer, time + (n - 1 - nr) + (m - 1 - nc))
                    else:
                        q.append((nr, nc))
                        visited[nr][nc] = 1
​
    print(answer if answer != 10001 else "Fail")
    return
​
solution()