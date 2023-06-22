// [문제 링크]: https://www.acmicpc.net/problem/20154

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
from collections import deque
​
def solution():
    cnt = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 3, 'H': 3, 'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 3, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 2, 'X': 2, 'Y': 2, 'Z': 1}
    s = deque([cnt[c] for c in list(input().rstrip())])
​
    while len(s) > 1:
        t = 0
        if len(s) % 2 == 1:
            t = s.pop()
​
        for _ in range(len(s) // 2):
            n1 = s.popleft()
            n2 = s.popleft()
            s.append(n1 + n2)
        if t:
            s.append(t)
​
    if (s[0] % 10) % 2 == 0:
        print("You're the winner?")
    else:
        print("I'm a winner!")
    return
​
solution()
​