// [문제 링크]: https://www.acmicpc.net/problem/16953

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    global B
    ans = -1
    cnt = 1
​
    while True:
        if len(str(A)) > len(str(B)) or A > B:
            break
​
        if A == B:
            ans = cnt
            break
​
        if B % 2 == 0:
            B //= 2
            cnt += 1
​
        else:
            B = str(B)
            if B[-1] == '1':
                B = int(B[:-1])
                cnt += 1
            else:
                break
​
​
    print(ans)
​
    return
​
​
A, B = map(int, input().split())
solution()
​