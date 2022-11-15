// [문제 링크]: https://www.acmicpc.net/problem/11508

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from functools import reduce
​
def solution():
    price = [int(input()) for _ in range(N)]
    price.sort(reverse=True)
    cnt = 0
    ans = 0
    for i in range(N):
        cnt += 1
        if cnt == 3:
            cnt = 0
            continue
        ans += price[i]
​
​
​
    print(ans)
    return
​
​
N = int(input())
solution()
​