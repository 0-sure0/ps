// [문제 링크]: https://www.acmicpc.net/problem/15681

import sys
​
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
sys.setrecursionlimit(10 ** 9)
​
​
def solution():
    n, r, q = map(int, input().split())
    graph = defaultdict(list)
    tree = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
​
    def make_tree(vertex, p):
        for v in graph[vertex]:
            if v != p:
                tree[vertex].append(v)
                parent[v] = vertex
                size[vertex] += make_tree(v, vertex)
        return size[vertex]
​
    parent = [0] * (n + 1)
    size = [1] * (n + 1)
    make_tree(r, -1)
​
    for _ in range(q):
        target = int(input())
        print(size[target])
​
    return
​
​
solution()
​