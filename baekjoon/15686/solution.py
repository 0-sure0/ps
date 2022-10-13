// [문제 링크]: https://www.acmicpc.net/problem/15686

import sys
# sys.stdin = open("./test.txt", "r")
input = sys.stdin.readline
​
def dist(h):
    l = []
    for i in range(len(target)):
        min_d = 1000000
        for j in range(len(target[i])):
            min_d = min(min_d, abs(h[0] - target[i][j][0]) + abs(h[1] - target[i][j][1]))
        l.append(min_d)
​
    return l
​
​
def comb(l, depth):
    if len(l) == m:
        target.append(l)
        return
​
    elif depth == len(chicken):
        return
​
    l.append(chicken[depth])
    comb(l[:], depth + 1)
​
    l.pop()
    comb(l[:], depth + 1)
​
    return
​
​
def solution():
    comb([], 0)
    chicken_d = []
    for h in home:
        chicken_d.append(dist(h))
​
    ans = list(map(sum, zip(*chicken_d)))
    return min(ans)
​
​
n, m = map(int, input().split())
chicken = []
board = []
target = []
home = []
​
for i in range(n):
    t = list(map(int, input().split()))
    for j in range(n):
        if t[j] == 2:
            chicken.append([i, j])
        elif t[j] == 1:
            home.append([i, j])
    board.append(t)
​
print(solution())