// [문제 링크]: https://www.acmicpc.net/problem/15663

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import permutations
​
def solution():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    for s in sorted(set(permutations(nums, m))):
        print(*s)
​
    return
​
​
solution()
​