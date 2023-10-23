// [문제 링크]: https://www.acmicpc.net/problem/1182

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import combinations
​
​
def solution():
    N, S = map(int, input().split())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(l) + 1):
        for comb in combinations(l, i):
            if sum(comb) == S:
                ans += 1
    print(ans)
    return
​
solution()
​