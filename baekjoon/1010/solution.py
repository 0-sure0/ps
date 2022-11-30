// [문제 링크]: https://www.acmicpc.net/problem/1010

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    dp = [1, 1, 2]
    for i in range(3, 31):
        dp.append(i * dp[i-1])
​
    def comb(n, r):
        if n == r:
            return 1
        return dp[n] // (dp[n-r] * dp[r])
    for _ in range(T):
        left, right = map(int, input().split())
        print(comb(right, left))
​
    return
​
​
T = int(input())
solution()
​