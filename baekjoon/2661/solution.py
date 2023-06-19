// [문제 링크]: https://www.acmicpc.net/problem/2661

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
​
    def dfs(idx):
        nonlocal s
        
        for i in range(1, idx // 2 + 1):
            if s[-i:] == s[-2 * i: -i]:
                return False
​
        if idx == n:
            print(''.join(s))
            return True
​
​
        for i in range(1, 4):
            s.append(str(i))
            if dfs(idx + 1):
                return True
            s.pop()
​
        return False
​
    s = []
    dfs(0)
    return
​
​
solution()