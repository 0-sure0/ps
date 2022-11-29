// [문제 링크]: https://www.acmicpc.net/problem/2285

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    village = [list(map(int, input().split())) for _ in range(N)]
    village.sort()
​
    dist = 0
    l_man = r_man = 0
    for i in range(N):
        r_man += village[i][1]
        dist += (village[i][0] - village[0][0]) * village[i][1]
​
    min_dist = dist
    ans = village[0][0]
    for i in range(1, N):
        l_man += village[i-1][1]
        r_man -= village[i-1][1]
        dist += (l_man - r_man) * (village[i][0] - village[i-1][0])
        if dist < min_dist:
            min_dist = dist
            ans = village[i][0]
​
    print(ans)
    return
​
​
N = int(input())
solution()