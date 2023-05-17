// [문제 링크]: https://www.acmicpc.net/problem/2961

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import combinations
​
​
def solution():
    n = int(input())
    taste = [list(map(int, input().split())) for _ in range(n)]
    answer = sys.maxsize
​
    for i in range(1, n + 1):
        for comb in combinations(taste, i):
            s, b = 1, 0
            for t in comb:
                s *= t[0]
                b += t[1]
​
            answer = min(answer, abs(s - b))
​
    print(answer)
    return
​
solution()
​
​