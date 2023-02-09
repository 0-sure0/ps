// [문제 링크]: https://www.acmicpc.net/problem/2156

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    n = int(input())
    wine = [int(input()) for _ in range(n)]
    if n == 1:
        print(wine[0])
        return
    elif n == 2:
        print(wine[0] + wine[1])
        return
    dp = [wine[0], wine[0] + wine[1], max(wine[0] + wine[2], wine[1] + wine[2], wine[0] + wine[1])]
​
    for i in range(3, n):
        dp.append(max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], wine[i] + dp[i-2]))
​
    print(dp[-1])
​
    return
​
solution()
​