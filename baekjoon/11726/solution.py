// [문제 링크]: https://www.acmicpc.net/problem/11726

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N = int(input())
    dp = [0, 1, 2]
​
    if N < 3:
        print(dp[N])
        return
​
    for i in range(3, N+1):
        t = 0
        for j in range(1, 3):
            t += dp[i-j]
        dp.append(t)
​
    print(dp[N] % 10007)
    return
​
solution()
​