// [문제 링크]: https://www.acmicpc.net/problem/21314

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    min_ans = max_ans = ""
    s = input().rstrip()
    cnt = 0
    for c in s:
        if c == 'M':
            cnt += 1
        else:
            if cnt > 0:
                max_ans += str(5 * 10 ** cnt)
                min_ans += str(10 ** (cnt - 1)) + '5'
            else:
                max_ans += '5'
                min_ans += '5'
            cnt = 0
​
    if cnt != 0:
        min_ans += str(10 ** (cnt - 1))
        max_ans += '1' * cnt
    print(max_ans)
    print(min_ans)
    return
​
solution()
​