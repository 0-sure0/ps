// [문제 링크]: https://www.acmicpc.net/problem/20543

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
N, M = map(int, input().split())
mid = M // 2
board = [list(map(lambda x: -1 * x, map(int, input().split()))) for _ in range(N)]
bomb = [[0] * N for _ in range(N)]
​
for r in range(mid, N - mid):
    for c in range(mid, N - mid):
        bomb[r][c] = board[r - mid][c - mid]
​
        if r - mid - 1 >= 0:
            bomb[r][c] -= board[r - mid - 1][c - mid]
        if c - mid - 1 >= 0:
            bomb[r][c] -= board[r - mid][c - mid - 1]
        if r - mid - 1 >= 0 and c - mid - 1 >= 0:
            bomb[r][c] += board[r - mid - 1][c - mid - 1]
​
        if r - M >= 0:
            bomb[r][c] += bomb[r - M][c]
        if c - M >= 0:
            bomb[r][c] += bomb[r][c - M]
        if r - M >= 0 and c - M >= 0:
            bomb[r][c] -= bomb[r - M][c - M]
​
​
for r in range(N):
    print(*bomb[r])
​
​