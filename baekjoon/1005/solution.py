// [문제 링크]: https://www.acmicpc.net/problem/1005

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        time = list(map(int, input().split()))
        total_time = [0] * n
        graph = [[] for _ in range(n)]
        indegree = [0] * n
​
        for _ in range(k):
            x, y = map(int, input().split())
            indegree[y - 1] += 1
            graph[x - 1].append(y - 1)
​
        w = int(input())
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                total_time[i] = time[i]
​
        while q:
            a = q.popleft()
            if a == w - 1:
                break
​
            for b in graph[a]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    q.append(b)
                total_time[b] = max(total_time[b], total_time[a] + time[b])
​
        print(total_time[w - 1])
​
    return
​
solution()