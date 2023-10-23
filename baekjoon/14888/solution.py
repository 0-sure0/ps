// [문제 링크]: https://www.acmicpc.net/problem/14888

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from math import ceil
​
​
def solution():
    N = int(input())
    l = list(map(int, input().split()))
    ops = list(map(int, input().split()))
​
    def dfs(idx, t):
        nonlocal max_ans, min_ans
        if idx >= len(l) - 1:
            max_ans = max(max_ans, t)
            min_ans = min(min_ans, t)
            return
​
        for i in range(len(ops)):
            if not ops[i]:
                continue
            if i == 0:
                ops[0] -= 1
                dfs(idx + 1, t + l[idx + 1])
                ops[0] += 1
​
            if i == 1:
                ops[1] -= 1
                dfs(idx + 1, t - l[idx + 1])
                ops[1] += 1
​
            if i == 2:
                ops[2] -= 1
                dfs(idx + 1, t * l[idx + 1])
                ops[2] += 1
​
            if i == 3:
                ops[3] -= 1
                tmp = 0
                if t < 0 or l[idx + 1] < 0:
                    tmp = ceil(t / l[idx + 1])
                else:
                    tmp = t // l[idx + 1]
                dfs(idx + 1, tmp)
                ops[3] += 1
​
        return
​
    max_ans = -sys.maxsize
    min_ans = sys.maxsize
    dfs(0, l[0])
    print(max_ans, min_ans, sep='\n')
    return
​
solution()
​