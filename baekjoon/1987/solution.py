// [문제 링크]: https://www.acmicpc.net/problem/1987

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    R, C = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]
    q = set([(0, 0, board[0][0])])
    answer = 0
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
​
    while q:
        for _ in range(len(q)):
            r, c, chars = q.pop()
            answer = max(answer, len(chars))
            for i in range(4):
                nr = r + dir[i][0]
                nc = c + dir[i][1]
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in chars:
                    q.add((nr, nc, chars + board[nr][nc]))
​
    print(answer)
    return
​
solution()
​