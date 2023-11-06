// [문제 링크]: https://www.acmicpc.net/problem/3029

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
cur_h, cur_m, cur_s = map(int, input().split(':'))
tgt_h, tgt_m, tgt_s = map(int, input().split(':'))
​
cur_time = cur_h * 3600 + cur_m * 60 + cur_s
tgt_time = tgt_h * 3600 + tgt_m * 60 + tgt_s
if tgt_time <= cur_time:
    tgt_time += 24 * 3600
ans = []
cnt = 3
time = tgt_time - cur_time
while cnt:
    ans.append(str(time // (60 ** (cnt - 1))).zfill(2))
    time %= (60 ** (cnt - 1))
    cnt -= 1
​
print(':'.join(ans))
​