// [문제 링크]: https://www.acmicpc.net/problem/2417

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from math import sqrt
​
​
def solution():
    n = int(input())
    if n == 0:
        print(0)
        return
    
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        if mid ** 2 >= n:
            r = mid - 1
        else:
            l = mid + 1
​
    print(r + 1)
    return
​
solution()
​
​