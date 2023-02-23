// [문제 링크]: https://www.acmicpc.net/problem/20542

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, M = map(int, input().split())
    mine = input().rstrip()
    target = input().rstrip()
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, M + 1):
        dp[0][i] = i
    for i in range(1, N + 1):
        dp[i][0] = i
​
    for r in range(1, N + 1):
        for c in range(1, M + 1):
            if mine[r-1] == target[c-1] or (mine[r-1] == 'i' and (target[c-1] == 'l' or target[c-1] == 'j') or (mine[r-1] == 'v' and target[c-1] == 'w')):
                dp[r][c] = dp[r-1][c-1]
            else:
                dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
​
    print(dp[N][M])
    return
​
solution()
​