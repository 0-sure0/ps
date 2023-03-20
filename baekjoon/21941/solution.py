// [문제 링크]: https://www.acmicpc.net/problem/21941

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    S = input().rstrip()
    M = int(input())
    words = [input().split() for _ in range(M)]
    dp = [0] + [i + 1 for i in range(len(S))]
​
    for i in range(1, len(S) + 1):
        for word, score in words:
            score = int(score)
            if i < len(word):
                continue
            if S[i-len(word):i] == word:
                dp[i] = max(dp[i], dp[i - len(word)] + score)
            else:
                dp[i] = max(dp[i], dp[i - 1] + 1)
​
​
    print(dp[-1])
    return
​
​
solution()
​