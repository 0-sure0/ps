// [문제 링크]: https://www.acmicpc.net/problem/21317

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    if n == 1:
        print(0)
        return
​
    jump = [list(map(int, input().split())) for _ in range(n - 1)]
    k = int(input())
    dp = [0] * n
    dp[1] = jump[0][0]
​
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + jump[i - 1][0], dp[i - 2] + jump[i - 2][1])
​
    answer = dp[-1]
​
    for t in range(n - 3):
        if dp[t] + k < dp[t + 3]:
            if t + 3 == n - 1:
                answer = min(answer, dp[t] + k)
                continue
​
            tmp = dp[:]
            tmp[t + 3] = tmp[t] + k
            j = t + 4
            tmp[j] = tmp[j - 1] + jump[j - 1][0]
            j += 1
​
            while j < n:
                tmp[j] = min(tmp[j - 1] + jump[j - 1][0], tmp[j - 2] + jump[j - 2][1])
                j += 1
​
            answer = min(answer, tmp[-1])
​
    print(answer)
    return
​
solution()
​