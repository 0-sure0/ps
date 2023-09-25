// [문제 링크]: https://www.acmicpc.net/problem/2470

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    ls = sorted(map(int, input().split()))
    answer = []
    tmp = sys.maxsize
    l, r = 0, N - 1
​
    while l < r:
        if abs(ls[l] + ls[r]) < tmp:
            answer = [ls[l], ls[r]]
            tmp = abs(ls[l] + ls[r])
​
        if ls[l] + ls[r] == 0:
            print(ls[l], ls[r])
            return
​
        elif ls[l] + ls[r] > 0:
            r -= 1
        else:
            l += 1
​
    print(*answer)
    return
​
​
solution()