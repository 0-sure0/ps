// [문제 링크]: https://www.acmicpc.net/problem/11055

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = nums[:]
​
    for i in range(N - 1):
        for j in range(i + 1, N):
            if nums[i] < nums[j]:
                dp[j] = max(dp[i] + nums[j], dp[j])
    print(max(dp))
    return
​
solution()
​