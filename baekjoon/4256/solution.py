// [문제 링크]: https://www.acmicpc.net/problem/4256

import sys
#sys.stdin = open("test.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
​
​
def solution():
    postorder = []
    def make_tree(part):
        nonlocal idx
​
        if idx >= len(preorder) or not part:
            return
​
        if len(part) == 1:
            postorder.append(part[0])
            return
​
        root = preorder[idx]
        mid = 0
        for i in range(len(part)):
            if root == part[i]:
                mid = i
                break
        left, right = part[:mid], part[mid+1:]
        if left:
            idx += 1
            make_tree(left)
        if right:
            idx += 1
            make_tree(right)
        postorder.append(root)
        return
​
    idx = 0
    make_tree(inorder)
    print(*postorder)
    return
​
​
T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    solution()