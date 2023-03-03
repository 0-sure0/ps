// [문제 링크]: https://www.acmicpc.net/problem/22869

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, K = map(int, input().split())
    stone = list(map(int, input().split()))
    dp = ['YES' if i == 0 else 'NO' for i in range(N)]
​
    def power(i, j):
        return (i - j) * (1 + abs(stone[i] - stone[j]))
​
    for i in range(1, N):
        for j in range(0, i):
            if dp[j] == 'NO':
                continue
            if power(i, j) <= K:
                dp[i] = 'YES'
                break
​
    print(dp[-1])
    return
​
​
solution()
​