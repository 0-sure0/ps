// [문제 링크]: https://www.acmicpc.net/problem/18352

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict, deque
​
​
def solution():
    n, m, k, x = map(int, input().split())
    graph = defaultdict(list)
    ans = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
​
    def bfs(start):
        checked = [0] * (n + 1)
        q = deque([start])
        checked[start] = 1
        depth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                ans[depth].append(node)
                for next_node in graph[node]:
                    if not checked[next_node]:
                        checked[next_node] = 1
                        q.append(next_node)
            depth += 1
        return
​
    bfs(x)
    if not ans[k]:
        print(-1)
    else:
        print(*sorted(ans[k]), sep='\n')
    return
​
solution()
​