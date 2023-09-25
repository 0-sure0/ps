// [문제 링크]: https://www.acmicpc.net/problem/22871

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    stone = list(map(int, input().split()))
    dp = [sys.maxsize] * N
    dp[0] = 0
​
    for i in range(1, N):
        for j in range(i):
            k = max((i - j) * (1 + abs(stone[j] - stone[i])), dp[j])
            dp[i] = min(dp[i], k)
​
    print(dp[-1])
    return
​
​
solution()