// [문제 링크]: https://www.acmicpc.net/problem/20115

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    drinks.sort()
    for i in range(len(drinks) - 1):
        drinks[-1] += drinks[i] / 2
​
    print(drinks[-1])
​
    return
​
​
​
N = int(input())
drinks = list(map(int, input().split()))
solution()
​