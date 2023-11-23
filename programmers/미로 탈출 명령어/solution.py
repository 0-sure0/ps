// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/150365

import sys
sys.setrecursionlimit(5000)


def solution(n, m, x, y, r, c, k):
    dir = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0), }
    answer = "z"

    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    def dfs(x, y, s, cnt):
        nonlocal answer

        if k < cnt + abs(x - r) + abs(y - c):
            return

        if (x, y) == (r, c) and cnt == k:
            answer = s
            return

        for d in dir:
            dx, dy = dir[d]
            nx = x + dx
            ny = y + dy

            if 1 <= nx <= n and 1 <= ny <= m and s < answer:
                dfs(nx, ny, s + d, cnt + 1)

        return

    dfs(x, y, "", 0)
    return answer
