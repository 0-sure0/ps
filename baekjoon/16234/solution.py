// [문제 링크]: https://www.acmicpc.net/problem/16234

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    n, L, R = map(int, input().split())
    people = [list(map(int, input().split())) for _ in range(n)]
​
    def check(r, c):
        visited[r][c] = 1
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        t = [(r, c)]
        q = deque([[r, c]])
        s = people[r][c]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dir[d][0]
                    nc = c + dir[d][1]
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and L <= abs(people[r][c] - people[nr][nc]) <= R:
                        visited[nr][nc] = 1
                        q.append([nr, nc])
                        s += people[nr][nc]
                        t.append((nr, nc))
​
        if len(t) > 1:
            t.append(s)
        else:
            t = []
​
        return t
​
    answer = 0
    while True:
        visited = [[0] * n for _ in range(n)]
        tmp = []
        for r in range(n):
            for c in range(n):
                if not visited[r][c]:
                    t = check(r, c)
                    if t:
                        tmp.append(t)
​
        if not tmp:
            break
​
        for t in tmp:
            s = t[-1]
            for r, c in t[:-1]:
                people[r][c] = s // (len(t) - 1)
        answer += 1
​
    print(answer)
    return
​
solution()