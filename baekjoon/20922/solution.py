// [문제 링크]: https://www.acmicpc.net/problem/20922

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def solution():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    count = defaultdict(int)
    ans = 0
    l = r = 0
​
    while l <= r and r < N:
        if count[arr[r]] < K:
            count[arr[r]] += 1
            r += 1
        else:
            ans = max(ans, r - l)
            while arr[l] != arr[r]:
                count[arr[l]] -= 1
                l += 1
            count[arr[l]] -= 1
            l += 1
​
    print(max(ans, r - l))
    return
​
solution()
​