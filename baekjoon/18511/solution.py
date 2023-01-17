// [문제 링크]: https://www.acmicpc.net/problem/18511

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    N, K = input().split()
    ks = list(input().split())
    ks.sort(reverse=True)
    ans = 0
    tmp = [ks[-1]] * len(N)
    if int(''.join(tmp)) > int(N):
        ans = int(ks[0] * (len(N) - 1))
        print(ans)
        return
​
    for i in range(len(N)):
        for k in ks:
            tmp[i] = k
            if int(N) >= int(''.join(tmp)):
                ans = max(ans, int(''.join(tmp)))
                break
    print(ans)
    return
​
solution()
​