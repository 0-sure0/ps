// [문제 링크]: https://www.acmicpc.net/problem/17136

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
board = [list(map(int, input().split())) for _ in range(10)]
​
​
def check(r, c, size):
    if r + size > 10 or c + size > 10:
        return False
​
    for sr in range(r, r + size):
        for sc in range(c, c + size):
            if board[sr][sc] == 0:
                return False
    return True
​
​
def toggle(r, c, size):
    for sr in range(r, r + size):
        for sc in range(c, c + size):
            board[sr][sc] ^= 1
    return
​
​
def dfs(idx, size, t):
    global ans, total
​
    if idx >= 100:
        ans = min(ans, t)
        return
​
    r, c = idx // 10, idx % 10
​
    if board[r][c] == 0:
        dfs(idx + 1, size, t)
​
    for s in range(size, 0, -1):
        if total[s] and check(r, c, s):
            toggle(r, c, s)
            total[s] -= 1
            dfs(idx + s, size, t + 1)
            total[s] += 1
            toggle(r, c, s)
    return
​
​
total = [5] * 6
total[0] = 0
ans = sys.maxsize
dfs(0, 5, 0)
​
print(-1 if ans == sys.maxsize else ans)
​