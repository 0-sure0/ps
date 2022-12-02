// [문제 링크]: https://www.acmicpc.net/problem/17626

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    dp = [0, 1]
​
    for i in range(2, N+1):
        min_v = sys.maxsize
        j = 1
​
        while (j ** 2) <= i:
            min_v = min(min_v, dp[i - (j ** 2)])
            j += 1
​
        dp.append(min_v + 1)
    print(dp[N])
    return
​
​
solution()
​