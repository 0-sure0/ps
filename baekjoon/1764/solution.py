// [문제 링크]: https://www.acmicpc.net/problem/1764

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def solution():
    n, m = map(int, input().split())
    p1 = defaultdict(int)
    cnt = 0
    answer = []
    for _ in range(n):
        p1[input().rstrip()] = 1
​
    for _ in range(m):
        s = input().rstrip()
        if p1[s]:
            cnt += 1
            answer.append(s)
​
    print(cnt)
    print(*sorted(answer), sep='\n')
    return
​
solution()
​