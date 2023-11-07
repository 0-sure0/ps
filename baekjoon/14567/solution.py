// [문제 링크]: https://www.acmicpc.net/problem/14567

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict, deque
​
​
N, M = map(int, input().split())
ins = [0] * (N + 1)
ans = [0] * (N + 1)
l = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    ins[b] += 1
    l[a].append(b)
​
q = deque()
for i in range(1, N + 1):
    if ins[i] == 0:
        q.append(i)
​
cnt = 0
while q:
    cnt += 1
    for _ in range(len(q)):
        node = q.popleft()
        ans[node] = cnt
        for next_node in l[node]:
            ins[next_node] -= 1
            if ins[next_node] == 0:
                q.append(next_node)
​
print(*ans[1:])
​
​