// [문제 링크]: https://www.acmicpc.net/problem/10942

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    nums = input().split()
    m = int(input())
    dp = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
​
    for step in range(1, n):
        for start in range(n):
            end = start + step
            if end >= n:
                break
            if step == 1 and nums[start] == nums[end]:
                dp[start][end] = 1
            elif nums[start] == nums[end] and dp[start + 1][end - 1] == 1:
                dp[start][end] = 1
​
    for _ in range(m):
        s, e = map(int, input().split())
        print(dp[s - 1][e - 1])
​
    return
​
solution()