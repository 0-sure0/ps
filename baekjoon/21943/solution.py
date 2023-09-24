// [문제 링크]: https://www.acmicpc.net/problem/21943

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from itertools import permutations
​
​
def solution():
    N = int(input())
    nums = sorted(map(int, input().split()))
    P, Q = map(int, input().split())
    answer = 0
​
    def dfs(idx, cnt, position, t_nums):
        nonlocal answer
​
        if (cnt + N - 1 - idx) < Q:
            return
​
        if idx == N - 1:
            position.append(idx)
            mul, sum = 1, 0
            cur_idx = 0
​
            for mul_idx in position:
                while cur_idx <= mul_idx:
                    sum += t_nums[cur_idx]
                    cur_idx += 1
                mul *= sum
                sum = 0
​
            answer = max(answer, mul)
            position.pop()
            return
​
        dfs(idx + 1, cnt, position, t_nums)
        position.append(idx)
        if cnt + 1 <= Q:
            dfs(idx + 1, cnt + 1, position, t_nums)
        position.pop()
        return
​
    for perm in permutations(nums):
        dfs(0, 0, [], perm)
​
    print(answer)
    return
​
​
solution()