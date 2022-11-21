// [문제 링크]: https://www.acmicpc.net/problem/21314

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    max_ans = min_ans = ''
    m_cnt = 0
    for c in s:
        if c == 'M':
            m_cnt += 1
        else:
            if m_cnt == 0:
                min_ans += '5'
                max_ans += '5'
            else:
                min_ans += str(10 ** m_cnt + 5)
                max_ans += str(10 ** m_cnt * 5)
                m_cnt = 0
​
    if m_cnt != 0:
        max_ans += '1' * m_cnt
        min_ans += str(10 ** (m_cnt - 1))
    print(max_ans)
    print(min_ans)
    return
​
​
s = input().rstrip()
solution()