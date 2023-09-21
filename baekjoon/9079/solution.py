// [문제 링크]: https://www.acmicpc.net/problem/9079

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
​
def solution():
    T = int(input())
​
    def bfs(num):
        q = deque()
        q.append((num, 0))
        int_num = int(''.join(num), 2)
        visited[int_num] = 1
​
        while q:
            num, cnt = q.popleft()
            int_num = int(''.join(num), 2)
            if int_num == 0 or int_num == 511:
                return cnt
​
            for case in cases:
                t = num[:]
                for c in case:
                    if num[c] == '1':
                        t[c] = '0'
                    else:
                        t[c] = '1'
                int_t = int(''.join(t), 2)
                if not visited[int_t]:
                    visited[int_t] = 1
                    q.append((t, cnt + 1))
​
        return -1
​
    for _ in range(T):
        num = []
        visited = [0] * 512
        cases = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for _ in range(3):
            s = input().split()
            for c in s:
                if c == 'H':
                    num.append('1')
                else:
                    num.append('0')
​
        print(bfs(num))
​
    return
​
​
solution()