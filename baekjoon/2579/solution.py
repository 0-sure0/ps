// [문제 링크]: https://www.acmicpc.net/problem/2579

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    n = int(input())
    score = [int(input()) for _ in range(n)]
​
    if n <= 2:
        print(sum(score))
        return
​
    dp = [0] * n
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[2] + score[0], score[2] + score[1])
​
    for i in range(3, n):
        dp[i] = max(score[i] + score[i - 1] + dp[i - 3], score[i] + dp[i - 2])
​
    print(dp[-1])
    return
​
solution()
​