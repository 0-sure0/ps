// [문제 링크]: https://www.acmicpc.net/problem/1463

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N = int(input())
    dp = [0, 0, 1, 1]
​
    for i in range(4, N+1):
        t = []
        t.append(dp[i-1])
        if i % 2 == 0:
            t.append(dp[i // 2])
        if i % 3 == 0:
            t.append(dp[i // 3])
        dp.append(min(t) + 1)
    print(dp[N])
    return
​
solution()
​