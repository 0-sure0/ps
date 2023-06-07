// [문제 링크]: https://www.acmicpc.net/problem/15649

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import permutations
​
def solution():
    n, m = map(int, input().split())
    for p in sorted(permutations(range(1, n + 1), m)):
        print(*p)
    return
​
​
solution()
​