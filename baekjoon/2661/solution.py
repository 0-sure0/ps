// [문제 링크]: https://www.acmicpc.net/problem/2661

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
N = int(input())
​
​
def possible(s):
    jump = 2
    while jump < len(s):
        for i in range(len(s) - jump):
            prev = s[i:i + jump]
            for j in range(i + jump, len(s) - jump + 1, jump):
                if prev == s[j:j+jump]:
                    return False
                prev = s[j:j+jump]
        jump += 1
    return True
​
​
def dfs(s):
    if len(s) == N:
        print(s)
        return True
​
    for i in range(1, 4):
        if s[-1] == str(i):
            continue
​
        t = s + str(i)
        if possible(t):
            if dfs(t):
                return True
​
    return False
​
​
dfs('1')
​