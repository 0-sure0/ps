// [문제 링크]: https://www.acmicpc.net/problem/1074

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
N, R, C = map(int, input().split())
​
​
def dfs(t, r, c):
    qr, qc = r // 2 ** t, c // 2 ** t
​
    if t == 0:
        return 2 * r + c
​
    return dfs(t - 1, r % 2 ** t, c % 2 ** t) + (2 ** t) ** 2 * (2 * qr + qc)
​
​
print(dfs(N - 1, R, C))
​
​