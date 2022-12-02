// [문제 링크]: https://www.acmicpc.net/problem/2839

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    if N % 5 == 0:
        print(N // 5)
        return
​
​
    ans = N // 3 if N % 3 == 0 else sys.maxsize
    cnt = 0
    while N > 3:
        cnt += 1
        N -= 5
​
        if N % 3 == 0:
            ans = min(ans, cnt + N // 3)
​
    ans = -1 if ans == sys.maxsize else ans
    print(ans)
    return
​
​
solution()
​