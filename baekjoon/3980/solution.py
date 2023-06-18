// [문제 링크]: https://www.acmicpc.net/problem/3980

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    c = int(input())
​
    def dfs(idx, value):
        nonlocal answer
        if idx == 11 and sum(checked) == 11:
            answer = max(answer, value)
            return
​
        for i, v in player[idx]:
            if not checked[i]:
                checked[i] = 1
                dfs(idx + 1, value + v)
                checked[i] = 0
​
        return
​
    for _ in range(c):
        answer = 0
        player = [[] for _ in range(11)]
        for r in range(11):
            t = list(map(int, input().split()))
            for c in range(11):
                if t[c]:
                    player[r].append((c, t[c]))
        checked = [0] * 11
        dfs(0, 0)
        print(answer)
​
    return
​
solution()
​