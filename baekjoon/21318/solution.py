// [문제 링크]: https://www.acmicpc.net/problem/21318

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    difficulty = [0] + list(map(int, input().split()))
    t = [0] * (n + 1)
    for i in range(1, n + 1):
        t[i] = t[i - 1]
        if difficulty[i - 1] > difficulty[i]:
            t[i] += 1
​
    q = int(input())
    for _ in range(q):
        x, y = map(int, input().split())
        print(t[y] - t[x])
​
    return
​
solution()
​