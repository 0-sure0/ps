// [문제 링크]: https://www.acmicpc.net/problem/9655

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    N = int(input())
    if N % 2 != 0:
        print('SK')
        return
​
    print('CY')
    return
​
​
solution()
​