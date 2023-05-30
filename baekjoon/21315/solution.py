// [문제 링크]: https://www.acmicpc.net/problem/21315

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import math
​
​
def solution():
    n = int(input())
    result = list(map(int, input().split()))
    max_k = int(math.log2(n))
​
    def mix(k):
        nonlocal card
        end = n - 1
        for i in range(1, k + 2):
            sorted_card = []
            cnt = 2 ** (k - i + 1)
            start = end - cnt + 1
            for idx in range(start, end + 1):
                sorted_card.append(card[idx])
            for idx in range(start):
                sorted_card.append(card[idx])
            for idx in range(end + 1, n):
                sorted_card.append(card[idx])
            card = sorted_card
            end = cnt - 1
​
        return
​
​
    for k1 in range(1, max_k + 1):
        for k2 in range(1, max_k + 1):
            card = range(1, n + 1)
            mix(k1)
            mix(k2)
            if card == result:
                print(k1, k2)
                return
​
    return
​
solution()
​
​