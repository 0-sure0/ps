// [문제 링크]: https://www.acmicpc.net/problem/12865

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, K = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (K + 1)
​
    for w, v in wv:
        for i in range(K, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
​
    print(dp[K])
    return
​
​
solution()
​