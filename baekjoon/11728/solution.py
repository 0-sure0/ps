// [문제 링크]: https://www.acmicpc.net/problem/11728

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, M = map(int, input().split())
    ans = []
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    l, r = 0, 0
​
    while l < N and r < M:
        if a[l] <= b[r]:
            ans.append(a[l])
            l += 1
        else:
            ans.append(b[r])
            r += 1
​
    if l < N:
        ans += a[l:]
    else:
        ans += b[r:]
​
    print(*map(str, ans))
    return
​
solution()
​