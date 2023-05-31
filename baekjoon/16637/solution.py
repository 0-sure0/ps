// [문제 링크]: https://www.acmicpc.net/problem/16637

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import math
​
def solution():
    n: int = int(input())
    s: str = input().rstrip()
    result: int = -math.inf
​
    def calc(n1: int, op: int, n2: int):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
​
    def dfs(idx: int, value: int):
        nonlocal result
        if idx == n - 1:
            result = max(result, value)
            return
​
        if idx + 2 < n:
            dfs(idx + 2, calc(value, s[idx + 1], int(s[idx + 2])))
​
        if idx + 4 < n:
            dfs(idx + 4, calc(value, s[idx + 1], calc(int(s[idx + 2]), s[idx + 3], int(s[idx + 4]))))
​
        return
​
    dfs(0, int(s[0]))
    print(result)
    return
​
solution()
​
​