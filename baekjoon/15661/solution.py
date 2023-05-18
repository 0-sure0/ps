// [문제 링크]: https://www.acmicpc.net/problem/15661

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import combinations
​
​
def solution():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    total = set(range(n))
    answer = sys.maxsize
    
​
    for i in range(1, n // 2 + 1):
        for comb in combinations(range(n), i):
            t = t2 = 0
            start = set(comb)
            link = total - start
​
            for i in start:
                for j in start:
                    t += s[i][j]
​
            for i in link:
                for j in link:
                    t2 += s[i][j]
​
            answer = min(answer, abs(t - t2))
            
    print(answer)
    return
​
​
solution()