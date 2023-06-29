// [문제 링크]: https://www.acmicpc.net/problem/1647

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, m = map(int, input().split())
    uf = [-1] * (n + 1)
    edge = [list(map(int, input().split())) for _ in range(m)]
    edge.sort(key=lambda x: x[2])
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
            return False
        uf[b] = a
        return True
​
    answer = 0
    max_c = 0
    for a, b, c in edge:
        if union(a, b):
            answer += c
            max_c = max(max_c, c)
​
    print(answer - max_c)
    return
​
solution()
​