// [문제 링크]: https://www.acmicpc.net/problem/2758

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    T = int(input())
    dp = [[1 if i == 0 and j != 0 else 0 for j in range(2001)] for i in range(10)]
​
    for i in range(1, 10):
        for j in range(1, 2001):
            dp[i][j] = sum(dp[i - 1][:j // 2 + 1])
​
    for _ in range(T):
        N, M = map(int, input().split())
        print(sum(dp[N - 1][:M + 1]))
​
    return
​
​
solution()
​