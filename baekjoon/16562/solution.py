// [문제 링크]: https://www.acmicpc.net/problem/16562

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
​
def solution():
    n, m, k = map(int, input().split())
    uf = [-1 for i in range(n + 1)]
    fee = [0] + list(map(int, input().split()))
​
    def find(x):
        if uf[x] < 0:
            return x
        uf[x] = find(uf[x])
        return uf[x]
​
    def merge(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        uf[b] = a
        fee[a] = min(fee[a], fee[b])
        fee[b] = 0
        return
​
    for _ in range(m):
        a, b = map(int, input().split())
        merge(a, b)
​
    answer = sum(fee)
    print(answer if answer <= k else "Oh no")
    return
​
solution()
​