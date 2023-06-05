// [문제 링크]: https://www.acmicpc.net/problem/19637

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def solution():
    n, m = map(int, input().split())
    dic = defaultdict(list)
    for i in range(n):
        s, score = input().split()
        if int(score) not in dic:
            dic[int(score)] = s
​
    keys = sorted(dic.keys())
    for _ in range(m):
        l, r = 0, len(keys) - 1
        power = int(input())
​
        while l <= r and keys[l] <= power:
            mid = l + (r - l) // 2
            if keys[mid] == power:
                l = mid
                break
            elif keys[mid] < power:
                l = mid + 1
            else:
                r = mid - 1
​
        print(dic[keys[l]])
​
    return
​
solution()
​
​