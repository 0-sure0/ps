// [문제 링크]: https://www.acmicpc.net/problem/9095

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    dp = [0, 1, 2, 4]
    T = int(input())
    for _ in range(T):
        n = int(input())
        if len(dp) >= n+1:
            print(dp[n])
            continue
        for i in range(len(dp), n+1):
            t = 0
            for j in range(1, 4):
                t += dp[i-j]
            dp.append(t)
​
        print(dp[n])
    return
​
solution()
​