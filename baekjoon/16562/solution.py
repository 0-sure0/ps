// [문제 링크]: https://www.acmicpc.net/problem/16562

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, M, K = map(int, input().split())
    friend = [i for i in range(N + 1)]
    money = [0] + list(map(int, input().split()))
​
    def find(a):
        if a == friend[a]:
            return a
​
        friend[a] = find(friend[a])
        return friend[a]
​
    for _ in range(M):
        v, w = map(int, input().split())
        v = find(v)
        w = find(w)
​
        if money[v] < money[w]:
            friend[w] = friend[v]
            money[w] = 0
        else:
            friend[v] = friend[w]
            money[v] = 0
​
    ans = sum(money)
    print(ans if ans <= K else "Oh no")
    return
​
solution()
​