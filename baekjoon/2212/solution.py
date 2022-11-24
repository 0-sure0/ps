// [문제 링크]: https://www.acmicpc.net/problem/2212

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    coord = list(map(int, input().split()))
    coord.sort()
    diff = [coord[i] - coord[i-1] for i in range(1, N)]
    diff.sort()
    print(sum(diff[:N-K]))
    return
​
​
N = int(input())
K = int(input())
​
solution()
​