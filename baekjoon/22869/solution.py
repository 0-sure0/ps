// [문제 링크]: https://www.acmicpc.net/problem/22869

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, K = map(int, input().split())
    stone = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = 1
    j = 1
​
    while j < N:
        if dp[j] == 1:
            continue
​
        for i in range(j-1, -1, -1):
            if dp[i] and (j - i) * (1 + abs(stone[i] - stone[j])) <= K:
                dp[j] = 1
                break
        j += 1
​
    ans = 'NO' if dp[-1] != 1 else 'YES'
    print(ans)
    return
​
solution()
​