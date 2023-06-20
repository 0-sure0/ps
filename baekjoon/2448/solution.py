// [문제 링크]: https://www.acmicpc.net/problem/2448

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    stars = [[' '] * 2 * n for _ in range(n)]
    default = ["  *  ", " * * ", "*****"]
​
    def sol(r, c, size):
        if size == 1:
            for i in range(3):
                for j in range(5):
                    stars[r + i][c + j] = default[i][j]
            return
​
        size //= 2
        sol(r, c + 3 * size, size)
        sol(r + 3 * size, c, size)
        sol(r + 3 * size, c + 6 * size, size)
        return
​
    sol(0, 0, n // 3)
    for star in stars:
        print(''.join(star))
    return
​
solution()
​