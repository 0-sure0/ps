// [문제 링크]: https://www.acmicpc.net/problem/13164

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, K = map(int, input().split())
    height = list(map(int, input().split()))
    diff = []
    for i in range(1, N):
        diff.append(height[i] - height[i-1])
    diff.sort()
    
    ans = 0
    for i in range(N-K):
        ans += diff[i]
​
    print(ans)
    return
​
​
solution()
​