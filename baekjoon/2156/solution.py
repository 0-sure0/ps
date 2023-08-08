// [문제 링크]: https://www.acmicpc.net/problem/2156

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    wine = [int(input()) for _ in range(n)]
​
    if n <= 2:
        print(sum(wine))
        return
​
    dp = [0] * n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])
​
    for i in range(3, n):
        dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2], dp[i - 1])
​
    print(dp[-1])
    return
​
solution()
​