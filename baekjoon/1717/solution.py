// [문제 링크]: https://www.acmicpc.net/problem/1717

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
​
def solution():
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
​
    def get_parent(node):
        if node == parent[node]:
            return node
        parent[node] = get_parent(parent[node])
        return parent[node]
​
    def union_parent(a, b):
        a = get_parent(a)
        b = get_parent(b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
        return
​
    for _ in range(m):
        x, a, b = map(int, input().split())
        if x == 0:
            union_parent(a, b)
        else:
            if get_parent(a) == get_parent(b):
                print("yes")
            else:
                print("no")
    return
​
solution()
​