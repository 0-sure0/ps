// [문제 링크]: https://www.acmicpc.net/problem/4195

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    t = int(input())
​
    def find(x):
        if uf[x] < 0:
            return x
        uf[x] = find(uf[x])
        return uf[x]
​
    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
​
        uf[b] = a
        size[a] += size[b]
        return
​
    for _ in range(t):
        f = int(input())
        idx = 0
        friends = {}
        uf = [-1] * 200000
        size = [1] * 200000
​
        for _ in range(f):
            f1, f2 = input().rstrip().split()
            if f1 not in friends:
                friends[f1] = idx
                idx += 1
            if f2 not in friends:
                friends[f2] = idx
                idx += 1
​
            union(friends[f1], friends[f2])
            print(size[find(friends[f1])])
​
    return
​
solution()
​