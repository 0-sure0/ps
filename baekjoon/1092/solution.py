// [문제 링크]: https://www.acmicpc.net/problem/1092

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N = int(input())
    crane = list(map(int, input().split()))
    crane.sort(reverse=True)
    M = int(input())
    box = list(map(int, input().split()))
    box.sort(reverse=True)
​
    if box[0] > crane[0]:
        print(-1)
        return
    ans = 0
    while box:
        ans += 1
        for c in crane:
            for i in range(len(box)):
                if c >= box[i]:
                    box.pop(i)
                    break
    print(ans)
    return
​
​
solution()
​