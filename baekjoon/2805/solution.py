// [문제 링크]: https://www.acmicpc.net/problem/2805

import sys
​
input = sys.stdin.readline
​
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
​
l = 0
r = max(trees)
​
while l <= r:
    mid = (l + r) // 2
    cutted = [tree - mid if tree > mid else 0 for tree in trees]
    cutted_sum = sum(cutted)
​
    if cutted_sum >= m:
        l = mid + 1
    else:
        r = mid - 1
​
print(r)
​
​