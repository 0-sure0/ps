// [문제 링크]: https://www.acmicpc.net/problem/20440

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import defaultdict
​
​
N = int(input())
dic = defaultdict(int)
for _ in range(N):
    s, e = map(int, input().split())
    dic[s] += 1
    dic[e] -= 1
​
ans = cur = 0
answer = [0, 0]
flag = False
​
for k in sorted(dic.keys()):
    cur += dic[k]
    if cur > ans:
        ans = cur
        answer[0] = k
        flag = True
​
    elif cur < ans and flag:
        answer[1] = k
        flag = False
​
print(ans)
print(*answer)
​