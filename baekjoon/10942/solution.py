// [문제 링크]: https://www.acmicpc.net/problem/10942

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    nums = input().split()
    M = int(input())
    dp = [[0 if i != j else 1 for j in range(N)] for i in range(N)]
​
    for step in range(1, N):
        for start in range(N):
            end = start + step
            if end >= N:
                break
            if step == 1 and nums[start] == nums[end]:
                dp[start][end] = 1
            elif nums[start] == nums[end] and dp[start+1][end-1] == 1:
                dp[start][end] = 1
​
    for _ in range(M):
        S, E = map(int, input().split())
        print(1 if dp[S-1][E-1] == 1 else 0)
    return
​
solution()
​