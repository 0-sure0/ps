// [문제 링크]: https://www.acmicpc.net/problem/2417

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import math
​
def solution():
    N = int(input())
    q = int(math.sqrt(N))
    print(q + 1 if q ** 2 < N else q)
    return
​
​
solution()