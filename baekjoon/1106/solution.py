// [문제 링크]: https://www.acmicpc.net/problem/1106

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from math import inf
​
def solution():
    C, N = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(N)]
    l.sort(key=lambda x: x[0], reverse=True)
    dp = [0] + [inf] * 1100
​
    for cost, people in l:
        for i in range(C + 1):
            dp[i + people] = min(dp[i + people], dp[i] + cost)
​
​
    print(min(dp[C:]))
    return
​
​
solution()
​