// [문제 링크]: https://www.acmicpc.net/problem/1717

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
​
​
def check_parent(a, b):
    if a == b:
        return True
​
    cur_a = a
    while parent[cur_a] != cur_a:
        cur_a = parent[cur_a]
​
    cur_b = b
    while parent[cur_b] != cur_b:
        cur_b = parent[cur_b]
​
    if cur_a == cur_b:
        return True
​
    return False
​
​
def change_parent(a, b):
    cur_a = a
    cur_b = b
    while parent[cur_a] != cur_a:
        cur_a = parent[cur_a]
​
    while parent[cur_b] != cur_b:
        cur_b = parent[cur_b]
​
    p = min(parent[cur_a], parent[cur_b])
    parent[cur_a] = p
    parent[cur_b] = p
    return
​
​
for _ in range(M):
    t, a, b = map(int, input().split())
    if t == 1:
        if check_parent(a, b):
            print("yes")
        else:
            print("no")
    else:
        change_parent(a, b)