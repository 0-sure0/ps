// [문제 링크]: https://www.acmicpc.net/problem/14916

import sys
# sys.stdin = open("test.txt", "r")
input = sys.stdin.readline
​
def solution():
    global n
​
    if n % 5 == 0:
        print(n // 5)
        return
​
    q = n // 5
    ans = q
    r = n % 5
    while q:
        if r % 2 == 0:
            ans += r // 2
            print(ans)
            return
​
        q -= 1
        ans = q
        r += 5
​
    if n % 2 == 0:
        print(n // 2)
        return
​
    print(-1)
​
    return
​
​
n = int(input())
solution()
​