// [문제 링크]: https://www.acmicpc.net/problem/1969

import sys
#sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
    n, m = map(int, input().split())
    dna = [input().rstrip() for _ in range(n)]
    answer = ''
    distance = 0
    for j in range(m):
        t = a = g = c = 0
        for i in range(n):
            if dna[i][j] == 'T':
                t += 1
            elif dna[i][j] == 'A':
                a += 1
            elif dna[i][j] == 'G':
                g += 1
            elif dna[i][j] == 'C':
                c += 1
​
        if max(t, a, g, c) == a:
           answer += 'A'
           distance += g + c + t
        elif max(t, a, g, c) == c:
            answer += 'C'
            distance += t + g + a
        elif max(t, a, g, c) == g:
            answer += 'G'
            distance += t + a + c
        elif max(t, a, g, c) == t:
            answer += 'T'
            distance += c + a + g
    print(answer)
    print(distance)
    return
​
​
solution()
​