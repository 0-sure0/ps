// [문제 링크]: https://www.acmicpc.net/problem/2422

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from math import factorial
from collections import deque
​
​
def solution():
    N, M = map(int, input().split())
    answer = factorial(N) // (factorial(N - 3) * factorial(3))
    ban = [list(map(int, input().split())) for _ in range(M)]
​
    def bfs(l):
        q = deque([l])
​
        while q:
            l = q.popleft()
            if len(l) == 3:
                banned.add(tuple(sorted(l)))
                continue
​
            for i in range(1, N + 1):
                if i not in l:
                    q.append(l + [i])
​
        return
​
    banned = set()
    for b in ban:
        bfs(b)
​
    print(answer - len(list(banned)))
    return
​
solution()