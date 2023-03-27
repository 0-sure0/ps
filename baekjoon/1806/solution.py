// [문제 링크]: https://www.acmicpc.net/problem/1806

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 10 ** 8
    tmp = l = r = 0
​
    while l <= r < N:
        tmp += arr[r]
        if tmp >= S:
            ans = min(ans, r - l + 1)
            while tmp >= S:
                tmp -= arr[l]
                l += 1
                if tmp >= S:
                    ans = min(ans, r - l + 1)
        r += 1
​
    print(0 if ans == 10 ** 8 else ans)
    return
​
solution()
​