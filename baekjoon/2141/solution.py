// [문제 링크]: https://www.acmicpc.net/problem/2141

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    n = int(input())
    village = []
    s = 0
    for _ in range(n):
        l = list(map(int, input().split()))
        s += l[1]
        village.append(l)
​
    village.sort()
    t = 0
    for i in range(n):
        x, a = village[i]
        t += a
        if t >= s / 2:
            print(x)
            break
    return
​
solution()
​