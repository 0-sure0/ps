// [문제 링크]: https://www.acmicpc.net/problem/1548

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    if n < 3:
        print(n)
        return
    nums = sorted(map(int, input().split()))
    answer = 2
​
    for s in range(n - 2):
        e = s + 2
        while True:
            if e == n:
                break
            if nums[s] + nums[s + 1] > nums[e]:
                answer = max(answer, e - s + 1)
                e += 1
            else:
                break
    print(answer)
    return
​
solution()
​
​