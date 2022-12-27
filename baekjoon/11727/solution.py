// [문제 링크]: https://www.acmicpc.net/problem/11727

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N = int(input())
    dp = [0, 1, 3]
​
    for i in range(3, N+1):
        dp.append(dp[i-1] + dp[i-2] * 2)
​
    print(dp[N] % 10007)
​
    return
​
solution()
​