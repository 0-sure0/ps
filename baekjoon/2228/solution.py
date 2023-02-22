// [문제 링크]: https://www.acmicpc.net/problem/2228

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from math import inf
​
def solution():
    N, M = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    dp1 = [[0] + [-inf] * M for _ in range(N + 1)]
    dp2 = [[0] + [-inf] * M for _ in range(N + 1)]
​
    for i in range(1, N + 1):
        for j in range(1, min(M, (i + 1) // 2 ) + 1):
            dp1[i][j] = max(dp2[i-1][j], dp1[i-1][j])
            dp2[i][j] = max(dp2[i-1][j], dp1[i-1][j-1]) + l[i-1]
​
​
    print(max(dp1[N][M], dp2[N][M]))
    return
​
solution()
​