// [문제 링크]: https://www.acmicpc.net/problem/18222

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    k = int(input())
​
    cnt = 0
    while k:
        cur = 1
        while cur * 2 < k:
            cur <<= 1
​
        k -= cur
        cnt += 1
​
    ans = ~cnt & 1
    print(ans)
    return
​
solution()
​