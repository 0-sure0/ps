// [문제 링크]: https://www.acmicpc.net/problem/16937

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    h, w = map(int, input().split())
    n = int(input())
    stikcer = [list(map(int, input().split())) for _ in range(n)]
​
    answer = 0
    for i in range(n):
        for j in range(i + 1, n):
            r1, c1 = stikcer[i]
            r2, c2 = stikcer[j]
​
            if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
                answer = max(answer, r1 * c1 + r2 * c2)
            if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
                answer = max(answer, r1 * c1 + r2 * c2)
            if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
                answer = max(answer, r1 * c1 + r2 * c2)
            if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
                answer = max(answer, r1 * c1 + r2 * c2)
​
    print(answer)
    return
​
solution()
​
​