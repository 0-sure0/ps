// [문제 링크]: https://www.acmicpc.net/problem/2805

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, m = map(int, input().split())
    tree = list(map(int, input().split()))    
    l, r = 0, max(tree)    
    
    while l <= r:
        tmp_h = l + (r - l) // 2
        tmp = 0
        for t in tree:
            tmp += max(0, t - tmp_h)
​
        if tmp >= m:            
            l = tmp_h + 1
            
        else:
            r = tmp_h - 1
​
    print(r)
    return
​
solution()
​
​