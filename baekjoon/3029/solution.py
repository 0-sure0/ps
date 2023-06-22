// [문제 링크]: https://www.acmicpc.net/problem/3029

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    h, m, s = map(int, input().split(':'))
    t = h * 3600 + m * 60 + s
    th, tm, ts = map(int, input().split(':'))
    tt = th * 3600 + tm * 60 + ts
    answer = tt - t
​
    if answer < 0:
        answer += 24 * 3600
    elif answer == 0:
        print('24:00:00')
        return
​
    ah = str(answer // 3600).zfill(2)
    answer %= 3600
    am = str(answer // 60).zfill(2)
    answer %= 60
    asec = str(answer).zfill(2)
    print(ah + ':' + am + ':' + asec)
    return
​
solution()
​