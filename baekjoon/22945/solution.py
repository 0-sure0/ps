// [문제 링크]: https://www.acmicpc.net/problem/22945

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    arr = [0] + list(map(int, input().split()))
​
    l, r = 1, N
    ans = 0
​
    def calc(l, r):
        return (r - l - 1) * min(arr[l], arr[r])
​
    while l <= r:
        ans = max(ans, calc(l, r))
        if arr[l] <= arr[r]:
            l += 1
        else:
            r -= 1
​
    print(ans)
    return
​
solution()
​