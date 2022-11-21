// [문제 링크]: https://www.acmicpc.net/problem/20300

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    weights.sort()
    length = len(weights)
    l = r = 0
    ans = 0
​
    if length % 2 == 0:
        l, r = 0, length - 1
​
    else:
        l, r = 0, length - 2
        ans = weights[-1]
​
    while l <= r:
        ans = max(ans, weights[l] + weights[r])
        l += 1
        r -= 1
​
    print(ans)
​
    return
​
​
N = int(input())
weights = list(map(int, input().split()))
solution()