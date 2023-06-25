// [문제 링크]: https://www.acmicpc.net/problem/4659

import sys
#.stdin = open('test.txt', 'r')
input = sys.stdin.readline
​
​
def solution():
​
    def is_vowel(c):
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            return True
        return False
​
    while True:
        flag = False
        s = input().rstrip()
        if s == 'end':
            break
        v_cnt = 0
        vowel_check = False
        for i in range(len(s)):
            if is_vowel(s[i]):
                vowel_check = True
                if v_cnt > 0:
                    v_cnt += 1
                    if v_cnt >= 3:
                        flag = True
                        break
                else:
                    v_cnt = 1
​
                if i > 0 and s[i] != 'e' and s[i] != 'o' and s[i - 1] == s[i]:
                    flag = True
                    break
            else:
                if v_cnt < 0:
                    v_cnt -= 1
                    if v_cnt <= -3:
                        flag = True
                        break
                else:
                    v_cnt = -1
​
                if i > 0 and s[i] == s[i - 1]:
                    flag = True
                    break
​
        if flag or not vowel_check:
            print(f'<{s}> is not acceptable.')
        else:
            print(f'<{s}> is acceptable.')
​
    return
​
solution()
​