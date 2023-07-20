// [문제 링크]: https://www.acmicpc.net/problem/11000

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import heapq
​
def solution():
    n = int(input())
    h = []
    for _ in range(n):
        l = list(map(int, input().split()))
        heapq.heappush(h, l)
    end = []
    heapq.heappush(end, heapq.heappop(h)[1])
    while h:
        s, t = heapq.heappop(h)
        if end[0] <= s:
            heapq.heappop(end)
            heapq.heappush(end, t)
        else:
            heapq.heappush(end, t)
​
    print(len(end))
    return
​
solution()
​