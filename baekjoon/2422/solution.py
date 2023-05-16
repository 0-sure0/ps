// [문제 링크]: https://www.acmicpc.net/problem/2422

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import combinations
​
def solution():
    n, m = map(int, input().split())
    ice = [[0] * n for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        a -= 1; b -= 1;
        ice[a][b] = 1
        ice[b][a] = 1
​
    answer = 0
    for comb in combinations(range(n), 3):
        if ice[comb[0]][comb[1]] or ice[comb[0]][comb[2]] or ice[comb[1]][comb[2]]:
            continue
​
        answer += 1
​
    print(answer)
    return
​
​
solution()
​