// [문제 링크]: https://www.acmicpc.net/problem/2263

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
​
def solution():
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
​
    def find_pre(il, ir, pl, pr):
        if il == ir:
            print(inorder[il], end = ' ')
            return
​
        if il > ir or pl > pr:
            return
​
        root = postorder[pr]
        print(root, end=' ')
        mid = il
        while inorder[mid] != root and mid <= ir:
            mid += 1
        find_pre(il, mid - 1, pl, pl + (mid - 1 - il))
        find_pre(mid + 1, ir, pr - 1 - (ir - mid - 1), pr - 1)
        return
​
    find_pre(0, n - 1, 0, n - 1)
​
    return
​
solution()
​