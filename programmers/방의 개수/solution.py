// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/49190

from collections import defaultdict

def solution(arrows):
    answer = 0
    dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    r, c = 0, 0

    node = defaultdict(int)
    edge = defaultdict(int)

    for d in arrows:
        node[(r, c)] += 1
        for _ in range(2):
            nr = r + dir[d][0]
            nc = c + dir[d][1]

            if node[(nr, nc)] and not edge[(r, c, nr, nc)]:
                answer += 1
                edge[(r, c, nr, nc)] += 1
                edge[(nr, nc, r, c)] += 1
            else:
                edge[(r, c, nr, nc)] += 1
                edge[(nr, nc, r, c)] += 1
                node[(nr, nc)] = 1
            r, c = nr, nc

    return answer