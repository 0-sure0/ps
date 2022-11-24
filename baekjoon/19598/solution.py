// [문제 링크]: https://www.acmicpc.net/problem/19598

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import heapq
​
​
def solution():
    conference = []
    for _ in range(N):
        a, b = map(int, input().split())
        conference.append([a, b])
​
    conference.sort()
    end = [0]
​
    for i in range(N):
        e = heapq.heappop(end)
        if e > conference[i][0]:
            heapq.heappush(end, e)
        heapq.heappush(end, conference[i][1])
​
    print(len(end))
    return
​
​
N = int(input())
solution()
​