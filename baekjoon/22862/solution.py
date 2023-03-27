// [문제 링크]: https://www.acmicpc.net/problem/22862

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, K = map(int, input().split())
    S = list(map(int, input().split()))
    cnt = l = r = 0
    t = ans = 0
​
    while l <= r < N:
        if S[r] % 2 == 0:
            t += 1
        else:
            cnt += 1
            if cnt > K:
                ans = max(ans, t)
                while cnt > K:
                    if S[l] % 2 != 0:
                        cnt -= 1
                    else:
                        t -= 1
                    l += 1
        r += 1
​
    print(max(ans, t))
    return
​
solution()
​