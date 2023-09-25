// [문제 링크]: https://www.acmicpc.net/problem/2417

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    l, r = 0, N
    while l <= r:
        q = (l + r) // 2
        if q ** 2 < N:
            l = q + 1
        elif q ** 2 >= N:
            r = q - 1
​
    print(r + 1)
    return
​
​
solution()