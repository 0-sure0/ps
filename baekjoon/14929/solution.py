// [문제 링크]: https://www.acmicpc.net/problem/14929

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
N = int(input())
nums = list(map(int, input().split()))
​
s = 0
t = 0
​
for i in range(len(nums) - 1):
    t += nums[i]
    s += t * nums[i + 1]
​
print(s)
​