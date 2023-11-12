// [문제 링크]: https://www.acmicpc.net/problem/14725

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
N = int(input())
dic = {}
​
for _ in range(N):
    s = input().split()[1:]
    cur = dic
    
    for i in range(len(s)):
        if s[i] not in cur:
            cur[s[i]] = {}
        cur = cur[s[i]]
​
​
def dic_print(l, k, cur):
    print('--' * l + k)
    for next_k in sorted(cur.keys()):
        dic_print(l + 1, next_k, cur[next_k])
    return
​
​
for k in sorted(dic.keys()):
    dic_print(0, k, dic[k])
​