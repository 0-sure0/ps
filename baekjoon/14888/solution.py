// [문제 링크]: https://www.acmicpc.net/problem/14888

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    op = list(map(int, input().split()))
    max_ans = -sys.maxsize
    min_ans = sys.maxsize
​
    def dfs(idx, value):
        nonlocal max_ans, min_ans
​
        if idx == n:
            max_ans = max(max_ans, value)
            min_ans = min(min_ans, value)
            return
​
        if op[0]:
            op[0] -= 1
            dfs(idx + 1, value + nums[idx])
            op[0] += 1
​
        if op[1]:
            op[1] -= 1
            dfs(idx + 1, value - nums[idx])
            op[1] += 1
​
        if op[2]:
            op[2] -= 1
            dfs(idx + 1, value * nums[idx])
            op[2] += 1
​
        if op[3]:
            op[3] -= 1
            dfs(idx + 1, int(value / nums[idx]))
            op[3] += 1
​
        return
​
    dfs(1, nums[0])
    print(max_ans)
    print(min_ans)
    return
​
solution()
​