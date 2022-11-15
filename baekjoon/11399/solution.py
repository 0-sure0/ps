// [문제 링크]: https://www.acmicpc.net/problem/11399

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from functools import reduce
​
def solution():
    global time
    time.sort()
    ans = prev = 0
    for t in time:
        ans += prev + t
        prev += t
    print(ans)
​
    return
​
​
N = int(input())
time = list(map(int, input().split()))
solution()