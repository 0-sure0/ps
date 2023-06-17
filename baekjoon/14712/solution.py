// [문제 링크]: https://www.acmicpc.net/problem/14712

import sys
input = sys.stdin.readline
def getInts(): return map(int, input().split())
​
​
def dfs(k):
    global cnt
    if k == N * M:
        cnt += 1
        return
    y, x = k//M + 1, k % M + 1
​
    # 넴모 안놓는 경우
    dfs(k+1)
​
    # 넴모 놓는 경우
    # 지금 놓은 칸이 2*2 넴모를 구성해 터지지 않는 경우만 놓기
    if not (board[y-1][x]*board[y][x-1]*board[y-1][x-1]):
        board[y][x] = 1
        dfs(k+1)
        board[y][x] = 0
​
​
N, M = getInts()
board = [[0]*(M+1) for _ in range(N+1)]
cnt = 0
dfs(0)
print(cnt)
​