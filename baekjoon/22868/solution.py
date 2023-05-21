// [문제 링크]: https://www.acmicpc.net/problem/22868

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict, deque
​
​
def solution():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, e = map(int, input().split())
​
    for i in range(1, n + 1):
        graph[i].sort()
​
    def bfs(start, end):
        q = deque()
        q.append((start, [start]))
        depth = 0
        checked[start] = 1
​
        while q:
            depth += 1
            for _ in range(len(q)):
                node, path = q.popleft()
​
                for next_node in graph[node]:
                    if next_node == end:
                        return depth, path + [next_node]
​
                    if not checked[next_node]:
                        checked[next_node] = 1
                        q.append((next_node, path + [next_node]))
​
        return 0
​
    checked = [0] * (n + 1)
    length = 0
    depth, path = bfs(s, e)
    checked = [0] * (n + 1)
    for node in path:
        checked[node] = 1
​
    length += depth
    depth, path = bfs(e, s)
    length += depth
​
    print(length)
    return
​
solution()
​
​