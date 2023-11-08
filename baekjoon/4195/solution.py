// [문제 링크]: https://www.acmicpc.net/problem/4195

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def find(node):
    if uf[node] < 0:
        return node
    uf[node] = find(uf[node])
    return uf[node]
​
​
def union(a, b):
    a = find(a)
    b = find(b)
​
    if a == b:
        return
​
    uf[b] = a
    size[a] += size[b]
​
    return
​
​
T = int(input())
for _ in range(T):
    F = int(input())
    uf = defaultdict(lambda: -1)
    size = defaultdict(lambda: 1)
    friends = {}
    idx = 0
    for _ in range(F):
        s1, s2 = input().split()
        if s1 not in friends:
            friends[s1] = idx
            idx += 1
        if s2 not in friends:
            friends[s2] = idx
            idx += 1
​
        union(friends[s1], friends[s2])
        print(size[find(friends[s1])])
        
​