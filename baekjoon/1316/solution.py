// [문제 링크]: https://www.acmicpc.net/problem/1316

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
def solution():
    n = int(input())
    ans = 0
    for _ in range(n):
        char = defaultdict(int)
        s = input().rstrip()
        flag = False
        for i in range(len(s)):
            if char[s[i]]:
                if s[i - 1] == s[i]:
                    continue
                else:
                    flag = True
                    break
            char[s[i]] = 1
        if flag:
            continue
        ans += 1
​
    print(ans)
    return
​
solution()
​