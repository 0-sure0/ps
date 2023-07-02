// [문제 링크]: https://www.acmicpc.net/problem/14725

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n = int(input())
    dic = {0: {}}
​
    for _ in range(n):
        k, *info = input().split()
        root = dic[0]
        cur_dic = root
        for char in info:
            cur_dic = cur_dic.setdefault(char, {})
​
    def travel(depth, cur):
        children = sorted(cur)
​
        for child in children:
            print(depth * '--' + child)
            travel(depth + 1, cur[child])
        return
​
    travel(0, dic[0])
    return
​
solution()
​
​
​