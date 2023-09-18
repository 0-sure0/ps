// [문제 링크]: https://www.acmicpc.net/problem/1969

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import Counter
​
def solution():
    N, M = map(int, input().split())
    words = [input().rstrip() for _ in range(N)]
    count = [[] for _ in range(M)]
    for word in words:
        for i in range(M):
            count[i].append(word[i])
​
    answer = ''
    cnt = 0
    for i in range(M):
        count[i] = Counter(count[i])
        common = sorted(count[i].most_common(), key=lambda x: (-x[1], x[0]))
        answer += common[0][0]
        for c, v in common[1:]:
            cnt += v
​
    print(answer)
    print(cnt)
    return
​
solution()