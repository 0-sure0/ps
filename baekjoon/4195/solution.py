// [문제 링크]: https://www.acmicpc.net/problem/4195

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def find(node):
    if not uf[node]:
        return node
    uf[node] = find(uf[node])
    return uf[node]
​
​
T = int(input())
for _ in range(T):
    F = int(input())
    uf = defaultdict(str)
    friend = defaultdict(list)
​
    for _ in range(F):
        s1, s2 = input().split()
        s1 = find(s1)
        s2 = find(s2)
        if s1 != s2:
            friend[s1].append(s2)
            friend[s1].extend(friend[s2])
            uf[s2] = s1
        print(len(friend[s1]) + 1)
​