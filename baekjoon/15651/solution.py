// [문제 링크]: https://www.acmicpc.net/problem/15651

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import product
​
def solution():
    n, m = map(int, input().split())
    for p in sorted(product(range(1, n + 1), repeat=m)):
        print(*p)
    return
​
​
solution()
​