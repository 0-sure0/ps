// [문제 링크]: https://www.acmicpc.net/problem/14567

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict, deque
​
​
def solution():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    indegree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
​
    answer = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            answer[i] = 1
    while q:
        cur = q.popleft()
        for node in graph[cur]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)
                answer[node] = answer[cur] + 1
​
    print(*answer[1:], sep=' ')
    return
​
​
solution()
​