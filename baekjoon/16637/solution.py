// [문제 링크]: https://www.acmicpc.net/problem/16637

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    s = input().rstrip()
​
    def calc(n1, n2, op):
        n1 = str(n1)
        n2 = str(n2)
        return eval(n1 + op + n2)
​
    def func(idx, value):
        nonlocal answer
​
        if idx == N - 1:
            answer = max(answer, value)
            return
​
        func(idx + 2, calc(value, s[idx + 2], s[idx + 1]))
​
        if idx + 4 < N:
            func(idx + 4, calc(value, calc(s[idx + 2], s[idx + 4], s[idx + 3]), s[idx + 1]))
​
        return
​
    answer = -sys.maxsize
    func(0, int(s[0]))
    print(answer)
    return
​
​
solution()