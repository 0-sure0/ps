// [문제 링크]: https://www.acmicpc.net/problem/2110

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, c = map(int, input().split())
    house = sorted([int(input()) for _ in range(n)])
    start, end = 1, house[n - 1]
    answer = -1
​
    while start <= end:
        mid = start + (end - start) // 2
        cnt = 1
        last = house[0]
​
        for i in range(1, n):
            if house[i] - last >= mid:
                cnt += 1
                last = house[i]
​
        if cnt >= c:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
​
    print(answer)
    return
​
​
solution()
​