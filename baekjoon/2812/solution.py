// [문제 링크]: https://www.acmicpc.net/problem/2812

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, k = map(int, input().split())
    num = input().rstrip()
    if n <= 2:
        print(num)
        return
​
    stk = [num[0]]
    for c in num[1:]:
        while k and stk and int(stk[-1]) < int(c):
            stk.pop()
            k -= 1
        stk.append(c)
        
    while k:
        stk.pop()
        k -= 1
        
    print(''.join(stk))
    return
​
solution()
​