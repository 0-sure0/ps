// [문제 링크]: https://www.acmicpc.net/problem/20440

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def solution():
    n = int(input())
    mos_io = defaultdict(int)
    for _ in range(n):
        i, o = map(int, input().split())
        mos_io[i] += 1
        mos_io[o] -= 1
​
    max_cnt = -1
    answer = [0, 0]
    flag = False
    s = 0
​
    for t in sorted(mos_io.keys()):
        s += mos_io[t]
        if s > max_cnt:
            max_cnt = s
            answer[0] = t
            flag = True
​
        elif s < max_cnt and flag:
            answer[1] = t
            flag = False
​
    print(max_cnt)
    print(*answer)
​
solution()
​