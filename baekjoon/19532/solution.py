// [문제 링크]: https://www.acmicpc.net/problem/19532

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    a, b, c, d, e, f = map(int, input().split())
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                print(x, y)
                return
​
​
solution()
​