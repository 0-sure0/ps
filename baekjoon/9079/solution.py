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
    def flip(numbers, arr):
        for number in numbers:
            arr[number] = '1' if arr[number] == '0' else '0'
        return arr
​
    def bfs():
        cases = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        visited = [0] * 512
        visited[int(''.join(arr), 2)] = 1
        q = deque([(int(''.join(arr), 2), 0)])
​
        while q:
            arrbin, cnt = q.popleft()
            if arrbin == 0 or arrbin == 511:
                return cnt
​
            for i, numbers in enumerate(cases):
                newarr = int(''.join(flip(numbers, list(bin(arrbin)[2:].zfill(9)))), 2)
                if not visited[newarr]:
                    visited[newarr] = 1
                    q.append((newarr, cnt + 1))
        return -1
​
    for _ in range(T):
        arr = list(list(input().split()) for _ in range(3))
        arr = ['1' if arr[y][x] == 'H' else '0' for y in range(3) for x in range(3)]
        print(bfs())
​
    return
​
​
solution()