// [문제 링크]: https://www.acmicpc.net/problem/1789

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    S = int(input())
    n = 1
​
    while (n * (n + 1) // 2) <= S:
        n += 1
​
    print(n - 1)
    return
​
​
solution()