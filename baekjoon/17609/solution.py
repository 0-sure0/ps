// [문제 링크]: https://www.acmicpc.net/problem/17609

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    t = int(input())
​
    def palin(start, end, del_cnt):
        if del_cnt == 2:
            return del_cnt
​
        while start <= end:
            if s[start] != s[end]:
                a = palin(start + 1, end, del_cnt + 1)
                b = palin(start, end - 1, del_cnt + 1)
                return a if a <= b else b
            start += 1
            end -= 1
​
        else:
            return del_cnt
​
    for _ in range(t):
        s = input().rstrip()
        print(palin(0, len(s) - 1, 0))
    return
​
solution()
​