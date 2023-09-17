// [문제 링크]: https://www.acmicpc.net/problem/22946

from collections import defaultdict
import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import math
​
n = int(input())
circles = [list(map(int, input().split())) for _ in range(n)]
circles.append((0, 0, 2000000))
inside = [(i, []) for i in range(n+1)]
​
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            continue
        Xa, Ya, Ra = circles[i]
        Xb, Yb, Rb = circles[j]
        distance = math.sqrt((Xa-Xb) * (Xa-Xb) + (Ya-Yb) * (Ya-Yb))
        Rab = Ra-Rb
        if distance < Rab:
            inside[i][1].append(j)
​
inside.sort(key=lambda x: len(x[1]))
​
res = defaultdict(int)
​
route = [[] for _ in range(n + 1)]
visit = [True for _ in range(n + 1)]
res = defaultdict(int)
​
for v, children in inside:
    for child in children:
        if visit[child]:
            route[v].append(child)
            visit[child] = False
        res[v] = max(res[v], res[child] + 1)
​
result = 0
​
for i in range(n+1):
    result = max(result, res[i])
    for child1 in route[i]:
        for child2 in route[i]:
            if child1 == child2:
                continue
            a = res[child1]
            b = res[child2]
            result = max(result, a+b+2)
​
​
print(result)
​