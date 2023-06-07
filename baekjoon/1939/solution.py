// [문제 링크]: https://www.acmicpc.net/problem/1939

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque, defaultdict
​
​
def solution():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    max_weight = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        max_weight = max(max_weight, c)
    s, e = map(int, input().split())
​
    def bfs(weight):
        checked[s] = 1
        q = deque([s])
        while q:
            node = q.popleft()
            if node == e:
                return True
​
            for next_node, w in graph[node]:
                if not checked[next_node] and mid <= w:
                    q.append(next_node)
                    checked[next_node] = 1
​
        return False
    
    l, r = 0, max_weight
    while l <= r:
        checked = [0] * (n + 1)
        mid = l + (r - l) // 2
        if bfs(mid):
            l = mid + 1
        else:
            r = mid - 1
​
    print(r)
    return
​
​
solution()
​