// [문제 링크]: https://www.acmicpc.net/problem/1912

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [nums[0]]
​
    for i in range(1, N):
        dp.append(max(dp[i-1] + nums[i], nums[i-1] + nums[i], nums[i]))
    print(max(dp))
    return
​
solution()
​