// [문제 링크]: https://www.acmicpc.net/problem/1931

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N = int(input())
    conf = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
    end = conf[0][1]
    ans = 1
​
    for i in range(1, len(conf)):
        s, e = conf[i]
        if end <= s:
            end = e
            ans += 1
​
    print(ans)
    return
​
solution()
​