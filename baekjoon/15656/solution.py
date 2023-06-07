// [문제 링크]: https://www.acmicpc.net/problem/15656

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import product
​
def solution():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    for comb in sorted(product(nums, repeat=m)):
        print(*comb)
​
​
    return
​
​
solution()
​