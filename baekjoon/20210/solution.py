// [문제 링크]: https://www.acmicpc.net/problem/20210

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from functools import cmp_to_key
​
​
def comp(f1, f2):
    i = 0
    f1 = to_list(f1)
    f2 = to_list(f2)
​
    while i < min(len(f1), len(f2)):
        if f1[i] == f2[i]:
            i += 1
            continue
​
        if f1[i].isdigit():
            if f2[i].isdigit():
                if int(f1[i]) == int(f2[i]):
                    l1 = len(f1[i]) - len(f1[i].lstrip('0'))
                    l2 = len(f2[i]) - len(f2[i].lstrip('0'))
                    return -1 if l1 < l2 else 1
                return -1 if int(f1[i]) < int(f2[i]) else 1
            else:
                return -1
        else:
            if f2[i].isdigit():
                return 1
            else:
                if f1[i].lower() == f2[i].lower():
                    return -1 if f1[i] < f2[i] else 1
                return -1 if f1[i].lower() < f2[i].lower() else 1
        i += 1
​
    return -1 if len(f1) < len(f2) else 1
​
​
def to_list(file):
    l = []
    i = 0
​
    while i < len(file):
        if file[i].isdigit():
            t = ''
            end = i
            while end < len(file) and file[end].isdigit():
                t += file[end]
                end += 1
            l.append(t)
            i = end
        else:
            l.append(file[i])
            i += 1
​
    return l
​
​
def solution():
    print(*sorted([input().rstrip() for _ in range(int(input()))], key=cmp_to_key(comp)), sep='\n')
    return
​
solution()
​