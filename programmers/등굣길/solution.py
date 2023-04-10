// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    mod = 1000000007
    board = [[0] * (m + 1) for _ in range(n + 1)]
    board[1][1] = 1
    for x, y in puddles:
        board[y][x] = -1

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if board[y][x] == -1:
                board[y][x] = 0
                continue
            board[y][x] += (board[y - 1][x] + board[y][x - 1]) % mod

    return board[n][m]