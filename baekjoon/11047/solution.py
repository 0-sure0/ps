// [문제 링크]: https://www.acmicpc.net/problem/11047

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    global K
    coin = []
    for _ in range(N):
        c = int(input())
        if c == K:
            print(1)
            return
        coin.append(c)
​
    ans = 0
    for i in range(N-1, -1, -1):
        if coin[i] > K:
            continue
​
        ans += K // coin[i]
        K %= coin[i]
        if K == 0:
            break
​
    if K != 0:
        ans = N
    print(ans)
​
    return
​
​
​
N, K = map(int, input().split())
solution()
​