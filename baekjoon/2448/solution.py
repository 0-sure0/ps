// [문제 링크]: https://www.acmicpc.net/problem/2448

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    stars = [[' '] * 2 * n for _ in range(n)]
​
    def sol(r, c, size):
        if size == 3:
            stars[r][c] = '*'
            stars[r + 1][c - 1] = stars[r + 1][c + 1] = '*'
            for k in range(-2, 3):
                stars[r + 2][c - k] = '*'
        else:
            size //= 2
            sol(r, c, size)
            sol(r + size, c - size, size)
            sol(r + size, c + size, size)
​
    sol(0, n - 1, n)
    for star in stars:
        print(''.join(star))
    return
​
solution()
​