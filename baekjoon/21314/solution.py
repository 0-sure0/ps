// [문제 링크]: https://www.acmicpc.net/problem/21314

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    s = input().rstrip()
    max_s = min_s = ''
​
    cnt = 0
    for c in s:
        if c == 'M':
            cnt += 1
        else:
            if cnt > 0:
                max_s += str(5 * (10 ** cnt))
                min_s += str(10 ** (cnt - 1)) + '5'
                cnt = 0
            else:
                max_s += '5'
                min_s += '5'
​
    if cnt > 0:
        max_s += '1' * cnt
        min_s += str(10 ** (cnt - 1))
​
    print(max_s)
    print(min_s)
​
​
    return
​
​
solution()
​