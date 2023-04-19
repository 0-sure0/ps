// [문제 링크]: https://www.acmicpc.net/problem/7576

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque, defaultdict
​
​
def solution():
    M, N = map(int, input().split())
    tomatoes = []
    checked = 0
    q = deque()
    ans = 0
​
    for r in range(N):
        t = list(map(int, input().split()))
        for c in range(M):
            if t[c] == 1:
                checked += 1
                q.append((r, c))
            elif t[c] == -1:
                checked += 1
        tomatoes.append(t)
​
    while q and checked != N * M:
        ans += 1
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
​
        for _ in range(len(q)):
            r, c = q.popleft()
​
            for d in range(4):
                nr = r + dir[d][0]
                nc = c + dir[d][1]
                if 0 <= nr < N and 0 <= nc < M and tomatoes[nr][nc] == 0:
                    tomatoes[nr][nc] = 1
                    checked += 1
                    q.append((nr, nc))
​
    print(ans if checked == M * N else -1)
    return
​
​
solution()
​