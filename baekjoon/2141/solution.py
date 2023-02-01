// [문제 링크]: https://www.acmicpc.net/problem/2141

import sys
input = sys.stdin.readline
​
X = []
people = 0
n = int(input())
for i in range(n):
    village, num = map(int,input().split())
    X.append([village, num])
    people+=num
​
X.sort(key = lambda x : x[0])
​
count = 0
po = 0
for i in range(n):
    count+=X[i][1]
    if count >= people/2:
      po = X[i][0]
      break 
​
print(po)