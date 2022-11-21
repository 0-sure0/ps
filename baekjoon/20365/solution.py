// [문제 링크]: https://www.acmicpc.net/problem/20365

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
def solution():
    ids = defaultdict(list)
    prev = ''
    tmp = []
​
    for i, c in enumerate(colors):
        if prev == '':
            prev = c
            tmp.append(i)
            continue
​
        if c == prev:
            tmp.append(i)
        else:
            ids[prev].append(tmp)
            tmp = [i]
            prev = c
​
​
        if i == len(colors) - 1:
            ids[prev].append(tmp)
​
    if len(ids['B']) <= len(ids['R']):
        print(len(ids['B']) + 1)
    elif len(ids['B']) > len(ids['R']):
        print(len(ids['R']) + 1)
​
​
    return
​
​
N = int(input())
colors = list(input())
solution()
​