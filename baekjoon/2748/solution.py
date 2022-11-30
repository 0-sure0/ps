// [문제 링크]: https://www.acmicpc.net/problem/2748

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    dp = [0, 1]
​
    for i in range(2, N+1):
        dp.append(dp[i-1] + dp[i-2])
​
    print(dp[N])
    return
​
​
N = int(input())
solution()
​