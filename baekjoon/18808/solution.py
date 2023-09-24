// [문제 링크]: https://www.acmicpc.net/problem/18808

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, M, K = map(int, input().split())
    stickers = []
    for _ in range(K):
        r, c = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(r)]
        tmp = 0
        for y in range(r):
            for x in range(c):
                if sticker[y][x] == 1:
                    tmp += 1
        stickers.append((sticker, tmp))
​
​
    def rotate(sticker):
        sr, sc = len(sticker), len(sticker[0])
        board = []
        for c in range(sc):
            t = []
            for r in range(sr - 1, -1, -1):
                t.append(sticker[r][c])
            board.append(t)
​
        return board
​
    def check(r, c, sticker):
        sr, sc = len(sticker), len(sticker[0])
        for nr in range(r, r + sr):
            for nc in range(c, c + sc):
                if board[nr][nc] == 0 and sticker[nr - r][nc - c] == 1:
                    return False
​
        for nr in range(r, r + sr):
            for nc in range(c, c + sc):
                if sticker[nr - r][nc - c] == 1:
                    board[nr][nc] = 0
​
        return True
​
    def dfs(sticker):
        nonlocal answer
        sticker, tmp = sticker
​
        for _ in range(4):
            sr, sc = len(sticker), len(sticker[0])
            if sr <= N and sc <= M:
                for r in range(N - sr + 1):
                    for c in range(M - sc + 1):
                        if board[r][c] == 1 or (board[r][c] == 0 and sticker[0][0] == 0):
                            if check(r, c, sticker):
                                return (True, tmp)
​
            sticker = rotate(sticker)
​
        return (False, 0)
​
    board = [[1] * M for _ in range(N)]
    answer = 0
    for sticker in stickers:
        flag, t = dfs(sticker)
        if flag:
            answer += t
​
    print(answer)
    return
​
​
solution()