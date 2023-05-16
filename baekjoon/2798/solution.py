// [문제 링크]: https://www.acmicpc.net/problem/2798

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N, M = map(int, input().split())
    card = sorted(list(map(int, input().split())), reverse=True)
    answer = 0
​
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if card[i] + card[j] + card[k] <= M:
                    answer = max(answer, card[i] + card[j] + card[k])
    print(answer)
    return
​
​
solution()
​