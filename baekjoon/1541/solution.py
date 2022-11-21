// [문제 링크]: https://www.acmicpc.net/problem/1541

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    f = []
    t = ''
    for c in s:
        if c != '+' and c != '-':
            t += c
        else:
            if f and f[-1] == '+':
                f.pop()
                n1 = f.pop()
                n2 = int(t)
                t = ''
                f.append(n1 + n2)
                f.append(c)
            else:
                f.append(int(t))
                t = ''
                f.append(c)
​
    if t:
        if f and f[-1] == '+':
            f.pop()
            n1 = f.pop()
            n2 = int(t)
            f.append(n1 + n2)
        else:
            f.append(int(t))
    f = list(map(str, f))
    ans = eval(''.join(f))
    print(ans)
​
    return
​
​
s = input()
solution()
​