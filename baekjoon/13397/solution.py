// [문제 링크]: https://www.acmicpc.net/problem/13397

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
​
    def count_section(value):
        min_num = max_num = nums[0]
        cnt = 1
        for i in range(1, n):
            max_num = max(max_num, nums[i])
            min_num = min(min_num, nums[i])
​
            if max_num - min_num > value:
                cnt += 1
                max_num = min_num = nums[i]
​
        return cnt
​
    answer = 0
    l, r = 0, max(nums)
    while l <= r:
        mid = l + (r - l) // 2
        if count_section(mid) <= m:
            r = mid - 1
            answer = mid
        else:
            l = mid + 1
​
    print(answer)
    return
​
​
solution()
​