// [문제 링크]: https://www.acmicpc.net/problem/20438

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, k, q, m = map(int, input().split())
​
    sleep = [0] * (n + 3)
    for s in map(int, input().split()):
        sleep[s] = 1
​
    check = [0] * (n + 3)
    for q in map(int, input().split()):
        if sleep[q]:
            continue
        for i in range(q, n + 3, q):
            if sleep[i]:
                continue
            check[i] = 1
​
    section = [0] * (n + 3)
    for i in range(3, n + 3):
        section[i] = section[i - 1]
        if not check[i]:
            section[i] += 1
​
    for _ in range(m):
        s, e = map(int, input().split())
        print(section[e] - section[s - 1])
​
    return
​
solution()
​