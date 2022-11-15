// [문제 링크]: https://www.acmicpc.net/problem/2217

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    global rope
    rope = deque(sorted(rope))
    ans = 0
​
    while rope:
        ans = max(ans, rope[0] * len(rope))
        rope.popleft()
    print(ans)
    return
​
​
N = int(input())
rope = []
for _ in range(N):
    w = int(input())
    rope.append(w)
solution()