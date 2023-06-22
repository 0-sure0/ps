// [문제 링크]: https://www.acmicpc.net/problem/16916

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    s = input().rstrip()
    p = input().rstrip()
    print(int(p in s))
    return
​
solution()
​