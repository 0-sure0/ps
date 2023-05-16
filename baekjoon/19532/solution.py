// [문제 링크]: https://www.acmicpc.net/problem/19532

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import product
​
def solution():
    a, b, c, d, e, f = map(int, input().split())
    for x, y in product(range(-999, 1000), repeat=2):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            return
​
​
    return
​
​
solution()
​