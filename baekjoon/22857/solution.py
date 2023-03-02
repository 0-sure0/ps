// [문제 링크]: https://www.acmicpc.net/problem/22857

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, K = map(int, input().split())
    s = list(map(int, input().split()))
    l = r = 0
    ans = cnt = 0
​
    while l <= r < N:
        if cnt <= K:
            if s[r] % 2 != 0:
                cnt += 1
            r += 1
​
        else:
            if s[l] % 2 != 0:
                cnt -= 1
            l += 1
​
        if cnt <= K:
            ans = max(ans, r - l - cnt)
​
    print(ans)
    return
​
​
solution()
​