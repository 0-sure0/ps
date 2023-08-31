// [문제 링크]: https://www.acmicpc.net/problem/2056

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    n = int(input())
    answer = 0
​
    t = [0] * (n + 1)
    t_done = [0] * (n + 1)
    con = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
​
    for i in range(1, n + 1):
        time, _, *l = map(int, input().split())
        t[i] = time
​
        for p in l:
            con[p].append(i)
            indeg[i] += 1
​
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)
            t_done[i] = t[i]
​
    while q:
        x = q.popleft()
        for y in con[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
            t_done[y] = max(t_done[y], t_done[x] + t[y])
​
    print(max(t_done))
    return
​
solution()