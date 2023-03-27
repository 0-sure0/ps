// [문제 링크]: https://www.acmicpc.net/problem/11049

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
​
    for i in range(1, N):
        for j in range(N - i):
            x = j + i
            dp[j][x] = 2 ** 32
            for k in range(j, x):
                dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + matrix[j][0] * matrix[k][1] * matrix[x][1])
​
    print(dp[0][N - 1])
    return
​
solution()
​