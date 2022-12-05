// [문제 링크]: https://www.acmicpc.net/problem/9489

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
def solution():
    while True:
        N, K = map(int, input().split())
        if N == K == 0:
            break
        parent = [0] * N
        parent[0] = -1
        nums = list(map(int, input().split()))
        p = -1
        k_idx = 0
        for i in range(1, N):
            if nums[i] == K:
                k_idx = i
            if nums[i] - nums[i-1] > 1:
                p += 1
                parent[i] = p
            else:
                parent[i] = p
        target = parent[parent[k_idx]]
        target_p = parent[k_idx]
        ans = 0
        for i in range(1, N):
            if i == k_idx:
                continue
            if target_p != parent[i] and target == parent[parent[i]]:
                ans += 1
        print(ans)
​
    return
​
​
​
solution()
​