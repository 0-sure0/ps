// [문제 링크]: https://www.acmicpc.net/problem/5639

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
​
def postorder(tree):
    if not tree:
        return
​
    if len(tree) == 1:
        print(tree[0])
        return
​
    root = tree[0]
    mid = len(tree)
    for i in range(1, len(tree)):
        if root < tree[i]:
            mid = i
            break
​
    if mid == len(tree):
        postorder(tree[1:])
    else:
        postorder(tree[1:mid])
        postorder(tree[mid:])
    print(root)
​
    return
​
l = []
while True:
    try:
        n = int(input())
        l.append(n)
    except ValueError:
        break
​
postorder(l)