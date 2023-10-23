// [문제 링크]: https://www.acmicpc.net/problem/14712

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
N, M = map(int, input().split())
board = [[0] * (M + 1) for _ in range(N + 1)]
ans = 0
​
def dfs(cnt):
    global ans
​
    if cnt == N * M:
        ans += 1
        return
​
    dfs(cnt + 1)
    r, c = cnt // M + 1, cnt % M + 1
    if not board[r - 1][c] or not board[r][c - 1] or not board[r - 1][c - 1]:
        board[r][c] = 1
        dfs(cnt + 1)
        board[r][c] = 0
​
    return
​
dfs(0)
print(ans)
​
​