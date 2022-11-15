// [문제 링크]: https://www.acmicpc.net/problem/1758

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    tips = [int(input()) for _ in range(N)]
    tips.sort(reverse=True)
​
    ans = 0
    for i, tip in enumerate(tips, start=1):
        tip -= i - 1
        ans += tip if tip > 0 else 0
​
    print(ans)
​
    return
​
​
N = int(input())
​
solution()
​