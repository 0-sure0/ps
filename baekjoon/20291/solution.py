// [문제 링크]: https://www.acmicpc.net/problem/20291

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def solution():
    n = int(input())
    answer = defaultdict(int)
​
    for _ in range(n):
        s = input().rstrip().split('.')
        answer[s[1]] += 1
​
    for k, v in sorted(answer.items()):
        print(k, v)
    return
​
solution()
​