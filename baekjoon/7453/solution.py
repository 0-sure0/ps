// [문제 링크]: https://www.acmicpc.net/problem/7453

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import bisect
​
​
def solution():
    n = int(input())
    A = []; B = []; C = []; D = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)
​
    ab = []
    cd = []
    for i in range(n):
        for j in range(n):
            ab.append(A[i] + B[j])
            cd.append(C[i] + D[j])
    ab.sort()
    cd.sort()
    l, r = 0, len(cd) - 1
    answer = 0
    while l < len(ab) and 0 <= r:
        t = ab[l] + cd[r]
        if t < 0:
            l += 1
        elif t > 0:
            r -= 1
        else:
            abl, abr = bisect.bisect_left(ab, ab[l]), bisect.bisect_right(ab, ab[l])
            cdl, cdr = bisect.bisect_left(cd, cd[r]), bisect.bisect_right(cd, cd[r])
            answer += (abr - abl) * (cdr - cdl)
            l, r = abr, cdl - 1
​
    print(answer)
    return
​
solution()