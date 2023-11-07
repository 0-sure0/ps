// [문제 링크]: https://www.acmicpc.net/problem/1865

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def bellman_ford():
    dist = [0] * (N + 1)
​
    for i in range(N):
        for s, e, t in edges:
            if dist[s] != sys.maxsize and dist[s] + t < dist[e]:
                dist[e] = dist[s] + t
                if i == N - 1:
                    return True
​
    return False
​
​
TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
​
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
​
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
​
    print("YES" if bellman_ford() else "NO")
​