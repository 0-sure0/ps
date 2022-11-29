// [문제 링크]: https://www.acmicpc.net/problem/1715

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import heapq
​
def solution():
    cards = [int(input()) for _ in range(N)]
    heapq.heapify(cards)
    ans = 0
    while len(cards) > 1:
        c1 = heapq.heappop(cards)
        c2 = heapq.heappop(cards)
        ans += c1 + c2
        heapq.heappush(cards, c1 + c2)
​
    print(ans)
​
    return
​
​
N = int(input())
solution()
​