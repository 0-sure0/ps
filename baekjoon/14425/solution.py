// [문제 링크]: https://www.acmicpc.net/problem/14425

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
def solution():
    n, m = map(int, input().split())
    dic = defaultdict(int)
    for _ in range(n):
        s = input().rstrip()
        dic[s] = 1
​
    answer = 0
    for _ in range(m):
        if dic[input().rstrip()]:
            answer += 1
​
    print(answer)
    return
​
solution()
​