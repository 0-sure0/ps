// [문제 링크]: https://www.acmicpc.net/problem/17609

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
T = int(input())
​
​
def check(s, l, r, flag):
    while l <= r:
        if s[l] != s[r]:
            if flag:
                return 2
            a = check(s, l + 1, r, True)
            b = check(s, l, r - 1, True)
            return min(a, b)
​
        l += 1
        r -= 1
​
    return 1 if flag else 0
​
for _ in range(T):
    s = input().rstrip()
    print(check(s, 0, len(s) - 1, False))
​