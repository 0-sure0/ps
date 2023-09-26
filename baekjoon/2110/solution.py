// [문제 링크]: https://www.acmicpc.net/problem/2110

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, C = map(int, input().split())
    house = sorted([int(input()) for _ in range(N)])
    l, r = 1, house[-1]
    answer = 0
​
    while l <= r:
        mid = (l + r) // 2
        cnt = 1
        prev = house[0]
​
        for i in range(1, N):
            if house[i] - prev >= mid:
                cnt += 1
                prev = house[i]
​
        if cnt >= C:
            answer = mid
            l = mid + 1
​
        else:
            r = mid - 1
​
    print(answer)
    return
​
​
solution()