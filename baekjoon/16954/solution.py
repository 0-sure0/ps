// [문제 링크]: https://www.acmicpc.net/problem/16954

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque, defaultdict
​
​
def solution():
    wall = []
    for i in range(8):
        tmp = list(input().rstrip())
        for j in range(8):
            if tmp[j] == '#':
                wall.append((i, j))
​
    q = deque([(7, 0)])
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1), (0, 0)]
    visited = defaultdict(int)
​
    def move_wall():
        nonlocal wall
        wall = list(filter(lambda x: x[0] < 8, map(lambda x: (x[0] + 1, x[1]), wall)))
        return
​
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if (r, c) in wall:
                continue
​
            if r == 0:
                print(1)
                return
​
            for d in range(9):
                nr = r + dir[d][0]
                nc = c + dir[d][1]
                if 0 <= nr < 8 and 0 <= nc < 8 and not visited[(nr, nc)] and (nr, nc) not in wall:
                    q.append((nr, nc))
                    visited[(nr, nc)] = 1
        move_wall()
        if wall:
            visited.clear()
​
    print(0)
    return
​
solution()