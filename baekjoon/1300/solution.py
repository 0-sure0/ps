// [문제 링크]: https://www.acmicpc.net/problem/1300

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    K = int(input())
​
    def count(v):
        cnt = 0
        for i in range(1, N + 1):
            cnt += min(v // i, N)
​
        return cnt
​
    l, r = 1, 10 ** 9
    answer = 1
    while l <= r:
        mid = (l + r) // 2
        if count(mid) >= K:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
​
    print(answer)
    return
​
​
solution()