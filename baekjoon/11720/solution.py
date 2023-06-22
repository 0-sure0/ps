// [문제 링크]: https://www.acmicpc.net/problem/11720

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    print(sum(map(int, list(input().rstrip()))))
    return
​
solution()
​