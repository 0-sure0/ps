// [문제 링크]: https://www.acmicpc.net/problem/2110

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, C = map(int, input().split())
    house = sorted([int(input()) for _ in range(N)])
    s, e = 1, house[N - 1]
    answer = -1
​
    while s <= e:
        mid = (s + e) // 2
        cnt = 1
        last = house[0]
​
        for i in range(1, N):
            if house[i] - last >= mid:
                cnt += 1
                last = house[i]
​
        if cnt >= C:
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
​
    print(answer)
    return
​
​
solution()