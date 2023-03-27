// [문제 링크]: https://www.acmicpc.net/problem/11728

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, M = map(int, input().split())
    ans = []
    for _ in range(2):
        ans.extend(list(map(int, input().split())))
    ans.sort()
​
    print(*ans)
    return
​
solution()
​