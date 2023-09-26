// [문제 링크]: https://www.acmicpc.net/problem/1939

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque, defaultdict
​
​
def solution():
    N, M = map(int, input().split())
    bridges = defaultdict(list)
    l, r = 1, 0
​
    for _ in range(M):
        a, b, c = map(int, input().split())
        bridges[a].append((b, c))
        bridges[b].append((a, c))
        r = max(r, c)
​
    A, B = map(int, input().split())
​
    def bfs(c):
        q = deque([A])
        visited = [0] * (N + 1)
        visited[A] = 1
​
        while q:
            node = q.popleft()
            if node == B:
                return True
​
            for n, w in bridges[node]:
                if not visited[n] and c <= w:
                    visited[n] = 1
                    q.append(n)
​
        return False
​
    answer = 0
    while l <= r:
        mid = (l + r) // 2
        if bfs(mid):
            answer = max(answer, mid)
            l = mid + 1
        else:
            r = mid - 1
​
    print(answer)
    return
​
​
solution()