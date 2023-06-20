// [문제 링크]: https://www.acmicpc.net/problem/2630

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    white = blue = 0
​
    def check(sr, sc, size):
        prev = board[sr][sc]
        for r in range(sr, sr + size):
            for c in range(sc, sc + size):
                if prev != board[r][c]:
                    return False
        return True
​
    def dfs(sr, sc, size):
        nonlocal white, blue
        if size == 0:
            return
​
        if check(sr, sc, size):
            if board[sr][sc] == 1:
                blue += 1
            else:
                white += 1
            return
​
        dfs(sr, sc, size // 2)
        dfs(sr, sc + size // 2, size // 2)
        dfs(sr + size // 2, sc, size // 2)
        dfs(sr + size // 2, sc + size // 2, size // 2)
        return
​
    dfs(0, 0, n)
    print(white, blue, sep='\n')
    return
​
solution()
​