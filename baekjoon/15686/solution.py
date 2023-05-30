// [문제 링크]: https://www.acmicpc.net/problem/15686

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import combinations
​
​
def solution():
    n, m = map(int, input().split())
    chicken = []
    house = []
    answer = sys.maxsize
    for r in range(n):
        t = list(map(int, input().split()))
        for c in range(n):
            if t[c] == 2:
                chicken.append((r, c))
            elif t[c] == 1:
                house.append((r, c))
​
    for comb in combinations(chicken, m):
        tmp = 0
        for r1, c1 in house:
            d = sys.maxsize
            for r2, c2 in comb:
                d = min(d, abs(r1 - r2) + abs(c1 - c2))
            tmp += d
        answer = min(answer, tmp)
​
    print(answer)
    return
​
​
solution()